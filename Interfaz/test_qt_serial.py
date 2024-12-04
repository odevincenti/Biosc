from PySide6.QtCore import QObject, Signal, Slot, QThread
from qt_esp_comm import ESPSerial  # Make sure this matches your file name
from comm_protocol import Commands
import sys

BAUD_RATE = 961_200


