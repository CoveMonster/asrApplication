from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (QWidget, QAction, qApp, QLabel,
                             QLineEdit, QTextEdit, QGridLayout, QMainWindow, QApplication,
                             QTextBrowser, QListWidget, QSplitter, QToolBar)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import (QSettings, Qt, QByteArray)
import datetime
import qtawesome

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()
        self.init_ui()
        self.generateData()
        self.UI_style()

    def init_ui(self):
        self.setFixedSize(1200, 700)
        self.setWindowTitle('STalking')
        self.setWindowIcon(QIcon("icon/stlogo.ico"))
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件 左侧为功能按钮
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.center_Splitter = QSplitter(Qt.Horizontal)
        self.center_Splitter.setObjectName('center_Splitter')
        self.center_layout = QtWidgets.QGridLayout()
        self.center_Splitter.setLayout(self.center_layout)  # 设置右侧部件布局为网格


        self.main_layout.addWidget(self.left_widget, 0, 0, 16, 3)  # 左侧部件在第0行第0列，占8行3列
        # self.main_layout.addWidget(self.center_QWidget, 0, 3, 16, 17)  # 左侧部件在第0行第3列，占8行3列
        self.main_layout.addWidget(self.center_Splitter, 0, 3, 16, 17)  # 左侧部件在第0行第3列，占8行3列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.icon_button = QtWidgets.QToolButton()
        self.icon_button.setIcon(QtGui.QIcon('icon/stlogo.ico'))  # 设置按钮图标
        self.icon_button.setIconSize(QtCore.QSize(150, 100))  # 设置图标大小


        self.left_label_1 = QtWidgets.QPushButton("模型选择")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("保存与设置")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("其他")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.database', color='gray'), "选择GMM")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.file', color='gray'), "选择UBM")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.plus-circle', color='gray'), "选择视频")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.save', color='gray'), "保存模型")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.file', color='gray'), "模型路径")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.folder-open', color='gray'), "文件路径")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='gray'), "使用向导")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='gray'), "版权说明")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='gray'), "关于我们")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.icon_button, 0, 0.5, 1, 3)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)



        self.model_list_widget = QtWidgets.QWidget()
        self.model_list_widget.setObjectName('model_widget')
        self.model_list_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.model_list_widget.setLayout(self.model_list_layout)  # 设置左侧部件布局为网格



        self.model_list_label = QtWidgets.QLabel("模型列表")
        self.model_list_label.setObjectName('my_lable')

        self.model_view_list = QListWidget()  # 文件列表
        self.model_view_list.setObjectName('my_list')
        # self.model_view_list.setFixedWidth(200)
        self.right_Splitter = QSplitter(Qt.Vertical)
        self.right_Splitter.setObjectName('right_Splitter')


        self.model_list_layout.addWidget(self.model_list_label, 0, 0, 1, 1)
        self.model_list_layout.addWidget(self.model_view_list, 1, 0, 9, 1)

        self.center_Splitter.addWidget(self.model_list_widget)
        self.center_Splitter.addWidget(self.right_Splitter)
        self.center_Splitter.setStretchFactor(0, 2)
        self.center_Splitter.setStretchFactor(1, 8)

        self.result_label = QtWidgets.QLabel("数据分析")
        self.result_label.setFixedHeight(80)
        self.result_label.setObjectName('my_lable')

        self.right_html_page_TabWidget = QtWidgets.QTabWidget()
        self.right_html_page_TabWidget.setObjectName('right_html_page_TabWidget')
        self.right_log_widget = QtWidgets.QWidget()  # log 框 = button + log
        self.right_log_widget.setObjectName('right_log_widget')
        self.right_log_layout = QtWidgets.QGridLayout()
        self.right_log_widget.setLayout(self.right_log_layout)  # 设置右侧部件布局为网格

        self.right_Splitter.addWidget(self.result_label)
        self.right_Splitter.addWidget(self.right_html_page_TabWidget)
        self.right_Splitter.addWidget(self.right_log_widget)
        self.right_Splitter.setStretchFactor(0, 1)
        self.right_Splitter.setStretchFactor(1, 9)
        self.right_Splitter.setStretchFactor(2, 1)

        self.right_log_toolbar = QToolBar()
        self.right_log_toolbar.setObjectName('right_log_toolbar')
        self.right_log_toolbar.setOrientation(Qt.Vertical)
        # self.right_button_layout.addWidget(self.toolbarGmm)
        delete_action = QAction(QIcon('icon/delete-gray.png'), '清空日志', self)
        self.right_log_toolbar.addAction(delete_action)
        export_action = QAction(QIcon('icon/save_m.png'), '导出日志', self)
        self.right_log_toolbar.addAction(export_action)
        # self.right_log_layout.setSpacing(0)
        self.right_log_contend = QListWidget()
        # self.right_log_contend.setFixedHeight(100)
        self.right_log_contend.setObjectName('my_list')
        self.right_log_layout.addWidget(self.right_log_toolbar, 0, 0, 1, 3)
        self.right_log_layout.addWidget(self.right_log_contend, 0, 1, 1, 18)


    # 定义 css
    def UI_style(self):
        self.main_widget.setStyleSheet('''
            QWidget#main_widget{
                background:#EBEBEB;
                border-top:1px solid #EBEBEB;
                border-bottom:1px solid #EBEBEB;
                border-left:1px solid #EBEBEB;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }

        ''')
        self.result_label.setStyleSheet('''
            QLabel{
                border:none;
                background:#EBEBEB;
                font-size:20px;
                font-weight:900;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.model_list_label.setStyleSheet('''
                    QLabel{
                        border:none;
                        background:#EBEBEB;
                        font-size:20px;
                        font-weight:900;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }

                ''')
        self.icon_button.setStyleSheet('''
            QToolButton{
                border:none;
                background:#EBEBEB;
            }
        ''')
        self.main_widget.setStyleSheet('''
            QWidget#center_QWidget{
                color:#232C51;
                background:#EBEBEB;
                border-top:1px solid #EBEBEB;
                border-bottom:1px solid #EBEBEB;
                border-right:1px solid #EBEBEB;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QWidget#left_widget{
                        background:#EBEBEB;
                        border-top:1px solid #EBEBEB;
                        border-bottom:1px solid #EBEBEB;
                        border-left:1px solid #EBEBEB;
                        border-top-left-radius:10px;
                        border-bottom-left-radius:10px;
                    }
        ''')
        self.model_list_widget.setStyleSheet('''
            QListWidget#my_list{
                background:light white;
                border:none;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }
        ''')
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:gray;font-size:18px;font-weight:700;}
            QPushButton#left_label{
                    border:none;
                    border-bottom:1px solid dark gray;
                    font-size:20px;
                    font-weight:900;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')
        self.center_Splitter.setStyleSheet('''
            QSplitter#center_Splitter{
                background:#EBEBEB;
            }
            QSplitter#right_Splitter{
                background:#EBEBEB;
            }
            QTabWidget#right_html_page_TabWidget{
                width:300px;
                border-radius:10px;
                padding:2px 4px;
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            }
            QLabel#my_lable{
                background-color:#EBEBEB;
                border:none;
                font-size:20px;
                font-weight:bold;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
             QToolBar#right_log_toolbar{
                border:none;
                background-color: #EBEBEB;
            }
            QListWidget#my_list{
                background:light white;
                border:none;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }

        ''')
        self.model_list_label.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.model_list_label.setStyleSheet('''
            QLabel{
                background-color:light gray;
                border:none;
                font-size:20px;
                font-weight:bold;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_log_widget.setStyleSheet('''
            QListWidget#right_log_widget{
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }
            QToolBar#right_log_toolbar{
                border:none;
                background-color: light gray;
            }
            QListWidget#right_log_contend{
                background:#EBEBEB;
                border:none;
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }
        ''')

        # self.setWindowOpacity(1)  # 设置窗口透明度
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.main_layout.setSpacing(0)


    def generateData(self):
        for group in range(1, 100):
            self.model_view_list.addItem("model_{0}".format(group))
        for group in range(1, 100):
            self.right_log_contend.addItem((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                         " : operation_{0}").format(group))
        for group in range(1, 4):
            self.tabItem = QTextBrowser()
            self.right_html_page_TabWidget.addTab(self.tabItem, "page_{0}".format(group))
            self.tabItem.setHtml("""<table bgcolor=yellow>
        <tr><td>Groups:</td><td>comp.lang.python.announce</td></tr>
        <tr><td>From:</td><td>"Fuzzyman" &lt;fuzzy...@gmail.com&gt;</td></tr>
        <tr><td>Subject:</td><td><b>[ANN] Movable Python 2.0.0 Final
        Available</b></td></tr>
        </table>

        <h3>Movable Python 2.0.0 Final</h3>
        <p>
        <a href="http://www.voidspace.org.uk/python/movpy/">
        http://www.voidspace.org.uk/python/movpy/</a>
        is now available.

        <p>
        The new binaries are available for download from the groups page :

        <p>Movable Python Groups Page
        <a href="http://voidspace.tradebit.com/groups.php">
        http://voidspace.tradebit.com/groups.php</a>
        <p>
        Binaries are uploaded for Python 2.2.3, 2.3.5, 2.4.4, 2.5 and the
        MegaPack
        <a href="http://www.voidspace.org.uk/python/movpy/megapack.html">
        http://www.voidspace.org.uk/python/movpy/megapack.html</a>.
        <p>
        There is also a fresh version of the free demo, based on Python 2.3.5:

        <p>Movable Python Trial Version
        <a href="http://voidspace.tradebit.com/files.php/7007">
        http://voidspace.tradebit.com/files.php/7007</a>

        <h3>What is Movable Python</h3>

        <p>
        <b><i>Movable Python</i></b> is a distribution of Python, for Windows,
        that can run without being installed. It means you can carry a full
        development environment round on a USB stick.

        <p>
        It is also useful for testing programs with a 'clean Python install',
        and testing programs with multiple versions of Python.

        <p>
        The GUI program launcher makes it a useful programmers tool, including
        features like :

        <ul>
        <li>Log the output of all Python scripts run
        <li>Enable Psyco for all scripts
        <li>Quick Launch buttons for commonly used programs
        <li>Configure multiple interpreters for use from a single interface
        </ul>
        <p>
        It comes with the Pythonwin IDE and works fine with other IDEs like
        SPE
        <a href="http://developer.berlios.de/projects/python/">
        http://developer.berlios.de/projects/python/</a>.
        <p>
        Plus many other features and bundled libraries.""")


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = Ui_MainWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()