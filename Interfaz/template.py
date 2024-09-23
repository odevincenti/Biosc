# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Bioscope(object):
    def setupUi(self, Bioscope):
        Bioscope.setObjectName("Bioscope")
        Bioscope.resize(1003, 650)
        self.centralwidget = QtWidgets.QWidget(parent=Bioscope)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = SignalPlotter(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 90, 771, 521))
        self.widget.setObjectName("widget")
        self.FrameControlScope = QtWidgets.QFrame(parent=self.centralwidget)
        self.FrameControlScope.setGeometry(QtCore.QRect(0, 0, 521, 91))
        self.FrameControlScope.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"alternate-background-color: rgb(119, 118, 123);\n"
"color: rgb(0, 0, 0);")
        self.FrameControlScope.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.FrameControlScope.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.FrameControlScope.setObjectName("FrameControlScope")
        self.buttonSingle = QtWidgets.QPushButton(parent=self.FrameControlScope)
        self.buttonSingle.setGeometry(QtCore.QRect(120, 10, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.buttonSingle.setFont(font)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaPlaybackPause")
        self.buttonSingle.setIcon(icon)
        self.buttonSingle.setIconSize(QtCore.QSize(25, 25))
        self.buttonSingle.setObjectName("buttonSingle")
        self.runStopButton = QtWidgets.QPushButton(parent=self.FrameControlScope)
        self.runStopButton.setGeometry(QtCore.QRect(10, 10, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.runStopButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaPlaybackStart")
        self.runStopButton.setIcon(icon)
        self.runStopButton.setIconSize(QtCore.QSize(25, 25))
        self.runStopButton.setObjectName("runStopButton")
        self.labelMode = QtWidgets.QLabel(parent=self.FrameControlScope)
        self.labelMode.setGeometry(QtCore.QRect(250, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMode.setFont(font)
        self.labelMode.setObjectName("labelMode")
        self.comboBox = QtWidgets.QComboBox(parent=self.FrameControlScope)
        self.comboBox.setGeometry(QtCore.QRect(310, 10, 91, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.buttonAutoscale = QtWidgets.QPushButton(parent=self.FrameControlScope)
        self.buttonAutoscale.setGeometry(QtCore.QRect(250, 50, 151, 31))
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::ZoomFitBest")
        self.buttonAutoscale.setIcon(icon)
        self.buttonAutoscale.setObjectName("buttonAutoscale")
        self.comboTriggerSet = QtWidgets.QComboBox(parent=self.FrameControlScope)
        self.comboTriggerSet.setGeometry(QtCore.QRect(410, 10, 86, 26))
        self.comboTriggerSet.setObjectName("comboTriggerSet")
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::GoUp")
        self.comboTriggerSet.addItem(icon, "")
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::GoDown")
        self.comboTriggerSet.addItem(icon, "")
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaPlaylistShuffle")
        self.comboTriggerSet.addItem(icon, "")
        self.comboTriggerCH = QtWidgets.QComboBox(parent=self.FrameControlScope)
        self.comboTriggerCH.setGeometry(QtCore.QRect(410, 50, 86, 31))
        self.comboTriggerCH.setObjectName("comboTriggerCH")
        self.comboTriggerCH.addItem("")
        self.comboTriggerCH.addItem("")
        self.comboTriggerCH.addItem("")
        self.comboTriggerCH.addItem("")
        self.frameCH1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameCH1.setGeometry(QtCore.QRect(820, 110, 171, 121))
        self.frameCH1.setStyleSheet("border-color: rgb(237, 51, 59);")
        self.frameCH1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCH1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCH1.setObjectName("frameCH1")
        self.checkCH1 = QtWidgets.QCheckBox(parent=self.frameCH1)
        self.checkCH1.setGeometry(QtCore.QRect(40, 10, 88, 19))
        self.checkCH1.setStyleSheet("background-color: rgb(246, 97, 81);\n"
"color: rgb(0, 0, 0);")
        self.checkCH1.setObjectName("checkCH1")
        self.labelCH1offset = QtWidgets.QLabel(parent=self.frameCH1)
        self.labelCH1offset.setGeometry(QtCore.QRect(10, 47, 66, 21))
        self.labelCH1offset.setObjectName("labelCH1offset")
        self.labelCH1scale = QtWidgets.QLabel(parent=self.frameCH1)
        self.labelCH1scale.setGeometry(QtCore.QRect(10, 80, 66, 21))
        self.labelCH1scale.setObjectName("labelCH1scale")
        self.spinCH1offset = QtWidgets.QSpinBox(parent=self.frameCH1)
        self.spinCH1offset.setGeometry(QtCore.QRect(60, 40, 91, 27))
        self.spinCH1offset.setSpecialValueText("")
        self.spinCH1offset.setMinimum(0)
        self.spinCH1offset.setMaximum(1000)
        self.spinCH1offset.setSingleStep(5)
        self.spinCH1offset.setObjectName("spinCH1offset")
        self.spinCH1scale = QtWidgets.QSpinBox(parent=self.frameCH1)
        self.spinCH1scale.setGeometry(QtCore.QRect(60, 80, 91, 27))
        self.spinCH1scale.setSpecialValueText("")
        self.spinCH1scale.setMinimum(1)
        self.spinCH1scale.setObjectName("spinCH1scale")
        self.frameCH2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameCH2.setGeometry(QtCore.QRect(820, 240, 171, 121))
        self.frameCH2.setStyleSheet("border-color: rgb(143, 240, 164);")
        self.frameCH2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCH2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCH2.setObjectName("frameCH2")
        self.checkCH2 = QtWidgets.QCheckBox(parent=self.frameCH2)
        self.checkCH2.setGeometry(QtCore.QRect(40, 10, 91, 24))
        self.checkCH2.setStyleSheet("background-color: rgb(249, 240, 107);\n"
"color: rgb(0, 0, 0);")
        self.checkCH2.setObjectName("checkCH2")
        self.labelCH2offset = QtWidgets.QLabel(parent=self.frameCH2)
        self.labelCH2offset.setGeometry(QtCore.QRect(10, 47, 66, 21))
        self.labelCH2offset.setObjectName("labelCH2offset")
        self.labelCH2scale = QtWidgets.QLabel(parent=self.frameCH2)
        self.labelCH2scale.setGeometry(QtCore.QRect(10, 80, 66, 21))
        self.labelCH2scale.setObjectName("labelCH2scale")
        self.spinCH2offset = QtWidgets.QSpinBox(parent=self.frameCH2)
        self.spinCH2offset.setGeometry(QtCore.QRect(60, 40, 91, 27))
        self.spinCH2offset.setSpecialValueText("")
        self.spinCH2offset.setMinimum(0)
        self.spinCH2offset.setMaximum(1000)
        self.spinCH2offset.setSingleStep(5)
        self.spinCH2offset.setObjectName("spinCH2offset")
        self.spinCH2scale = QtWidgets.QSpinBox(parent=self.frameCH2)
        self.spinCH2scale.setGeometry(QtCore.QRect(60, 80, 91, 27))
        self.spinCH2scale.setSpecialValueText("")
        self.spinCH2scale.setMinimum(1)
        self.spinCH2scale.setObjectName("spinCH2scale")
        self.frameCH3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameCH3.setGeometry(QtCore.QRect(820, 370, 171, 121))
        self.frameCH3.setStyleSheet("border-color: rgb(249, 240, 107);")
        self.frameCH3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCH3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCH3.setObjectName("frameCH3")
        self.checkCH3 = QtWidgets.QCheckBox(parent=self.frameCH3)
        self.checkCH3.setGeometry(QtCore.QRect(40, 10, 91, 24))
        self.checkCH3.setStyleSheet("background-color: rgb(143, 240, 164);\n"
"color: rgb(0, 0, 0);")
        self.checkCH3.setObjectName("checkCH3")
        self.labelCH3offset = QtWidgets.QLabel(parent=self.frameCH3)
        self.labelCH3offset.setGeometry(QtCore.QRect(10, 47, 66, 21))
        self.labelCH3offset.setObjectName("labelCH3offset")
        self.labelCH3scale = QtWidgets.QLabel(parent=self.frameCH3)
        self.labelCH3scale.setGeometry(QtCore.QRect(10, 80, 66, 21))
        self.labelCH3scale.setObjectName("labelCH3scale")
        self.spinCH3offset = QtWidgets.QSpinBox(parent=self.frameCH3)
        self.spinCH3offset.setGeometry(QtCore.QRect(60, 40, 91, 27))
        self.spinCH3offset.setSpecialValueText("")
        self.spinCH3offset.setMinimum(0)
        self.spinCH3offset.setMaximum(1000)
        self.spinCH3offset.setSingleStep(5)
        self.spinCH3offset.setObjectName("spinCH3offset")
        self.spinCH3scale = QtWidgets.QSpinBox(parent=self.frameCH3)
        self.spinCH3scale.setGeometry(QtCore.QRect(60, 80, 91, 27))
        self.spinCH3scale.setSpecialValueText("")
        self.spinCH3scale.setObjectName("spinCH3scale")
        self.frameCH4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameCH4.setGeometry(QtCore.QRect(820, 500, 171, 121))
        self.frameCH4.setStyleSheet("border-color: rgb(153, 193, 241);")
        self.frameCH4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCH4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCH4.setObjectName("frameCH4")
        self.checkCH4 = QtWidgets.QCheckBox(parent=self.frameCH4)
        self.checkCH4.setGeometry(QtCore.QRect(40, 10, 91, 24))
        self.checkCH4.setStyleSheet("background-color: rgb(153, 193, 241);\n"
"color: rgb(0, 0, 0);")
        self.checkCH4.setObjectName("checkCH4")
        self.labelCH4off = QtWidgets.QLabel(parent=self.frameCH4)
        self.labelCH4off.setGeometry(QtCore.QRect(10, 47, 66, 21))
        self.labelCH4off.setObjectName("labelCH4off")
        self.labelCH4scale = QtWidgets.QLabel(parent=self.frameCH4)
        self.labelCH4scale.setGeometry(QtCore.QRect(10, 80, 66, 21))
        self.labelCH4scale.setObjectName("labelCH4scale")
        self.spinCH4offset = QtWidgets.QSpinBox(parent=self.frameCH4)
        self.spinCH4offset.setGeometry(QtCore.QRect(60, 40, 91, 27))
        self.spinCH4offset.setSpecialValueText("")
        self.spinCH4offset.setSingleStep(5)
        self.spinCH4offset.setObjectName("spinCH4offset")
        self.spinCH4scale = QtWidgets.QSpinBox(parent=self.frameCH4)
        self.spinCH4scale.setGeometry(QtCore.QRect(60, 80, 91, 27))
        self.spinCH4scale.setSpecialValueText("")
        self.spinCH4scale.setMaximum(100)
        self.spinCH4scale.setObjectName("spinCH4scale")
        self.sliderTrigger = QtWidgets.QSlider(parent=self.centralwidget)
        self.sliderTrigger.setGeometry(QtCore.QRect(5, 109, 31, 501))
        self.sliderTrigger.setStyleSheet("handle: Arrow")
        self.sliderTrigger.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.sliderTrigger.setObjectName("sliderTrigger")
        self.FrameControlWavegen = QtWidgets.QFrame(parent=self.centralwidget)
        self.FrameControlWavegen.setGeometry(QtCore.QRect(520, 0, 481, 91))
        self.FrameControlWavegen.setStyleSheet("background-color: rgb(255, 190, 111);\n"
"color: rgb(0, 0, 0);")
        self.FrameControlWavegen.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.FrameControlWavegen.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.FrameControlWavegen.setObjectName("FrameControlWavegen")
        self.labelWaveform = QtWidgets.QLabel(parent=self.FrameControlWavegen)
        self.labelWaveform.setGeometry(QtCore.QRect(20, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelWaveform.setFont(font)
        self.labelWaveform.setObjectName("labelWaveform")
        self.comboWaveform = QtWidgets.QComboBox(parent=self.FrameControlWavegen)
        self.comboWaveform.setGeometry(QtCore.QRect(110, 10, 101, 26))
        self.comboWaveform.setObjectName("comboWaveform")
        self.comboWaveform.addItem("")
        self.comboWaveform.addItem("")
        self.comboWaveform.addItem("")
        self.comboWaveform.addItem("")
        self.frame_2 = QtWidgets.QFrame(parent=self.FrameControlWavegen)
        self.frame_2.setGeometry(QtCore.QRect(500, 0, 451, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.FrameControlWavegen)
        self.label.setGeometry(QtCore.QRect(20, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinWavegenAmp = QtWidgets.QSpinBox(parent=self.FrameControlWavegen)
        self.spinWavegenAmp.setGeometry(QtCore.QRect(110, 50, 101, 27))
        self.spinWavegenAmp.setObjectName("spinWavegenAmp")
        self.spinWavegenFreq = QtWidgets.QSpinBox(parent=self.FrameControlWavegen)
        self.spinWavegenFreq.setGeometry(QtCore.QRect(320, 10, 81, 27))
        self.spinWavegenFreq.setObjectName("spinWavegenFreq")
        self.label_2 = QtWidgets.QLabel(parent=self.FrameControlWavegen)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushRunWavegen = QtWidgets.QPushButton(parent=self.FrameControlWavegen)
        self.pushRunWavegen.setGeometry(QtCore.QRect(237, 50, 161, 26))
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaSeekForward")
        self.pushRunWavegen.setIcon(icon)
        self.pushRunWavegen.setObjectName("pushRunWavegen")
        Bioscope.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=Bioscope)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1003, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave_as = QtWidgets.QMenu(parent=self.menuFile)
        self.menuSave_as.setObjectName("menuSave_as")
        Bioscope.setMenuBar(self.menuBar)
        self.actionSave = QtGui.QAction(parent=Bioscope)
        self.actionSave.setObjectName("actionSave")
        self.action_png = QtGui.QAction(parent=Bioscope)
        self.action_png.setObjectName("action_png")
        self.menuSave_as.addAction(self.action_png)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuSave_as.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Bioscope)
        QtCore.QMetaObject.connectSlotsByName(Bioscope)

    def retranslateUi(self, Bioscope):
        _translate = QtCore.QCoreApplication.translate
        Bioscope.setWindowTitle(_translate("Bioscope", "Bioscope"))
        self.buttonSingle.setText(_translate("Bioscope", "Single"))
        self.runStopButton.setText(_translate("Bioscope", "Run"))
        self.labelMode.setText(_translate("Bioscope", "Mode:"))
        self.comboBox.setItemText(0, _translate("Bioscope", "Trigger"))
        self.comboBox.setItemText(1, _translate("Bioscope", "Roll"))
        self.comboBox.setItemText(2, _translate("Bioscope", "XY"))
        self.buttonAutoscale.setText(_translate("Bioscope", "Autoscale"))
        self.comboTriggerSet.setItemText(0, _translate("Bioscope", "Rise"))
        self.comboTriggerSet.setItemText(1, _translate("Bioscope", "Fall"))
        self.comboTriggerSet.setItemText(2, _translate("Bioscope", "Both"))
        self.comboTriggerCH.setItemText(0, _translate("Bioscope", "CH1"))
        self.comboTriggerCH.setItemText(1, _translate("Bioscope", "CH2"))
        self.comboTriggerCH.setItemText(2, _translate("Bioscope", "CH3"))
        self.comboTriggerCH.setItemText(3, _translate("Bioscope", "CH4"))
        self.checkCH1.setText(_translate("Bioscope", "Channel 1"))
        self.labelCH1offset.setText(_translate("Bioscope", "Offset:"))
        self.labelCH1scale.setText(_translate("Bioscope", "Scale:"))
        self.spinCH1offset.setSuffix(_translate("Bioscope", "mV"))
        self.spinCH1scale.setSuffix(_translate("Bioscope", "mV/div"))
        self.checkCH2.setText(_translate("Bioscope", "Channel 2"))
        self.labelCH2offset.setText(_translate("Bioscope", "Offset:"))
        self.labelCH2scale.setText(_translate("Bioscope", "Scale:"))
        self.spinCH2offset.setSuffix(_translate("Bioscope", "mV"))
        self.spinCH2scale.setSuffix(_translate("Bioscope", "mV/div"))
        self.checkCH3.setText(_translate("Bioscope", "Channel 3"))
        self.labelCH3offset.setText(_translate("Bioscope", "Offset:"))
        self.labelCH3scale.setText(_translate("Bioscope", "Scale:"))
        self.spinCH3offset.setSuffix(_translate("Bioscope", "mV"))
        self.spinCH3scale.setSuffix(_translate("Bioscope", "mV/div"))
        self.checkCH4.setText(_translate("Bioscope", "Channel 4"))
        self.labelCH4off.setText(_translate("Bioscope", "Offset:"))
        self.labelCH4scale.setText(_translate("Bioscope", "Scale:"))
        self.spinCH4offset.setSuffix(_translate("Bioscope", "mV"))
        self.spinCH4scale.setSuffix(_translate("Bioscope", "mV/div"))
        self.labelWaveform.setText(_translate("Bioscope", "Waveform:"))
        self.comboWaveform.setItemText(0, _translate("Bioscope", "Triangular"))
        self.comboWaveform.setItemText(1, _translate("Bioscope", "Square"))
        self.comboWaveform.setItemText(2, _translate("Bioscope", "Sinusoid"))
        self.comboWaveform.setItemText(3, _translate("Bioscope", "DC"))
        self.label.setText(_translate("Bioscope", "Amplitude:"))
        self.spinWavegenAmp.setSuffix(_translate("Bioscope", "mV"))
        self.spinWavegenFreq.setSuffix(_translate("Bioscope", "Hz"))
        self.label_2.setText(_translate("Bioscope", "Frequency:"))
        self.pushRunWavegen.setText(_translate("Bioscope", "Run Wavegen"))
        self.menuFile.setTitle(_translate("Bioscope", "File"))
        self.menuSave_as.setTitle(_translate("Bioscope", "Save as"))
        self.actionSave.setText(_translate("Bioscope", "Save"))
        self.action_png.setText(_translate("Bioscope", ".png"))
from custom_widgets import SignalPlotter


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bioscope = QtWidgets.QMainWindow()
    ui = Ui_Bioscope()
    ui.setupUi(Bioscope)
    Bioscope.show()
    sys.exit(app.exec())
