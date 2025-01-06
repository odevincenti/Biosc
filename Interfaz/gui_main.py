import sys
import json
from json import JSONDecodeError
from pyqtgraph import mkPen
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot
import numpy as np
from comm_protocol import Commands
from main_window_template import Ui_Bioscope
from qt_serial_monitor import ESPSerial

PROCESS_PATH = 'comm_protocol.py'
SAMPLING_RATE = 10_000
MAX_SIG_LEN = 505 * SAMPLING_RATE # 30 seconds

class MainWindow(QMainWindow, Ui_Bioscope):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Bioscope')

        # Setup process for connection to ESP32
        self.esp_serial = ESPSerial()
        self.esp_serial.data_received.connect(self.handle_newdata)

        # Plot utilities
        self.pen_CH1 = mkPen(color=(255, 0, 0), width=2)

        # Dummy signals for testing
        self.dummy_signal = np.zeros(MAX_SIG_LEN)
        self.CH1_data = self.dummy_signal
        self.update_plot()

        # Run button
        self.buttonRunStop.clicked.connect(self.on_click_push_run)

        # Connect the spinbox to the plot
        self.frameCH1.spinScale.valueChanged.connect(self.update_plot)

        # Connect the trigger button to the trigger line method from the plot widget
        self.setup_capture_combo()
        self.comboMode.currentTextChanged.connect(self.setup_capture_combo)
        self.comboMode.setCurrentText('Trigger')

    ###################################################################################
    #               ESP32 Communication Methods                                       #
    ###################################################################################

    @Slot()
    def on_click_push_run(self):
        """
        Start running
        """
        self.esp_serial.send_command(Commands.RUN)


    @Slot(str)
    def handle_newdata(self, message: str):
        """
        Read incoming data from the ESP32 process
        :return:
        """
        try:
            message = json.loads(message)
        except (JSONDecodeError, ValueError):
            print(80*'=')
            print('JSON ERROR')
            print(message)
            return

        if message["command"] == Commands.MEASURED_SIGNALS:
            new_data = np.array(message['data'][0]['signal']) / 255
            new_range = np.array(message['data'][0]['range']) * 1000
            new_data = new_data * (new_range[1] - new_range[0]) + new_range[0]
            self.CH1_data = np.concatenate((self.CH1_data, new_data))
            if len(self.CH1_data) > MAX_SIG_LEN:
                self.CH1_data = self.CH1_data[-MAX_SIG_LEN:]
            self.update_plot()

    def update_plot(self):
        scale = self.frameCH1.spinScale.value()
        offset = self.frameCH1.spinOffset.value()
        self.plotWidget.clear()
        time_scale = self.plotWidget.getViewBox().viewRange()[0]
        n_samples = int((time_scale[1] - time_scale[0]) * SAMPLING_RATE / 1_000_000) # in ms
        x_axis = np.linspace(time_scale[0], time_scale[1], n_samples)
        plot_sig = (self.CH1_data[-len(x_axis):]) / scale + offset
        self.plotWidget.plot(x_axis, plot_sig, pen=self.pen_CH1)

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