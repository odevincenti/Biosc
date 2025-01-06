# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_template.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

from custom_widgets import (CustomScaleSpinBox, SignalPlotter)

class Ui_Bioscope(object):
    def setupUi(self, Bioscope):
        if not Bioscope.objectName():
            Bioscope.setObjectName(u"Bioscope")
        Bioscope.resize(1107, 656)
        self.actionSave = QAction(Bioscope)
        self.actionSave.setObjectName(u"actionSave")
        self.action_png = QAction(Bioscope)
        self.action_png.setObjectName(u"action_png")
        self.centralwidget = QWidget(Bioscope)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.VLayoutGlobal = QVBoxLayout()
        self.VLayoutGlobal.setObjectName(u"VLayoutGlobal")
        self.HLayoutControl = QHBoxLayout()
        self.HLayoutControl.setObjectName(u"HLayoutControl")
        self.FrameControlScope = QFrame(self.centralwidget)
        self.FrameControlScope.setObjectName(u"FrameControlScope")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrameControlScope.sizePolicy().hasHeightForWidth())
        self.FrameControlScope.setSizePolicy(sizePolicy)
        self.FrameControlScope.setMinimumSize(QSize(20, 100))
        self.FrameControlScope.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"alternate-background-color: rgb(119, 118, 123);\n"
