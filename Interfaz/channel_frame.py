from PySide6.QtWidgets import QFrame, QCheckBox, QLabel, QDoubleSpinBox, QFormLayout, QVBoxLayout, QMainWindow, \
    QApplication, QWidget
from scale_spin_box import ScaleSpinBox
from PySide6.QtCore import QEvent


class ChannelFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.formLayout = QFormLayout(self)
        self.checkChannel = QCheckBox(self)
        self.labelOffset = QLabel(self)
        self.spinOffset = QDoubleSpinBox(self)
        self.labelScale = QLabel(self)
        self.spinScale = ScaleSpinBox(self)

    def event(self, event):
        if event.type() == QEvent.Type.DynamicPropertyChange:
            self.setup_ui()
        return super().event(event)

    def setup_ui(self):
        channel_name = self.property("channelName") or "Channel"
        color = self.property("frameColor") or "rgb(246, 97, 81)"

        self.setObjectName(f"frame{channel_name}")
        self.setStyleSheet(f"border-color: {color};")
        self.setFrameShape(QFrame.Shape.NoFrame)

        self.formLayout.setObjectName(f"formLayout_{channel_name}")

        self.checkChannel.setObjectName(f"check{channel_name}")
        self.checkChannel.setStyleSheet(f"background-color: {color};\ncolor: rgb(0, 0, 0);")
        self.checkChannel.setText(channel_name)
        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.checkChannel)

        self.labelOffset.setObjectName(f"label{channel_name}offset")
        self.labelOffset.setText("Offset:")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelOffset)

        self.spinOffset.setObjectName(f"spin{channel_name}offset")
        self.spinOffset.setMinimum(-5)
        self.spinOffset.setMaximum(+5)
        self.spinOffset.setSingleStep(0.05)
        self.spinOffset.setSuffix(" div")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinOffset)

        self.labelScale.setObjectName(f"label{channel_name}scale")
        self.labelScale.setText("Scale:")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelScale)

        self.spinScale.setObjectName(f"spinScale{channel_name}")
        self.spinScale.setSuffix("mV")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinScale)


def main():
    """
    Create a main window with multiple ChannelFrame widgets,
    to test the ChannelFrame class.
    """
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

    app = QApplication(sys.argv)
    window = QMainWindow()
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)

    # Create multiple ChannelFrame widgets
    frame1 = ChannelFrame(central_widget)
    frame1.setProperty("channelName", "Channel 1")
    frame1.setProperty("frameColor", "rgb(246, 97, 81)")
    layout.addWidget(frame1)

    frame2 = ChannelFrame(central_widget)
    frame2.setProperty("channelName", "Channel 2")
    frame2.setProperty("frameColor", "rgb(143, 240, 164)")
    layout.addWidget(frame2)

    window.setCentralWidget(central_widget)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
