
# -*- coding: utf-8 -*-
#
# Dang Huu Tuan Phong - 21151476 (LonerP)
#
#

import time
import serial.tools.list_ports
import threading
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1084, 602)
        MainWindow.setMinimumSize(QtCore.QSize(1084, 602))
        MainWindow.setMaximumSize(QtCore.QSize(1084, 602))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStatusTip("")
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(49, 51, 56);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(10, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Terminal = QtWidgets.QGroupBox(self.centralwidget)
        self.Terminal.setGeometry(QtCore.QRect(10, 10, 321, 191))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Terminal.setFont(font)
        self.Terminal.setStyleSheet("QGroupBox {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(58, 61, 67);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Terminal.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Terminal.setObjectName("Terminal")
        self.Bdbox = QtWidgets.QComboBox(self.Terminal)
        self.Bdbox.setGeometry(QtCore.QRect(10, 50, 101, 22))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Bdbox.setFont(font)
        self.Bdbox.setStyleSheet("QComboBox {\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 31, 34);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.Bdbox.setObjectName("Bdbox")
        self.Bdbox.addItem("")
        self.Bdbox.addItem("")
        self.Bdbox.addItem("")
        self.Bdbox.addItem("")
        self.Bdbox.addItem("")
        self.Bdbox.addItem("")
        self.Bdbox.addItem("")
        self.Bdbox.addItem("")
        self.Baudrate = QtWidgets.QLabel(self.Terminal)
        self.Baudrate.setGeometry(QtCore.QRect(10, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Baudrate.setFont(font)
        self.Baudrate.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.Baudrate.setObjectName("Baudrate")
        self.Port = QtWidgets.QLabel(self.Terminal)
        self.Port.setGeometry(QtCore.QRect(10, 80, 55, 16))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Port.setFont(font)
        self.Port.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.Port.setObjectName("Port")
        self.Portbox = QtWidgets.QComboBox(self.Terminal)
        self.Portbox.setGeometry(QtCore.QRect(10, 100, 101, 22))
        self.Portbox.setStyleSheet("QComboBox {\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 31, 34);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}\n"
"")
        self.Portbox.setObjectName("Portbox")
        self.Connect = QtWidgets.QPushButton(self.Terminal)
        self.Connect.setGeometry(QtCore.QRect(210, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Connect.setFont(font)
        self.Connect.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.Connect.setObjectName("Connect")
        self.Disconnect = QtWidgets.QPushButton(self.Terminal)
        self.Disconnect.setGeometry(QtCore.QRect(210, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Disconnect.setFont(font)
        self.Disconnect.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.Disconnect.setObjectName("Disconnect")
        self.Scan = QtWidgets.QPushButton(self.Terminal)
        self.Scan.setGeometry(QtCore.QRect(210, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Scan.setFont(font)
        self.Scan.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.Scan.setObjectName("Scan")
        self.label1 = QtWidgets.QLabel(self.Terminal)
        self.label1.setGeometry(QtCore.QRect(10, 130, 191, 16))
        self.label1.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.label1.setObjectName("label1")
        self.status = QtWidgets.QLabel(self.Terminal)
        self.status.setGeometry(QtCore.QRect(10, 155, 301, 21))
        self.status.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.status.setText("")
        self.status.setObjectName("status")
        self.PID = QtWidgets.QGroupBox(self.centralwidget)
        self.PID.setGeometry(QtCore.QRect(10, 210, 321, 231))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.PID.setFont(font)
        self.PID.setStyleSheet("QGroupBox {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(58, 61, 67);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.PID.setObjectName("PID")
        self.Kpline = QtWidgets.QLineEdit(self.PID)
        self.Kpline.setGeometry(QtCore.QRect(60, 50, 111, 22))
        self.Kpline.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kpline.setObjectName("Kpline")
        self.Kpline.setAlignment(Qt.AlignCenter)
        self.Kpline.setPlaceholderText("0")
        self.Kiline = QtWidgets.QLineEdit(self.PID)
        self.Kiline.setGeometry(QtCore.QRect(60, 90, 111, 22))
        self.Kiline.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kiline.setObjectName("Kiline")
        self.Kiline.setAlignment(Qt.AlignCenter)
        self.Kiline.setPlaceholderText("0")
        self.Kdline = QtWidgets.QLineEdit(self.PID)
        self.Kdline.setGeometry(QtCore.QRect(60, 130, 111, 22))
        self.Kdline.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kdline.setObjectName("Kdline")
        self.Kdline.setPlaceholderText("0")
        self.Kdline.setAlignment(Qt.AlignCenter)
        self.Kp = QtWidgets.QLabel(self.PID)
        self.Kp.setGeometry(QtCore.QRect(20, 50, 55, 21))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Kp.setFont(font)
        self.Kp.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kp.setObjectName("Kp")
        self.Ki = QtWidgets.QLabel(self.PID)
        self.Ki.setGeometry(QtCore.QRect(20, 90, 55, 16))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Ki.setFont(font)
        self.Ki.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.Ki.setObjectName("Ki")
        self.Kd = QtWidgets.QLabel(self.PID)
        self.Kd.setGeometry(QtCore.QRect(20, 130, 55, 16))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Kd.setFont(font)
        self.Kd.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kd.setObjectName("Kd")
        self.label = QtWidgets.QLabel(self.PID)
        self.label.setGeometry(QtCore.QRect(240, 20, 71, 16))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}")
        self.label.setObjectName("label")
        self.Kpline_2 = QtWidgets.QLineEdit(self.PID)
        self.Kpline_2.setGeometry(QtCore.QRect(240, 50, 61, 22))
        self.Kpline_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kpline_2.setObjectName("Kpline_2")
        self.Kpline_2.setAlignment(Qt.AlignCenter)
        self.Kpline_2.setReadOnly(True)
        self.Kiline_2 = QtWidgets.QLineEdit(self.PID)
        self.Kiline_2.setGeometry(QtCore.QRect(240, 90, 61, 22))
        self.Kiline_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kiline_2.setObjectName("Kiline_2")
        self.Kiline_2.setAlignment(Qt.AlignCenter)
        self.Kiline_2.setReadOnly(True)
        self.Kdline_2 = QtWidgets.QLineEdit(self.PID)
        self.Kdline_2.setGeometry(QtCore.QRect(240, 130, 61, 22))
        self.Kdline_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Kdline_2.setObjectName("Kdline_2")
        self.Kdline_2.setAlignment(Qt.AlignCenter)
        self.Kdline_2.setReadOnly(True)
        self.Send = QtWidgets.QPushButton(self.PID)
        self.Send.setGeometry(QtCore.QRect(20, 170, 281, 41))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Send.setFont(font)
        self.Send.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.Send.setObjectName("Send")
        self.Controller = QtWidgets.QGroupBox(self.centralwidget)
        self.Controller.setGeometry(QtCore.QRect(10, 450, 321, 141))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Controller.setFont(font)
        self.Controller.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Controller.setStyleSheet("QGroupBox {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(58, 61, 67);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.Controller.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Controller.setFlat(False)
        self.Controller.setCheckable(False)
        self.Controller.setObjectName("Controller")
        self.LEFT = QtWidgets.QPushButton(self.Controller)
        self.LEFT.setGeometry(QtCore.QRect(40, 50, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.LEFT.setFont(font)
        self.LEFT.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEFT.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.LEFT.setObjectName("LEFT")
        self.BACKWARD = QtWidgets.QPushButton(self.Controller)
        self.BACKWARD.setGeometry(QtCore.QRect(100, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BACKWARD.setFont(font)
        self.BACKWARD.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BACKWARD.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.BACKWARD.setObjectName("BACKWARD")
        self.RIGHT = QtWidgets.QPushButton(self.Controller)
        self.RIGHT.setGeometry(QtCore.QRect(160, 50, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.RIGHT.setFont(font)
        self.RIGHT.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.RIGHT.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.RIGHT.setObjectName("RIGHT")
        self.FORWARD = QtWidgets.QPushButton(self.Controller)
        self.FORWARD.setGeometry(QtCore.QRect(100, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.FORWARD.setFont(font)
        self.FORWARD.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FORWARD.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(88, 101, 242);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(71, 82, 196);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.FORWARD.setObjectName("FORWARD")
        self.STOP = QtWidgets.QPushButton(self.Controller)
        self.STOP.setGeometry(QtCore.QRect(230, 40, 71, 71))
        self.STOP.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(218, 55, 60);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 63 10pt \"gg sans SemiBold\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(177, 44, 46);\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.STOP.setObjectName("STOP")
#         self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
#         self.groupBox.setGeometry(QtCore.QRect(10, 600, 1061, 231))
#         font = QtGui.QFont()
#         font.setFamily("gg sans SemiBold")
#         font.setPointSize(10)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(50)
#         self.groupBox.setFont(font)
#         self.groupBox.setStyleSheet("QGroupBox {\n"
# "    border-radius: 5px;\n"
# "    background-color: rgb(58, 61, 67);\n"
# "    color:rgb(255, 255, 255);\n"
# "    font: 10pt \"gg sans SemiBold\";\n"
# "}")
#         self.groupBox.setObjectName("groupBox")
#         self.message = QtWidgets.QLineEdit(self.groupBox)
#         self.message.setGeometry(QtCore.QRect(10, 30, 861, 31))
#         self.message.setMinimumSize(QtCore.QSize(0, 31))
#         self.message.setMaximumSize(QtCore.QSize(1041, 31))
#         self.message.setStyleSheet("QLineEdit {\n"                            
# "    border-radius: 5px;\n"
# "    font: 63 8pt \"gg sans Medium\";\n"
# "}")
#         self.message.setObjectName("message")
#         self.SerialMonitor = QtWidgets.QPlainTextEdit(self.groupBox)
#         self.SerialMonitor.setGeometry(QtCore.QRect(10, 70, 1041, 151))
#         self.SerialMonitor.setMinimumSize(QtCore.QSize(1041, 151))
#         self.SerialMonitor.setMaximumSize(QtCore.QSize(1041, 151))
#         self.SerialMonitor.setStyleSheet("QPlainTextEdit {\n"
# "    border-radius: 5px;\n"
# "    background-color: rgb(255, 255, 255);\n"
# "}")
#         self.SerialMonitor.setObjectName("SerialMonitor")
#         self.SerialMonitor.setReadOnly(True)
#         self.Clear = QtWidgets.QPushButton(self.groupBox)
#         self.Clear.setGeometry(QtCore.QRect(880, 30, 171, 31))
#         self.Clear.setStyleSheet("QPushButton {\n"
# "    border-radius: 5px;\n"
# "    background-color: rgb(88, 101, 242);\n"
# "    color:rgb(255, 255, 255);\n"
# "    font: 63 10pt \"gg sans SemiBold\";\n"
# "}\n"
# "QPushButton:hover {\n"
# "    border-radius: 5px;\n"
# "    background-color: rgb(71, 82, 196);\n"
# "    color:rgb(255, 255, 255);\n"
# "}")
#         self.Clear.setObjectName("Clear")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 0, 751, 601))
        self.widget.setMinimumSize(QtCore.QSize(751, 601))
        self.widget.setMaximumSize(QtCore.QSize(751, 601))
        self.widget.setObjectName("widget")
        #create vertical layout
        self.widget_layout = QVBoxLayout(self.widget)
        self.widget_layout.setObjectName("widget_layout")
        #canvas
        self.fig = plt.figure(facecolor="#3a3d43")
        self.canvas = FigureCanvas(self.fig)
        plt.style.use("dark_background")
        #add canvas
        self.widget_layout.addWidget(self.canvas)
        self.Data = QtWidgets.QPlainTextEdit(self.widget)
        self.Data.setGeometry(QtCore.QRect(557, 37, 120, 41))
        self.Data.setStyleSheet("QPlainTextEdit {\n"
"    padding-left: 20px;\n"    
"    border-radius: 5px;\n"
"    color: white;\n"
"    background-color: rgb(58, 61, 67);\n"
"}")
        self.Data.setObjectName("Data")
        self.Data.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.status_label = self.status  # QLabel trong UI
        self.serial_connection = None
        self.receive_thread = None
        self.is_connected = False  # Biến cờ kiểm tra kết nối

        self.Scan.clicked.connect(self.scan_ports)
        self.Connect.clicked.connect(self.connect_port)
        self.Disconnect.clicked.connect(self.disconnect_port)
        self.Send.clicked.connect(self.send_parameters)
        # self.Clear.clicked.connect(self.clear_output)
        # self.message.returnPressed.connect(self.send_command)
        self.FORWARD.clicked.connect(self.go_forward)
        self.BACKWARD.clicked.connect(self.go_backward)
        self.LEFT.clicked.connect(self.turn_left)
        self.RIGHT.clicked.connect(self.turn_right)
        self.STOP.clicked.connect(self.stop_move)
        
        #figure
        self.time=[]
        self.angle=[]
        self.ax = self.fig.subplots(1, 1)  
        self.ax.set_title("Giá trị góc nghiêng")
        self.ax.set_ylabel("Theta (degree)")
        self.ax.set_xlabel("Time (s)")

        self._line, = self.ax.plot(self.time, self.angle, 'cyan')
        self._timer = self.canvas.new_timer(10)
        self._timer.add_callback(self.update_plot)
        self._timer.start(10)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arduino SBRobot"))
        MainWindow.setWindowIcon(QtGui.QIcon(":/icon/3.png"))
        self.Terminal.setTitle(_translate("MainWindow", "Terminal"))
        self.Bdbox.setItemText(0, _translate("MainWindow", "200"))
        self.Bdbox.setItemText(1, _translate("MainWindow", "2400"))
        self.Bdbox.setItemText(2, _translate("MainWindow", "4800"))
        self.Bdbox.setItemText(3, _translate("MainWindow", "9600"))
        self.Bdbox.setItemText(4, _translate("MainWindow", "19200"))
        self.Bdbox.setItemText(5, _translate("MainWindow", "38400"))
        self.Bdbox.setItemText(6, _translate("MainWindow", "57600"))
        self.Bdbox.setItemText(7, _translate("MainWindow", "115200"))
        self.Bdbox.setCurrentIndex(3)
        self.Baudrate.setText(_translate("MainWindow", "Baudrate"))
        self.Port.setText(_translate("MainWindow", "Port"))
        self.Connect.setText(_translate("MainWindow", "Connect"))
        self.Disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.Scan.setText(_translate("MainWindow", "Scan"))
        self.label1.setText(_translate("MainWindow", "Status:"))
        self.PID.setTitle(_translate("MainWindow", "PID "))
        self.Kp.setText(_translate("MainWindow", "Kp"))
        self.Ki.setText(_translate("MainWindow", "Ki"))
        self.Kd.setText(_translate("MainWindow", "Kd"))
        self.label.setText(_translate("MainWindow", "Current"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.Controller.setTitle(_translate("MainWindow", "Controller"))
        self.LEFT.setText(_translate("MainWindow", "◀"))
        self.LEFT.setShortcut(_translate("MainWindow", "Left"))
        self.BACKWARD.setText(_translate("MainWindow", "▼"))
        self.BACKWARD.setShortcut(_translate("MainWindow", "Down"))
        self.RIGHT.setText(_translate("MainWindow", "▶"))
        self.RIGHT.setShortcut(_translate("MainWindow", "Right"))
        self.FORWARD.setText(_translate("MainWindow", "▲"))
        self.FORWARD.setShortcut(_translate("MainWindow", "Up"))
        self.STOP.setText(_translate("MainWindow", "STOP"))
        self.STOP.setShortcut(_translate("MainWindow", "Space"))
        # self.groupBox.setTitle(_translate("MainWindow", "Command"))
        # self.message.setPlaceholderText(_translate("MainWindow", "Message (Enter to send message to Arduino)"))
        # self.Clear.setText(_translate("MainWindow", "Clear Output"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))

    def scan_ports(self):                                               # Hàm quét các cổng COM
        self.Portbox.clear()                                            # Xoá các giá trị cổng COM trên QComboBox Portbox nếu đã quét từ trước
        available_ports = list(serial.tools.list_ports.comports())      # Gán giá trị của biến available_ports bằng danh sách các cổng COM
        for port in available_ports:                                    # Lần lượt thêm từng cổng COM hiển thị lên Portbox
            self.Portbox.addItem(port.device)
        self.status_label.setText("Đã quét xong các cổng COM.")         # Báo đã hoàn thành quét lên QLabel status_label

    def connect_port(self):                                             # Hàm kết nối tới cổng COM
        selected_port = self.Portbox.currentText()                      # Gán giá trị của biến available_ports bằng danh sách các cổng COM
        if selected_port:                                         
            self.status_label.setText(f"Đang kết nối đến {selected_port}...")           #Hiển thị lên status_label trạng thái đang kết nối
            self.serial_thread = threading.Thread(target=self.connect_thread, args=(selected_port,))    # Khởi tạo thread kết nối connect_thread
            self.serial_thread.daemon = True                            # Khai báo thread là một daemon
            self.serial_thread.start()                                  # Khởi chạy serial_thread
        else:
            self.status_label.setText("Chưa chọn cổng COM.")            # Hiển thị lên status_label trạng thái chưa chọn cổng COM

    def connect_thread(self, selected_port):
        baudrate = int(self.Bdbox.currentText())                        #Biến baudrate bằng giá trị hiện tại của QComboBox Bdbox
        try:
            self.serial_connection = serial.Serial(selected_port, baudrate, timeout=5)  # Kết nối tới cổng COM đã chọn
            self.is_connected = True                                    # Đã kết nối thành công
            self.status_label.setText(f"Kết nối đến {selected_port} thành công.")       # Hiển thị kết nối thành công lên
            self.Connect.setEnabled(False)                              # Vô hiệu nút Connect
        except serial.SerialException:                                  # Nếu xuất hiện lỗi kết nối
            self.is_connected = False
            self.status_label.setText(f"Kết nối đến {selected_port} thất bại.") # Hiển thị lên status_label kết nối đến cổng COM thất bại

    def disconnect_port(self):                                          # Hàm ngắt kết nối cổng COM
        if self.serial_connection is not None:
            self.serial_connection.close()                              # Ngắt kết nối cổng COM
            self.status_label.setText("Ngắt kết nối.")                  # Hiển thị trạng thái ngắt kết nối lên status_label
            self.is_connected = False                                   
            self.Connect.setEnabled(True)                               # Cho phép tương tác với nút Connect
        #     self.Kpline_2.clear()                                     
        #     self.Kiline_2.clear()
        #     self.Kdline_2.clear()
        else:
            self.status_label.setText("Không có kết nối cổng COM nào đang mở.")

    def send_parameters(self):
        if self.is_connected is True:  # Kiểm tra kết nối trước khi gửi lệnh
            k_p = self.Kpline.text()
            k_i = self.Kiline.text()
            k_d = self.Kdline.text()

            try:
                # Cập nhật các biến Kp, Ki và Kd từ các QLineEdit
                self.Kp = float(k_p)
                self.Ki = float(k_i)
                self.Kd = float(k_d)

                if self.serial_connection is not None and self.serial_connection.is_open:
                    self.serial_connection.write(f"{self.Kp},{self.Ki},{self.Kd}\n".encode())
                    self.status_label.setText(f"Đã gửi đến {self.port} : Kp={self.Kp}, Ki={self.Ki}, Kd={self.Kd}")
                    self.SerialMonitor.appendPlainText(f"Command: Kp={self.Kp}, Ki={self.Ki}, Kd={self.Kd}")
                    self.Kpline_2.setText(k_p)
                    self.Kiline_2.setText(k_i)
                    self.Kdline_2.setText(k_d)
                else:
                    self.status_label.setText("Chưa kết nối với cổng COM.")
            except ValueError:
                self.status_label.setText("Lỗi: Vui lòng nhập giá trị số hợp lệ cho Kp, Ki và Kd.")
        else:
            self.status_label.setText("Chưa kết nối với cổng COM.")

    def send_command(self):
        command = self.message.text()
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.write(command.encode() + b'\n')
            self.SerialMonitor.appendPlainText(f"Command: {command}")
            self.message.clear()  # Xóa nội dung trong QLineEdit sau khi gửi lệnh

    def clear_output(self):
        self.SerialMonitor.clear()
        
    def turn_left(self):
        if self.is_connected is True:
            try:
                if self.serial_connection is not None and self.serial_connection.is_open:
                    self.serial_connection.write(b'l\n')
                    self.status_label.setText(f"Turn left ◀")
                else:
                    self.status_label.setText("Chưa kết nối với cổng COM.")
            except Exception:
                pass
        else:
            self.status_label.setText("Chưa kết nối với cổng COM.")       
              
    def turn_right(self):
        if self.is_connected is True:
            try:
                if self.serial_connection is not None and self.serial_connection.is_open:
                    self.serial_connection.write(b'r\n')
                    self.status_label.setText(f"Turn right ▶")
                else:
                    self.status_label.setText("Chưa kết nối với cổng COM.")
            except Exception:
                pass
        else:
            self.status_label.setText("Chưa kết nối với cổng COM.")      
            
    def go_forward(self):
        if self.is_connected is True:
            try:
                if self.serial_connection is not None and self.serial_connection.is_open:
                    self.serial_connection.write(b'f\n')
                    self.status_label.setText(f"Go forward ▲")
                else:
                    self.status_label.setText("Chưa kết nối với cổng COM.")
            except Exception:
                pass
        else:
            self.status_label.setText("Chưa kết nối với cổng COM.")
            
    def go_backward(self):
        if self.is_connected is True:  # Kiểm tra kết nối trước khi gửi lệnh
            try:
                if self.serial_connection is not None and self.serial_connection.is_open:
                    self.serial_connection.write(b'b\n')
                    self.status_label.setText(f"Go backward ▼")
                else:
                    self.status_label.setText("Chưa kết nối với cổng COM.")
            except Exception:
                pass
        else:
            self.status_label.setText("Chưa kết nối với cổng COM.")
            
    def stop_move(self):
        if self.is_connected is True:
            try:
                if self.serial_connection is not None and self.serial_connection.is_open:
                    self.serial_connection.write(b's\n')
                    self.status_label.setText(f"Stop")
                else:
                    self.status_label.setText("Chưa kết nối với cổng COM.")
            except Exception:
                pass
        else:
            self.status_label.setText("Chưa kết nối với cổng COM.")   

    def update_plot(self):
        if self.serial_connection is not None:
                try:
                        arduinoData_string = self.serial_connection.readline().decode('ascii')
                        
                        if arduinoData_string:
                                try:
                                        arduinoData_float = float(arduinoData_string)
                                        self.angle.append(arduinoData_float)            

                                except ValueError as e:                                                                      
                                        pass
                        
                        self.time.append(len(self.time))
                        self.angle = self.angle[-1200:]         #SỐ DỮ LIỆU HIỂN THỊ ĐƯỢC TRÊN TRỤC X
                        self.time = self.time[-1200:]
                        
                        #self.angle.append(np.random.uniform(-90,90))
                
                        # if len(self.angle) > 50:
                        #         self.angle.pop(0)
                
                        self._line.set_data(np.arange(len(self.time)), self.angle)
                        self.ax.set_xlim(0, len(self.time))
                        self.ax.set_ylim(-2, 2)                 #GIỚI HẠN HIỂN THỊ DỮ LIỆU TRỤC Y
                
                        self.canvas.draw()
                        self.Data.clear()
                        self.Data.appendPlainText(f"Angle: {arduinoData_float}°")
                except Exception as e:
                        self.serial_connection.close()
                        self.Connect.setEnabled(True)    
        else:
                pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
