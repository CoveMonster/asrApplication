# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#encoding = utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    # define ui component and sub_frame
    def setupUi(self, MainWindow):
        # frame 界面
        # 1 定义外层容器
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(10, 0, 1000, 600))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("语音识别")
        # 1.1 定义上层容器

        # 1.1.1 定义button按钮容器

        # 1.1.2 定义log日志文本框容器

        # 1.2 定义结果展示面板容器
        # 1.2.1 定义结果3个抽卡结果面板
        self.groupBox = QtWidgets.QGroupBox(self.mainFrame)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 981, 131))
        self.groupBox.setObjectName("groupBox")
        self.buttonBox = QtWidgets.QWidget(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(10, 20, 501, 101))
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.buttonBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.buttonBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 20, 90, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.buttonBox)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 20, 90, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.TextScroll = QtWidgets.QScrollArea(self.groupBox)
        self.TextScroll.setGeometry(QtCore.QRect(530, 20, 431, 101))
        self.TextScroll.setWidgetResizable(True)
        self.TextScroll.setObjectName("TextScroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 90, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 50, 90, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.TextScroll.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_3 = QtWidgets.QGroupBox(self.mainFrame)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 981, 441))
        self.groupBox_3.setObjectName("groupBox_3")
        self.result = QtWidgets.QTabWidget(self.groupBox_3)
        self.result.setGeometry(QtCore.QRect(10, 20, 951, 431))
        self.result.setObjectName("result")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.result.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.result.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.result.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "模型选择"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.groupBox_3.setTitle(_translate("MainWindow", "结果"))
        self.result.setTabText(self.result.indexOf(self.tab), _translate("MainWindow", "result 1"))
        self.result.setTabText(self.result.indexOf(self.tab_3), _translate("MainWindow", "result 3"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "说明"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
