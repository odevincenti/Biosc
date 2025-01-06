from PySide6.QtWidgets import QFrame, QCheckBox, QLabel, QSpinBox, QFormLayout
from custom_widgets import CustomScaleSpinBox
from PySide6.QtCore import QEvent

class ChannelFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.formLayout = QFormLayout(self)
        self.checkChannel = QCheckBox(self)
        self.labelOffset = QLabel(self)
        self.spinOffset = QSpinBox(self)
        self.labelScale = QLabel(self)
        self.spinScale = CustomScaleSpinBox(self)

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
        self.spinOffset.setMinimum(-1000)
        self.spinOffset.setMaximum(1000)
        self.spinOffset.setSingleStep(5)
        self.spinOffset.setSuffix("mV")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinOffset)

        self.labelScale.setObjectName(f"label{channel_name}scale")
        self.labelScale.setText("Scale:")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelScale)

        self.spinScale.setObjectName(f"spinScale{channel_name}")
        self.spinScale.setSuffix("mV")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinScale)