# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boltz_teste.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 130)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ln_edit_nconf = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_edit_nconf.setObjectName("ln_edit_nconf")
        self.gridLayout.addWidget(self.ln_edit_nconf, 1, 1, 1, 1)
        self.lbl_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info.setObjectName("lbl_info")
        self.gridLayout.addWidget(self.lbl_info, 1, 0, 1, 1)
        self.ln_edit_temp = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_edit_temp.setObjectName("ln_edit_temp")
        self.gridLayout.addWidget(self.ln_edit_temp, 0, 1, 1, 1)
        self.lbl_info2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info2.setObjectName("lbl_info2")
        self.gridLayout.addWidget(self.lbl_info2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 272, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_quit = QtWidgets.QAction(MainWindow)
        self.menu_quit.setObjectName("menu_quit")
        self.menuFile.addAction(self.menu_quit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Boltzmann Distribution"))
        self.lbl_info.setText(_translate("MainWindow", "Type the number of conformations:"))
        self.lbl_info2.setText(_translate("MainWindow", "Type the temperature (K):"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu_quit.setText(_translate("MainWindow", "Quit"))
        self.menu_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


