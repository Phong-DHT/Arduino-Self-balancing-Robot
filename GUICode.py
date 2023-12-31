# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1084, 841)
        MainWindow.setMinimumSize(QtCore.QSize(1084, 841))
        MainWindow.setMaximumSize(QtCore.QSize(1084, 841))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 51, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
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
"}\n"
"QComboBox QListView{\n"
"    border: 1px;\n"
"    outline: 0px;\n"
"}\n"
"")
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
"}")
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
        self.PID.setEnabled(False)
        self.PID.setGeometry(QtCore.QRect(10, 210, 321, 231))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
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
"}")
        self.Kpline.setObjectName("Kpline")
        self.Kiline = QtWidgets.QLineEdit(self.PID)
        self.Kiline.setGeometry(QtCore.QRect(60, 90, 111, 22))
        self.Kiline.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"}")
        self.Kiline.setObjectName("Kiline")
        self.Kdline = QtWidgets.QLineEdit(self.PID)
        self.Kdline.setGeometry(QtCore.QRect(60, 130, 111, 22))
        self.Kdline.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"}")
        self.Kdline.setObjectName("Kdline")
        self.Kp = QtWidgets.QLabel(self.PID)
        self.Kp.setGeometry(QtCore.QRect(20, 50, 55, 21))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
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
"}")
        self.Kpline_2.setObjectName("Kpline_2")
        self.Kiline_2 = QtWidgets.QLineEdit(self.PID)
        self.Kiline_2.setGeometry(QtCore.QRect(240, 90, 61, 22))
        self.Kiline_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"}")
        self.Kiline_2.setObjectName("Kiline_2")
        self.Kdline_2 = QtWidgets.QLineEdit(self.PID)
        self.Kdline_2.setGeometry(QtCore.QRect(240, 130, 61, 22))
        self.Kdline_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"}")
        self.Kdline_2.setObjectName("Kdline_2")
        self.Send = QtWidgets.QPushButton(self.PID)
        self.Send.setGeometry(QtCore.QRect(20, 170, 281, 41))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 600, 1061, 231))
        font = QtGui.QFont()
        font.setFamily("gg sans SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(58, 61, 67);\n"
"    color:rgb(255, 255, 255);\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.message = QtWidgets.QLineEdit(self.groupBox)
        self.message.setGeometry(QtCore.QRect(10, 30, 861, 31))
        self.message.setMinimumSize(QtCore.QSize(0, 31))
        self.message.setMaximumSize(QtCore.QSize(1041, 31))
        self.message.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    font: 63 8pt \"gg sans Medium\";\n"
"}")
        self.message.setObjectName("message")
        self.SerialMonitor = QtWidgets.QTextBrowser(self.groupBox)
        self.SerialMonitor.setGeometry(QtCore.QRect(10, 70, 1041, 151))
        self.SerialMonitor.setMinimumSize(QtCore.QSize(1041, 151))
        self.SerialMonitor.setMaximumSize(QtCore.QSize(1041, 151))
        self.SerialMonitor.setStyleSheet("QTextBrowser {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.SerialMonitor.setObjectName("SerialMonitor")
        self.Clear = QtWidgets.QPushButton(self.groupBox)
        self.Clear.setGeometry(QtCore.QRect(880, 30, 171, 31))
        self.Clear.setStyleSheet("QPushButton {\n"
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
        self.Clear.setObjectName("Clear")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(330, 10, 751, 581))
        self.frame.setStyleSheet("QWidget {\n"
"    border-radius: 5px;\n"
"    font: 10pt \"gg sans SemiBold\";\n"
"}")
        self.frame.setObjectName("frame")
        self.Data = QtWidgets.QLineEdit(self.frame)
        self.Data.setGeometry(QtCore.QRect(520, 10, 221, 21))
        self.Data.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"}")
        self.Data.setObjectName("Data")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arduino SBRobot"))
        self.Terminal.setTitle(_translate("MainWindow", "Terminal"))
        self.Bdbox.setItemText(0, _translate("MainWindow", "200"))
        self.Bdbox.setItemText(1, _translate("MainWindow", "2400"))
        self.Bdbox.setItemText(2, _translate("MainWindow", "4800"))
        self.Bdbox.setItemText(3, _translate("MainWindow", "9600"))
        self.Bdbox.setItemText(4, _translate("MainWindow", "19200"))
        self.Bdbox.setItemText(5, _translate("MainWindow", "38400"))
        self.Bdbox.setItemText(6, _translate("MainWindow", "57600"))
        self.Bdbox.setItemText(7, _translate("MainWindow", "115200"))
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
        self.groupBox.setTitle(_translate("MainWindow", "Command"))
        self.message.setPlaceholderText(_translate("MainWindow", "Message (Enter to send message to Arduino)"))
        self.Clear.setText(_translate("MainWindow", "Clear Output"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
