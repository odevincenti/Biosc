import sys
import json
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QProcess, Slot
import numpy as np
from Interfaz.comm_protocol import Commands
from template_ui import Ui_Bioscope
from comm_protocol import BioscSerial

TEST_SIG_LEN = 2_000_000
PROCESS_PATH = 'comm_protocol.py'


class MainWindow(QMainWindow, Ui_Bioscope):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Bioscope')

        # Setup process for connection to ESP32
        self.process = QProcess(self)
        self.process_path = PROCESS_PATH
        self.start_process()

        # Dummy signals for testing
        self.dummy_signal = 100 * np.sin(2 * np.pi * 1e-4 * np.arange(TEST_SIG_LEN)) + 5 * np.random.normal(
            size=TEST_SIG_LEN)
        self.CH1_data = self.dummy_signal
        self.update_plot()

        self.buttonRunStop.clicked.connect(self.on_click_push_run)

        # Connect the spinbox to the plot
        self.spinScaleCH1.valueChanged.connect(self.update_plot)

        # Connect the trigger button to the trigger line method from the plot widget
        self.setup_capture_combo()
        self.comboMode.currentTextChanged.connect(self.setup_capture_combo)
        self.comboMode.setCurrentText('Trigger')

    ###################################################################################
    #               ESP32 Communication Methods                                       #
    ###################################################################################

    @Slot()
    def on_click_push_run(self):
        self.process.write(f"{Commands.MEASURED_SIGNALS}\n".encode())


    def start_process(self):
        self.process.start('python', [self.process_path])

        started = self.process.waitForStarted(500)
        if not started:
            sys.exit(1)

        # Automatically read stdout and stderr when something new shows up
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        # self.process.readyReadStandardError.connect(self.handle_stderr)

    def handle_stdout(self):
        message = self.process.readAllStandardOutput().data().decode()
        if not message:
            pass
        command, data = message.split('-')
        if command == Commands.MEASURED_SIGNALS:
            self.CH1_data = np.array(json.loads(data)[0]['signal'])
            self.update_plot()
        print(message)

    def update_plot(self):
        scale = self.spinScaleCH1.value()
        self.plotWidget.clear()
        self.plotWidget.plot(self.CH1_data / scale, pen=(255, 0, 0))

    # Kill process when closing the window
    def closeEvent(self, event):
        self.process.kill()
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
        # Enable the trigger line
        self.plotWidget.set_trigger_line()

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