"color: rgb(0, 0, 0);")
        self.FrameControlScope.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.FrameControlScope)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonRunStop = QPushButton(self.FrameControlScope)
        self.buttonRunStop.setObjectName(u"buttonRunStop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonRunStop.sizePolicy().hasHeightForWidth())
        self.buttonRunStop.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.buttonRunStop.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.buttonRunStop.setIcon(icon)
        self.buttonRunStop.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.buttonRunStop)

        self.buttonSingle = QPushButton(self.FrameControlScope)
        self.buttonSingle.setObjectName(u"buttonSingle")
        sizePolicy1.setHeightForWidth(self.buttonSingle.sizePolicy().hasHeightForWidth())
        self.buttonSingle.setSizePolicy(sizePolicy1)
        self.buttonSingle.setFont(font)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.buttonSingle.setIcon(icon1)
        self.buttonSingle.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.buttonSingle)

        self.VLayoutModeAuto = QVBoxLayout()
        self.VLayoutModeAuto.setObjectName(u"VLayoutModeAuto")
        self.HLayoutMode = QHBoxLayout()
        self.HLayoutMode.setObjectName(u"HLayoutMode")
        self.labelMode = QLabel(self.FrameControlScope)
        self.labelMode.setObjectName(u"labelMode")
        font1 = QFont()
        font1.setPointSize(12)
        self.labelMode.setFont(font1)

        self.HLayoutMode.addWidget(self.labelMode)

        self.comboMode = QComboBox(self.FrameControlScope)
        self.comboMode.addItem("")
        self.comboMode.addItem("")
        self.comboMode.addItem("")
        self.comboMode.setObjectName(u"comboMode")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboMode.sizePolicy().hasHeightForWidth())
        self.comboMode.setSizePolicy(sizePolicy2)
        self.comboMode.setMinimumSize(QSize(0, 10))

        self.HLayoutMode.addWidget(self.comboMode)


        self.VLayoutModeAuto.addLayout(self.HLayoutMode)

        self.buttonAutoscale = QPushButton(self.FrameControlScope)
        self.buttonAutoscale.setObjectName(u"buttonAutoscale")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonAutoscale.sizePolicy().hasHeightForWidth())
        self.buttonAutoscale.setSizePolicy(sizePolicy3)
        self.buttonAutoscale.setMinimumSize(QSize(0, 12))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ZoomFitBest))
        self.buttonAutoscale.setIcon(icon2)

        self.VLayoutModeAuto.addWidget(self.buttonAutoscale)


        self.horizontalLayout.addLayout(self.VLayoutModeAuto)

        self.VLayoutTriggerRight = QVBoxLayout()
        self.VLayoutTriggerRight.setObjectName(u"VLayoutTriggerRight")
        self.comboTriggerSet = QComboBox(self.FrameControlScope)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.comboTriggerSet.addItem(icon3, "")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.comboTriggerSet.addItem(icon4, "")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistShuffle))
        self.comboTriggerSet.addItem(icon5, "")
        self.comboTriggerSet.setObjectName(u"comboTriggerSet")
        sizePolicy2.setHeightForWidth(self.comboTriggerSet.sizePolicy().hasHeightForWidth())
        self.comboTriggerSet.setSizePolicy(sizePolicy2)
        self.comboTriggerSet.setMinimumSize(QSize(0, 10))

        self.VLayoutTriggerRight.addWidget(self.comboTriggerSet)

        self.comboTriggerCH = QComboBox(self.FrameControlScope)
        self.comboTriggerCH.addItem("")
        self.comboTriggerCH.addItem("")
        self.comboTriggerCH.addItem("")
        self.comboTriggerCH.addItem("")
        self.comboTriggerCH.setObjectName(u"comboTriggerCH")
        sizePolicy2.setHeightForWidth(self.comboTriggerCH.sizePolicy().hasHeightForWidth())
        self.comboTriggerCH.setSizePolicy(sizePolicy2)
        self.comboTriggerCH.setMinimumSize(QSize(0, 10))

        self.VLayoutTriggerRight.addWidget(self.comboTriggerCH)


        self.horizontalLayout.addLayout(self.VLayoutTriggerRight)


        self.HLayoutControl.addWidget(self.FrameControlScope)

        self.FrameControlWavegen = QFrame(self.centralwidget)
        self.FrameControlWavegen.setObjectName(u"FrameControlWavegen")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.FrameControlWavegen.sizePolicy().hasHeightForWidth())
        self.FrameControlWavegen.setSizePolicy(sizePolicy4)
        self.FrameControlWavegen.setMinimumSize(QSize(0, 100))
        self.FrameControlWavegen.setStyleSheet(u"background-color: rgb(255, 190, 111);\n"
"color: rgb(0, 0, 0);")
        self.FrameControlWavegen.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.FrameControlWavegen)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.VLayoutWavAmp = QVBoxLayout()
        self.VLayoutWavAmp.setObjectName(u"VLayoutWavAmp")
        self.HLayoutWaveform = QHBoxLayout()
        self.HLayoutWaveform.setObjectName(u"HLayoutWaveform")
        self.labelWaveform = QLabel(self.FrameControlWavegen)
        self.labelWaveform.setObjectName(u"labelWaveform")
        self.labelWaveform.setFont(font1)

        self.HLayoutWaveform.addWidget(self.labelWaveform)

        self.comboWaveform = QComboBox(self.FrameControlWavegen)
        self.comboWaveform.addItem("")
        self.comboWaveform.addItem("")
        self.comboWaveform.addItem("")
        self.comboWaveform.addItem("")
        self.comboWaveform.setObjectName(u"comboWaveform")

        self.HLayoutWaveform.addWidget(self.comboWaveform)


        self.VLayoutWavAmp.addLayout(self.HLayoutWaveform)

        self.HLayoutAmplitud = QHBoxLayout()
        self.HLayoutAmplitud.setObjectName(u"HLayoutAmplitud")
        self.labelAmplitude = QLabel(self.FrameControlWavegen)
        self.labelAmplitude.setObjectName(u"labelAmplitude")
        self.labelAmplitude.setFont(font1)

        self.HLayoutAmplitud.addWidget(self.labelAmplitude)

        self.spinWavegenAmp = QSpinBox(self.FrameControlWavegen)
        self.spinWavegenAmp.setObjectName(u"spinWavegenAmp")

        self.HLayoutAmplitud.addWidget(self.spinWavegenAmp)


        self.VLayoutWavAmp.addLayout(self.HLayoutAmplitud)


        self.horizontalLayout_2.addLayout(self.VLayoutWavAmp)

        self.VLayoutFreqRunWav = QVBoxLayout()
        self.VLayoutFreqRunWav.setObjectName(u"VLayoutFreqRunWav")
        self.HLayoutFreq = QHBoxLayout()
        self.HLayoutFreq.setObjectName(u"HLayoutFreq")
        self.labelFrequency = QLabel(self.FrameControlWavegen)
        self.labelFrequency.setObjectName(u"labelFrequency")
        self.labelFrequency.setFont(font1)

        self.HLayoutFreq.addWidget(self.labelFrequency)

        self.spinWavegenFreq = QSpinBox(self.FrameControlWavegen)
        self.spinWavegenFreq.setObjectName(u"spinWavegenFreq")

        self.HLayoutFreq.addWidget(self.spinWavegenFreq)


        self.VLayoutFreqRunWav.addLayout(self.HLayoutFreq)

        self.pushRunWavegen = QPushButton(self.FrameControlWavegen)
        self.pushRunWavegen.setObjectName(u"pushRunWavegen")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.pushRunWavegen.setIcon(icon6)

        self.VLayoutFreqRunWav.addWidget(self.pushRunWavegen)


        self.horizontalLayout_2.addLayout(self.VLayoutFreqRunWav)


        self.HLayoutControl.addWidget(self.FrameControlWavegen)


        self.VLayoutGlobal.addLayout(self.HLayoutControl)

        self.HLayoutPlotCH = QHBoxLayout()
        self.HLayoutPlotCH.setObjectName(u"HLayoutPlotCH")
        self.plotWidget = SignalPlotter(self.centralwidget)
        self.plotWidget.setObjectName(u"plotWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy5)

        self.HLayoutPlotCH.addWidget(self.plotWidget)

        self.CHVLayout = QVBoxLayout()
        self.CHVLayout.setObjectName(u"CHVLayout")
        self.CHVLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.frameCH1 = QFrame(self.centralwidget)
        self.frameCH1.setObjectName(u"frameCH1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frameCH1.sizePolicy().hasHeightForWidth())
        self.frameCH1.setSizePolicy(sizePolicy6)
        self.frameCH1.setMinimumSize(QSize(200, 0))
        self.frameCH1.setStyleSheet(u"border-color: rgb(237, 51, 59);")
        self.frameCH1.setFrameShape(QFrame.Shape.NoFrame)
        self.formLayout_3 = QFormLayout(self.frameCH1)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.checkCH1 = QCheckBox(self.frameCH1)
        self.checkCH1.setObjectName(u"checkCH1")
        self.checkCH1.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
"color: rgb(0, 0, 0);")

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.checkCH1)

        self.labelCH1offset = QLabel(self.frameCH1)
        self.labelCH1offset.setObjectName(u"labelCH1offset")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.labelCH1offset)

        self.spinCH1offset = QSpinBox(self.frameCH1)
        self.spinCH1offset.setObjectName(u"spinCH1offset")
        self.spinCH1offset.setMinimum(-1000)
        self.spinCH1offset.setMaximum(1000)
        self.spinCH1offset.setSingleStep(5)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinCH1offset)

        self.labelCH1scale = QLabel(self.frameCH1)
        self.labelCH1scale.setObjectName(u"labelCH1scale")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.labelCH1scale)

        self.spinScaleCH1 = CustomScaleSpinBox(self.frameCH1)
        self.spinScaleCH1.setObjectName(u"spinScaleCH1")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinScaleCH1)


        self.CHVLayout.addWidget(self.frameCH1)

        self.frameCH2 = QFrame(self.centralwidget)
        self.frameCH2.setObjectName(u"frameCH2")
        sizePolicy6.setHeightForWidth(self.frameCH2.sizePolicy().hasHeightForWidth())
        self.frameCH2.setSizePolicy(sizePolicy6)
        self.frameCH2.setMinimumSize(QSize(200, 0))
        self.frameCH2.setStyleSheet(u"border-color: rgb(143, 240, 164);")
        self.frameCH2.setFrameShape(QFrame.Shape.NoFrame)
        self.formLayout_2 = QFormLayout(self.frameCH2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.checkCH2 = QCheckBox(self.frameCH2)
        self.checkCH2.setObjectName(u"checkCH2")
        self.checkCH2.setStyleSheet(u"background-color: rgb(249, 240, 107);\n"
"color: rgb(0, 0, 0);")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.checkCH2)

        self.labelCH2offset = QLabel(self.frameCH2)
        self.labelCH2offset.setObjectName(u"labelCH2offset")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.labelCH2offset)

        self.spinCH2offset = QSpinBox(self.frameCH2)
        self.spinCH2offset.setObjectName(u"spinCH2offset")
        self.spinCH2offset.setMinimum(-1000)
        self.spinCH2offset.setMaximum(1000)
        self.spinCH2offset.setSingleStep(5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.spinCH2offset)

        self.labelCH2scale = QLabel(self.frameCH2)
        self.labelCH2scale.setObjectName(u"labelCH2scale")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.labelCH2scale)

        self.spinScaleCH2 = CustomScaleSpinBox(self.frameCH2)
        self.spinScaleCH2.setObjectName(u"spinScaleCH2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spinScaleCH2)


        self.CHVLayout.addWidget(self.frameCH2)

        self.frameCH3 = QFrame(self.centralwidget)
        self.frameCH3.setObjectName(u"frameCH3")
        sizePolicy6.setHeightForWidth(self.frameCH3.sizePolicy().hasHeightForWidth())
        self.frameCH3.setSizePolicy(sizePolicy6)
        self.frameCH3.setMinimumSize(QSize(200, 0))
        self.frameCH3.setStyleSheet(u"border-color: rgb(249, 240, 107);")
        self.frameCH3.setFrameShape(QFrame.Shape.NoFrame)
        self.formLayout = QFormLayout(self.frameCH3)
        self.formLayout.setObjectName(u"formLayout")
        self.checkCH3 = QCheckBox(self.frameCH3)
        self.checkCH3.setObjectName(u"checkCH3")
        self.checkCH3.setStyleSheet(u"background-color: rgb(143, 240, 164);\n"
"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.checkCH3)

        self.labelCH3offset = QLabel(self.frameCH3)
        self.labelCH3offset.setObjectName(u"labelCH3offset")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelCH3offset)

        self.spinCH3offset = QSpinBox(self.frameCH3)
        self.spinCH3offset.setObjectName(u"spinCH3offset")
        self.spinCH3offset.setMinimum(-1000)
        self.spinCH3offset.setMaximum(1000)
        self.spinCH3offset.setSingleStep(5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinCH3offset)

        self.labelCH3scale = QLabel(self.frameCH3)
        self.labelCH3scale.setObjectName(u"labelCH3scale")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelCH3scale)

        self.spinScaleCH3 = CustomScaleSpinBox(self.frameCH3)
        self.spinScaleCH3.setObjectName(u"spinScaleCH3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinScaleCH3)


        self.CHVLayout.addWidget(self.frameCH3)

        self.frameCH4 = QFrame(self.centralwidget)
        self.frameCH4.setObjectName(u"frameCH4")
        sizePolicy6.setHeightForWidth(self.frameCH4.sizePolicy().hasHeightForWidth())
        self.frameCH4.setSizePolicy(sizePolicy6)
        self.frameCH4.setMinimumSize(QSize(200, 0))
        self.frameCH4.setStyleSheet(u"border-color: rgb(153, 193, 241);")
        self.frameCH4.setFrameShape(QFrame.Shape.NoFrame)
        self.formLayout_4 = QFormLayout(self.frameCH4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.checkCH4 = QCheckBox(self.frameCH4)
        self.checkCH4.setObjectName(u"checkCH4")
        self.checkCH4.setStyleSheet(u"background-color: rgb(153, 193, 241);\n"
"color: rgb(0, 0, 0);")

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.checkCH4)

        self.labelCH4off = QLabel(self.frameCH4)
        self.labelCH4off.setObjectName(u"labelCH4off")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.labelCH4off)

        self.spinCH4offset = QSpinBox(self.frameCH4)
        self.spinCH4offset.setObjectName(u"spinCH4offset")
        self.spinCH4offset.setMinimum(-1000)
        self.spinCH4offset.setMaximum(1000)
        self.spinCH4offset.setSingleStep(5)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.spinCH4offset)

        self.labelCH4scale = QLabel(self.frameCH4)
        self.labelCH4scale.setObjectName(u"labelCH4scale")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.labelCH4scale)

        self.spinScaleCH4 = CustomScaleSpinBox(self.frameCH4)
        self.spinScaleCH4.setObjectName(u"spinScaleCH4")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.spinScaleCH4)


        self.CHVLayout.addWidget(self.frameCH4)


        self.HLayoutPlotCH.addLayout(self.CHVLayout)


        self.VLayoutGlobal.addLayout(self.HLayoutPlotCH)


        self.verticalLayout_3.addLayout(self.VLayoutGlobal)

        Bioscope.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Bioscope)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1107, 23))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSave_as = QMenu(self.menuFile)
        self.menuSave_as.setObjectName(u"menuSave_as")
        Bioscope.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuSave_as.menuAction())
        self.menuSave_as.addAction(self.action_png)

        self.retranslateUi(Bioscope)

        QMetaObject.connectSlotsByName(Bioscope)
    # setupUi

    def retranslateUi(self, Bioscope):
        Bioscope.setWindowTitle(QCoreApplication.translate("Bioscope", u"Bioscope", None))
        self.actionSave.setText(QCoreApplication.translate("Bioscope", u"Save", None))
        self.action_png.setText(QCoreApplication.translate("Bioscope", u".png", None))
        self.buttonRunStop.setText(QCoreApplication.translate("Bioscope", u"Run", None))
        self.buttonSingle.setText(QCoreApplication.translate("Bioscope", u"Single", None))
        self.labelMode.setText(QCoreApplication.translate("Bioscope", u"Mode:", None))
        self.comboMode.setItemText(0, QCoreApplication.translate("Bioscope", u"Trigger", None))
        self.comboMode.setItemText(1, QCoreApplication.translate("Bioscope", u"Roll", None))
        self.comboMode.setItemText(2, QCoreApplication.translate("Bioscope", u"XY", None))

        self.buttonAutoscale.setText(QCoreApplication.translate("Bioscope", u"Autoscale", None))
        self.comboTriggerSet.setItemText(0, QCoreApplication.translate("Bioscope", u"Rise", None))
        self.comboTriggerSet.setItemText(1, QCoreApplication.translate("Bioscope", u"Fall", None))
        self.comboTriggerSet.setItemText(2, QCoreApplication.translate("Bioscope", u"Both", None))

        self.comboTriggerCH.setItemText(0, QCoreApplication.translate("Bioscope", u"CH1", None))
        self.comboTriggerCH.setItemText(1, QCoreApplication.translate("Bioscope", u"CH2", None))
        self.comboTriggerCH.setItemText(2, QCoreApplication.translate("Bioscope", u"CH3", None))
        self.comboTriggerCH.setItemText(3, QCoreApplication.translate("Bioscope", u"CH4", None))

        self.labelWaveform.setText(QCoreApplication.translate("Bioscope", u"Waveform:", None))
        self.comboWaveform.setItemText(0, QCoreApplication.translate("Bioscope", u"Triangular", None))
        self.comboWaveform.setItemText(1, QCoreApplication.translate("Bioscope", u"Square", None))
        self.comboWaveform.setItemText(2, QCoreApplication.translate("Bioscope", u"Sinusoid", None))
        self.comboWaveform.setItemText(3, QCoreApplication.translate("Bioscope", u"DC", None))

        self.labelAmplitude.setText(QCoreApplication.translate("Bioscope", u"Amplitude:", None))
        self.spinWavegenAmp.setSuffix(QCoreApplication.translate("Bioscope", u"mV", None))
        self.labelFrequency.setText(QCoreApplication.translate("Bioscope", u"Frequency:", None))
        self.spinWavegenFreq.setSuffix(QCoreApplication.translate("Bioscope", u"Hz", None))
        self.pushRunWavegen.setText(QCoreApplication.translate("Bioscope", u"Run Wavegen", None))
        self.checkCH1.setText(QCoreApplication.translate("Bioscope", u"Channel 1", None))
        self.labelCH1offset.setText(QCoreApplication.translate("Bioscope", u"Offset:", None))
        self.spinCH1offset.setSpecialValueText("")
        self.spinCH1offset.setSuffix(QCoreApplication.translate("Bioscope", u"mV", None))
        self.labelCH1scale.setText(QCoreApplication.translate("Bioscope", u"Scale:", None))
        self.checkCH2.setText(QCoreApplication.translate("Bioscope", u"Channel 2", None))
        self.labelCH2offset.setText(QCoreApplication.translate("Bioscope", u"Offset:", None))
        self.spinCH2offset.setSpecialValueText("")
        self.spinCH2offset.setSuffix(QCoreApplication.translate("Bioscope", u"mV", None))
        self.labelCH2scale.setText(QCoreApplication.translate("Bioscope", u"Scale:", None))
        self.checkCH3.setText(QCoreApplication.translate("Bioscope", u"Channel 3", None))
        self.labelCH3offset.setText(QCoreApplication.translate("Bioscope", u"Offset:", None))
        self.spinCH3offset.setSpecialValueText("")
        self.spinCH3offset.setSuffix(QCoreApplication.translate("Bioscope", u"mV", None))
        self.labelCH3scale.setText(QCoreApplication.translate("Bioscope", u"Scale:", None))
        self.checkCH4.setText(QCoreApplication.translate("Bioscope", u"Wavegen", None))
        self.labelCH4off.setText(QCoreApplication.translate("Bioscope", u"Offset:", None))
        self.spinCH4offset.setSpecialValueText("")
        self.spinCH4offset.setSuffix(QCoreApplication.translate("Bioscope", u"mV", None))
        self.labelCH4scale.setText(QCoreApplication.translate("Bioscope", u"Scale:", None))
        self.menuFile.setTitle(QCoreApplication.translate("Bioscope", u"File", None))
        self.menuSave_as.setTitle(QCoreApplication.translate("Bioscope", u"Save as", None))
    # retranslateUi

