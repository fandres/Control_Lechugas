# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created: Sat Nov 15 23:32:06 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(700, 350)
        self.calendarWidget = QtGui.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(420, 200, 272, 143))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.dockWidget = QtGui.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(10, 40, 201, 301))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.ui_Display_tempS = QtGui.QLCDNumber(self.dockWidgetContents)
        self.ui_Display_tempS.setGeometry(QtCore.QRect(30, 60, 64, 23))
        self.ui_Display_tempS.setObjectName(_fromUtf8("ui_Display_tempS"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(110, 40, 57, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.ui_termoTempS = QwtThermo(self.dockWidgetContents)
        self.ui_termoTempS.setGeometry(QtCore.QRect(20, 90, 71, 181))
        self.ui_termoTempS.setMaxValue(60.0)
        self.ui_termoTempS.setObjectName(_fromUtf8("ui_termoTempS"))
        self.ui_termoTempA = QwtThermo(self.dockWidgetContents)
        self.ui_termoTempA.setGeometry(QtCore.QRect(90, 90, 71, 181))
        self.ui_termoTempA.setMaxValue(60.0)
        self.ui_termoTempA.setObjectName(_fromUtf8("ui_termoTempA"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 57, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ui_Display_tempA = QtGui.QLCDNumber(self.dockWidgetContents)
        self.ui_Display_tempA.setGeometry(QtCore.QRect(100, 60, 64, 23))
        self.ui_Display_tempA.setObjectName(_fromUtf8("ui_Display_tempA"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.dockWidget_2 = QtGui.QDockWidget(Form)
        self.dockWidget_2.setGeometry(QtCore.QRect(210, 40, 201, 301))
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.ui_Display_huS = QtGui.QLCDNumber(self.dockWidgetContents_2)
        self.ui_Display_huS.setGeometry(QtCore.QRect(30, 60, 64, 23))
        self.ui_Display_huS.setObjectName(_fromUtf8("ui_Display_huS"))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(110, 40, 57, 14))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ui_termoHuS = QwtThermo(self.dockWidgetContents_2)
        self.ui_termoHuS.setGeometry(QtCore.QRect(20, 90, 71, 181))
        self.ui_termoHuS.setMaxValue(100.0)
        self.ui_termoHuS.setObjectName(_fromUtf8("ui_termoHuS"))
        self.ui_termoHuA = QwtThermo(self.dockWidgetContents_2)
        self.ui_termoHuA.setGeometry(QtCore.QRect(90, 90, 71, 181))
        self.ui_termoHuA.setMaxValue(100.0)
        self.ui_termoHuA.setPipeWidth(5)
        self.ui_termoHuA.setObjectName(_fromUtf8("ui_termoHuA"))
        self.label_6 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 57, 14))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.ui_Display_huA = QtGui.QLCDNumber(self.dockWidgetContents_2)
        self.ui_Display_huA.setGeometry(QtCore.QRect(100, 60, 64, 23))
        self.ui_Display_huA.setObjectName(_fromUtf8("ui_Display_huA"))
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 681, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(420, 170, 271, 31))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.ui_label = QtGui.QLabel(self.frame)
        self.ui_label.setGeometry(QtCore.QRect(10, 0, 151, 22))
        self.ui_label.setObjectName(_fromUtf8("ui_label"))
        self.ui_nivelTanque = QtGui.QLineEdit(self.frame)
        self.ui_nivelTanque.setEnabled(False)
        self.ui_nivelTanque.setGeometry(QtCore.QRect(158, 0, 91, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_nivelTanque.sizePolicy().hasHeightForWidth())
        self.ui_nivelTanque.setSizePolicy(sizePolicy)
        self.ui_nivelTanque.setObjectName(_fromUtf8("ui_nivelTanque"))
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(420, 40, 271, 131))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(70, 10, 141, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Control [Temperatura - Humedad]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Temperatura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Aire", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Suelo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Humedad", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Aire", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Suelo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Control Temperatura Humedad en Cultivos</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_label.setText(QtGui.QApplication.translate("Form", "Nivel Llenado tanque:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Predicción del tiempo ", None, QtGui.QApplication.UnicodeUTF8))

#from qwt_thermo import QwtThermo
from PyQt4.Qwt5.Qwt import QwtThermo