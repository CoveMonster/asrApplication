from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (QWidget, QAction, qApp, QLabel,
                             QLineEdit, QTextEdit, QGridLayout, QMainWindow, QApplication,
                             QTextBrowser, QListWidget, QSplitter, QToolBar)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import (QSettings, Qt, QByteArray)
import datetime

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    # 初始化 界面
    def initUI(self):
        # 添加菜单和工具栏
        self.createMenusAndToolbars()
        # 设置页面布局
        self.createDesktop()
        self.generateData()
        self.setGeometry(300, 100, 1200, 800)
        self.setWindowTitle('师生说')
        # self.setWindowIcon(self, "icon/logo.jpg")
        self.setWindowIcon(QIcon("icon/logo.ico"))
        self.show()

    # 定义菜单 和 工具栏
    def createMenusAndToolbars(self):
        # 定义菜单栏
        menuBar = self.menuBar()
        model_menu = menuBar.addMenu("模型选择")
        setting_menu = menuBar.addMenu("设置")
        guide_menu = menuBar.addMenu("说明指南")
        copyright = menuBar.addMenu("版权说明")
        # 模型选择 菜单项
        basic_model_menu_action = QAction(QIcon("icon/cloud.png"), "基础模型", self)
        new_model_menu_action = QAction(QIcon("icon/file-fill.png"), "训练新模型", self)
        select_model_menu_action = QAction(QIcon("icon/file plus-fill.png"), "选择模型", self)
        save_model_menu_action = QAction(QIcon("icon/save.png"), "保存模型", self)
        model_menu.addAction(basic_model_menu_action)
        model_menu.addAction(new_model_menu_action)
        model_menu.addAction(select_model_menu_action)
        model_menu.addAction(save_model_menu_action)

        # 设置  菜单项
        save_path_setting = QAction("模型保存路径", self)
        other_setting = QAction("other...", self)
        setting_menu.addAction(save_path_setting)
        setting_menu.addAction(other_setting)

        # 说明指南 菜单项
        guide_item = QAction("向导说明", self)
        author_intro_item = QAction("作者介绍", self)
        guide_menu.addAction(guide_item)
        guide_menu.addAction(author_intro_item)

        # 定义工具栏
        # self.toolbarGmm = self.addToolBar('GMM')
        self.toolbarGmm = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea, self.toolbarGmm)
        # self.toolbarModel = self.addToolBar('Model')
        # self.toolbarSetting = self.addToolBar('Setting')

        # add GMM UBM button
        gmmAction = QAction(QIcon('icon/cloud.png'), '选择UBM', self)
        self.toolbarGmm.addAction(gmmAction)
        for oen in range(0,5):
            self.toolbarGmm.addSeparator()
        # add 'new model' button
        newModelAction = QAction(QIcon('icon/file-fill.png'), '选择GMM', self)
        self.toolbarGmm.addAction(newModelAction)
        for oen in range(0,5):
            self.toolbarGmm.addSeparator()
        # add 'select model' button
        selectModelAction = QAction(QIcon('icon/file plus-fill.png'), '选择课堂视频', self)
        self.toolbarGmm.addAction(selectModelAction)
        for oen in range(0,5):
            self.toolbarGmm.addSeparator()
        # add 'save model' button
        # saveModelAction = QAction(QIcon('icon/save.png'), '保存模型', self)
        # self.toolbarModel.addAction(saveModelAction)

        # add 'setting' button
        # settingAction = QAction(QIcon('icon/cog.png'), '设置', self)
        # self.toolbarSetting.addAction(settingAction)

    def createDesktop(self):
        self.modelViewList = QListWidget()
        self.logMessageView = QListWidget()

        # self.logmodule = QtWidgets.QGroupBox()  # log module

        # self.logmodule.setLayout(Qt.Horizontal)
        # self.logMessageView = QTextBrowser()
        # self.resultView =
        self.resultView = QtWidgets.QTabWidget()

        self.logOperationBtn = QtWidgets.QToolBar()
        self.clearLog = QAction(QIcon('icon/clearLog.png'), '清除日志', self)
        self.logOperationBtn.addAction(self.clearLog)
        #
        # self.logmodule.addWidget(self.logOperationBtn)
        # self.logmodule.addWidget(self.logMessageView)
        # self.logmodule.setStretchFactor(0, 1)
        # self.logmodule.setStretchFactor(1, 10)


        self.responseSplitter = QSplitter(Qt.Vertical)
        self.responseSplitter.addWidget(self.resultView)
        self.responseSplitter.addWidget(self.logOperationBtn)
        self.responseSplitter.addWidget(self.logMessageView)
        # self.responseSplitter.addWidget(self.logmodule)
        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.modelViewList)
        self.mainSplitter.addWidget(self.responseSplitter)
        self.setCentralWidget(self.mainSplitter)

        self.mainSplitter.setStretchFactor(0, 1)
        self.mainSplitter.setStretchFactor(1, 4)
        self.responseSplitter.setStretchFactor(0, 8)
        self.responseSplitter.setStretchFactor(1, 1)
        self.responseSplitter.setStretchFactor(1, 2)
        # self.responseSplitter.set(2, False)

    def generateData(self):
        for group in range(1, 100):
            self.modelViewList.addItem("model_{0}".format(group))
        for group in range(1, 20):
            self.logMessageView.addItem((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+
                                         " : operation_{0}").format(group))
        for group in range(1, 4):
            self.tabItem = QTextBrowser()
            self.resultView.addTab(self.tabItem, "page_{0}".format(group))
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())