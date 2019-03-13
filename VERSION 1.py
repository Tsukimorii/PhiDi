# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VERSION1.ui'
#
# Created: Fri Dec 28 14:56:30 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
import matplotlib as mpl
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpldatacursor import datacursor
import scipy
from scipy import signal
import numpy as np
import control
from matplotlib.pyplot import * # Grab MATLAB plotting functions
from control.matlab import *    # MATLAB-like functions

mpl.style.use('classic')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Main Window Set Up
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(353, 563)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 311, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        #User Inputs
        self.LineEdit = QtGui.QLineEdit(self.groupBox)
        self.LineEdit.setGeometry(QtCore.QRect(20, 40, 121, 22))
        self.LineEdit.setObjectName(_fromUtf8("LineEdit"))
        self.LineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.LineEdit_2.setGeometry(QtCore.QRect(20, 80, 121, 22))
        self.LineEdit_2.setObjectName(_fromUtf8("LineEdit"))
        self.LineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.LineEdit_3.setGeometry(QtCore.QRect(20, 120, 121, 22))
        self.LineEdit_3.setObjectName(_fromUtf8("LineEdit_2"))
        self.LineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.LineEdit_4.setGeometry(QtCore.QRect(20, 160, 121, 22))
        self.LineEdit_4.setObjectName(_fromUtf8("LineEdit_5"))
        self.LineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.LineEdit_5.setGeometry(QtCore.QRect(170, 40, 121, 22))
        self.LineEdit_5.setObjectName(_fromUtf8("LineEdit_4"))
        self.LineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.LineEdit_6.setGeometry(QtCore.QRect(170, 80, 121, 22))
        self.LineEdit_6.setObjectName(_fromUtf8("LineEdit_16"))
        self.LineEdit_7 = QtGui.QLineEdit(self.groupBox)
        self.LineEdit_7.setGeometry(QtCore.QRect(170, 120, 121, 22))
        self.LineEdit_7.setObjectName(_fromUtf8("LineEdit_17"))
        self.LineEdit_8 = QtGui.QLineEdit(self.groupBox)
        self.LineEdit_8.setGeometry(QtCore.QRect(170, 160, 121, 22))
        self.LineEdit_8.setObjectName(_fromUtf8("LineEdit_18"))
        
        #Widget Layout
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 240, 221, 260))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        
        #Push Buttons
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pushButton_7 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_7.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout_6.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_6.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout_6.addWidget(self.pushButton_9)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        self.pushButton_4.clicked.connect(self.plot1)
        self.pushButton_5.clicked.connect(self.plot2)
        self.pushButton_6.clicked.connect(self.plot3)
        self.pushButton_7.clicked.connect(self.plot4)
        self.pushButton_8.clicked.connect(self.plot5)
        self.pushButton_9.clicked.connect(self.plot6)
        self.dialogs = list()
        
    def plot1(self):
        global a, b, c, d, e, f, g, h
        a = float(self.LineEdit.text())
        b = float(self.LineEdit_2.text())
        c = float(self.LineEdit_3.text())
        d = float(self.LineEdit_4.text())
        e = float(self.LineEdit_5.text())
        f = float(self.LineEdit_6.text())
        g = float(self.LineEdit_7.text())
        h = float(self.LineEdit_8.text())
        
        G = control.TransferFunction((a,b,c,d), (e,f,g,h))
        kvect=np.linspace(100.0, -100.0, num=1000)
        rlist, klist = control.rlocus(G, kvect)
        dc = datacursor(display='multiple', draggable=True, bbox=dict(fc='white'))
        plt.gcf().canvas.set_window_title('Root Locus')
        plt.title('Root Locus')
        plt.grid()
        plt.draw()
        plt.show()
   
    def plot2(self):
        global a, b, c, d, e, f, g, h
        a = float(self.LineEdit.text())
        b = float(self.LineEdit_2.text())
        c = float(self.LineEdit_3.text())
        d = float(self.LineEdit_4.text())
        e = float(self.LineEdit_5.text())
        f = float(self.LineEdit_6.text())
        g = float(self.LineEdit_7.text())
        h = float(self.LineEdit_8.text())
        
        plt.figure(1)
        G = control.TransferFunction((a,b,c,d), (e,f,g,h))
        mag, phase, omega = control.bode(G)          
        dc = datacursor(display='multiple', draggable=True, bbox=dict(fc='white'))
        plt.title('Bode Plots', y= 2.20) 
        plt.gcf().canvas.set_window_title('Bode Plots')
        plt.xlabel('Frequency (rad/s)')
        plt.grid()
        plt.draw()
        plt.show()
        
    def plot3(self):
        global a, b, c, d, e, f, g, h
        a = float(self.LineEdit.text())
        b = float(self.LineEdit_2.text())
        c = float(self.LineEdit_3.text())
        d = float(self.LineEdit_4.text())
        e = float(self.LineEdit_5.text())
        f = float(self.LineEdit_6.text())
        g = float(self.LineEdit_7.text())
        h = float(self.LineEdit_8.text())
        
        plt.figure(2)
        G = control.TransferFunction((a,b,c,d), (e,f,g,h))
        real, imag, freq = control.nyquist_plot(G)
        dc = datacursor(display='multiple', draggable=True, bbox=dict(fc='white'))
        plt.title('Nyquist Plot') 
        plt.gcf().canvas.set_window_title('Nyquist Plot')
        plt.xlabel('Real')
        plt.ylabel('Imaginary')
        plt.grid() 
        plt.draw()    
        plt.show()   
        
    def plot4(self):
        global a, b, c, d, e, f, g, h
        a = float(self.LineEdit.text())
        b = float(self.LineEdit_2.text())
        c = float(self.LineEdit_3.text())
        d = float(self.LineEdit_4.text())
        e = float(self.LineEdit_5.text())
        f = float(self.LineEdit_6.text())
        g = float(self.LineEdit_7.text())
        h = float(self.LineEdit_8.text())
    
        G = control.TransferFunction((a,b,c,d), (e,f,g,h))
        nichols(G)
        plt.title('Nichols Plot') 
        plt.gcf().canvas.set_window_title('Nichols Plot')
        plt.grid()
        plt.show()
    
    def plot5(self):
        global a, b, c, d, e, f, g, h
        a = float(self.LineEdit.text())
        b = float(self.LineEdit_2.text())
        c = float(self.LineEdit_3.text())
        d = float(self.LineEdit_4.text())
        e = float(self.LineEdit_5.text())
        f = float(self.LineEdit_6.text())
        g = float(self.LineEdit_7.text())
        h = float(self.LineEdit_8.text())
        
        G = signal.TransferFunction((a,b,c,d), (e,f,g,h))
        T, yout = signal.step(G)
        plt.figure(3)
        plt.plot(T,yout)
        plt.gcf().canvas.set_window_title('Step Response')
        dc = datacursor(display='multiple', draggable=True, bbox=dict(fc='white'))
        plt.title('Step Response')
        plt.ylabel('Amplitude')
        plt.xlabel('Time(s)')
        plt.grid()
        plt.imshow()
        
    def plot6(self):
        global a, b, c, d, e, f, g, h
        a = float(self.LineEdit.text())
        b = float(self.LineEdit_2.text())
        c = float(self.LineEdit_3.text())
        d = float(self.LineEdit_4.text())
        e = float(self.LineEdit_5.text())
        f = float(self.LineEdit_6.text())
        g = float(self.LineEdit_7.text())
        h = float(self.LineEdit_8.text())
        
        G = signal.TransferFunction((a,b,c,d), (e,f,g,h))
        w, H = signal.freqresp(G)
        plt.figure(4)
        plt.plot(H.real, H.imag, "b")
        plt.plot(H.real, -H.imag, "r")
        plt.gcf().canvas.set_window_title('Frequency Response')
        dc = datacursor(display='multiple', draggable=True, bbox=dict(fc='white'))
        plt.title('Frequency Response')
        plt.ylabel('Magnitude (dB)')
        plt.xlabel('Frequency (rad/s)')
        plt.grid()
        plt.imshow()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Coefficients", None))
        self.pushButton_4.setText(_translate("MainWindow", "Generate Root Locus", None))
        self.pushButton_5.setText(_translate("MainWindow", "Generate Bode Plot", None))
        self.pushButton_6.setText(_translate("MainWindow", "Generate Nyquist Plot ", None))
        self.pushButton_7.setText(_translate("MainWindow", "Generate Nichols Plot", None))
        self.pushButton_8.setText(_translate("MainWindow", "Generate Step Response", None))
        self.pushButton_9.setText(_translate("MainWindow", "Generate Frequency Response", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

