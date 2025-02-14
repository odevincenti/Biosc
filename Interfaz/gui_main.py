import sys
import json
from json import JSONDecodeError
from pyqtgraph import mkPen
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot, QTimer
from PySide6.QtGui import QIcon
import numpy as np
from comm_protocol import Commands
from main_window_template import Ui_Bioscope
from qt_serial_monitor import ESPSerial
from typing import List, Tuple, Dict, TypedDict

class SignalData(TypedDict):
    channel: int
    range: List[int]
    signal: List[int]


SAMPLING_RATE = 10_000
MAX_SIG_LEN = 505 * SAMPLING_RATE  # 30 seconds


class MainWindow(QMainWindow, Ui_Bioscope):
    STATE_IDLE = 0
    STATE_RUNNING = 1
    FRAME_RATE = 30

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Bioscope')
        self.state = self.STATE_IDLE

        # Setup process for connection to ESP32
        self.esp_serial = ESPSerial()
        self.esp_serial.data_received.connect(self.handle_newdata)

        # Dummy signals for testing
        self.dummy_signal = np.zeros(MAX_SIG_LEN)
        self.CH1_data = self.dummy_signal

        # Run button
        self.buttonRunStop.clicked.connect(self.on_click_push_run_stop)

        # Channel frames
        self.channel_frames = [self.frameCH1, self.frameCH2, self.frameCH3, self.frameCH4]
        self.channel_data = [self.dummy_signal, self.dummy_signal, self.dummy_signal, self.dummy_signal]
        self.channel_pens = [mkPen(color=eval(frame.color.strip('rgb')), width=2) for frame in self.channel_frames]

        # Timer for updating the plot
        self.plot_timer = QTimer(self)
        self.plot_timer.timeout.connect(self.update_plot)
        self.plot_timer.start(1000 // self.FRAME_RATE)

        # # Connect the spinbox to the plot
        # self.frameCH1.spinScale.valueChanged.connect(self.update_plot)

    def channel_is_enabled(self, idx: int) -> bool:
        # Use the checkbox to verify selection
        return self.channel_frames[idx].checkEnabled.isChecked()

    def update_run_button_to_stop(self):
        """
        Update the RUN button to act as a STOP button during recording.
        """
        self.buttonRunStop.setText("STOP")
        self.buttonRunStop.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.buttonRunStop.clicked.disconnect()
        self.buttonRunStop.clicked.connect(self.on_click_push_run_stop)
        self.buttonRunStop.setStyleSheet(
            u"color: rgb(0,0,0);\n"
            u"font: 700 11pt \"Arial\";")

    def reset_stop_button_to_run(self):
        """
        Reset the RUN button to its original state.
        """
        self.buttonRunStop.setText("RUN")
        self.buttonRunStop.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.buttonRunStop.clicked.disconnect()
        self.buttonRunStop.clicked.connect(self.on_click_push_run_stop)
        self.buttonRunStop.setStyleSheet(
            u"color: rgb(0,0,0);\n"
            u"font: 700 11pt \"Arial\";")

    ###################################################################################
    #               ESP32 Communication Methods                                       #
    ###################################################################################

    @Slot()
    def on_click_push_run_stop(self):
        """
        Start running
        """
        if self.state == self.STATE_IDLE:
            self.esp_serial.send_command(Commands.RUN)
            self.state = self.STATE_RUNNING
            self.update_run_button_to_stop()
        elif self.state == self.STATE_RUNNING:
            self.esp_serial.send_command(Commands.STOP)
            self.state = self.STATE_IDLE
            self.reset_stop_button_to_run()
            # Clear the data
            self.channel_data = [self.dummy_signal, self.dummy_signal, self.dummy_signal, self.dummy_signal]
            self.update_plot()


    @staticmethod
    def parse_new_signal(signal_data: SignalData) -> np.ndarray:
        """
        Given signal data for channel, range, and samples, convert it to a numpy array and rescale
        """
        new_data = np.array(signal_data['signal']) / 255
        new_range = np.array(signal_data['range']) * 1000
        new_data = new_data * (new_range[1] - new_range[0]) + new_range[0]
        return new_data

    @Slot(str)
    def handle_newdata(self, message: str):
        """
        Read incoming data from the ESP32 process
        :return:
        """
        try:
            message = json.loads(message)
        except (JSONDecodeError, ValueError):
            print(80 * '=')
            print('JSON ERROR')
            print(message)
            return

        if message["command"] == Commands.MEASURED_SIGNALS:
            for i, signal_data in enumerate(message['data']):
                channel_idx = signal_data['channel'] - 1  # 0 based indexing
                assert 0 <= channel_idx < 4, f'Invalid channel index: {channel_idx}'
                if not self.channel_is_enabled(channel_idx):
                    continue

                # Roll in new data. In the future, this should be handled by the capture mode
                new_data = self.parse_new_signal(signal_data)
                self.channel_data[channel_idx] = np.roll(self.channel_data[channel_idx], -len(new_data))
                self.channel_data[channel_idx][-len(new_data):] = new_data

    def update_plot(self):
        """
        Currently, this function updates in rolling mode
        In the future, it should handle the different capture modes
        """
        self.plotWidget.clear()
        time_scale = self.plotWidget.getViewBox().viewRange()[0]
        n_samples = int((time_scale[1] - time_scale[0]) * SAMPLING_RATE / 1_000_000)  # in ms
        x_axis = np.linspace(time_scale[0], time_scale[1], n_samples)

        for i, frame in enumerate(self.channel_frames):
            if not self.channel_is_enabled(i):
                continue
            scale = frame.spinScale.value()
            offset = frame.spinOffset.value()
            plot_sig = (self.channel_data[i][-len(x_axis):]) / scale + offset
            self.plotWidget.plot(x_axis, plot_sig, pen=self.channel_pens[i])

    def closeEvent(self, event):
        """Handle window close event."""
        self.esp_serial.send_command(Commands.STOP)
        self.esp_serial.close()
        event.accept()

    ###################################################################################
    #               Capture Methods                                                   #
    ###################################################################################

    def setup_capture_combo(self):
        capture_mode = self.comboMode.currentText()
        if capture_mode == 'Trigger':
            self.setup_capture_trigger()
        else:
            # Disable all trigger related widgets, and trigger line
            self.plotWidget.remove_trigger_line()
            self.comboTriggerCH.setEnabled(False)
            self.comboTriggerSet.setEnabled(False)

            if capture_mode == 'Roll':
                self.setup_capture_roll()
            elif capture_mode == 'XY':
                self.setup_capture_xy()

    def setup_capture_trigger(self):
        # Enable the trigger channel and trigger set widgets
        self.comboTriggerCH.setEnabled(True)
        self.comboTriggerSet.setEnabled(True)

    def setup_capture_roll(self):
        print('roll selected')

    def setup_capture_xy(self):
        print('xy selected')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
