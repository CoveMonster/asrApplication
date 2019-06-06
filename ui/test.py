from PyQt5.QtWidgets import QAction, QMessageBox, QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys
from functools import partial


class MunDemo(QMainWindow):
    def __init__(self):
        super(MunDemo, self).__init__(parent=None)
        self.setWindowTitle("Example for ToolBar")
        self.setWindowIcon(QIcon("./images/cartoon1.ico"))
        self.resize(500, 300)

        action = partial(newAction, self)

        open = action("Open", self.open, "Ctrl+o",
                      "open", u"Open  file")

        save = action("Save", self.save, "Ctrl+S",
                      "save", u"Save file")

        close = action("Close", self.close, "Ctrl+Q",
                       "quit", u"Close window")

        new = action("New", self.new, "Ctrl+N",
                     "new", u"New a project")

        self.toolBarMenu = (new, open, save, close)
        tb = self.addToolBar("File")
        self.addAct(tb, self.toolBarMenu)

    def new(self):
        QMessageBox.information(self, "提示",
                                "New a project！", QMessageBox.Ok)

    def save(self):
        QMessageBox.information(self, "提示",
                                "Save file！", QMessageBox.Ok)

    def open(self):
        QMessageBox.information(self, "提示",
                                "Open  file！", QMessageBox.Ok)

    def addAct(self, tb, actions):
        for action in actions:
            if action is not None:
                tb.addAction(action)

            else:
                self.addSeparator()


def newAction(parent, text, slot=None, shortcut=None, icon=None,
              tip=None, checkable=False, enable=True):
    a = QAction(text, parent)

    if tip is not None:
        a.setToolTip(tip)
        a.setStatusTip(tip)
    if icon is not None:
        a.setIcon(newIcon(icon))

    if shortcut is not None:
        if isinstance(shortcut, (list, tuple)):
            a.setShortcuts(shortcut)
        else:
            a.setShortcut(shortcut)

    if slot is not None:
        a.triggered.connect(slot)

    if checkable:
        a.setCheckable(checkable)
    a.setEnabled(enable)

    return a


def newIcon(icon):
    path = "./images/" + icon + ".png"
    return QIcon(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MunDemo()
    demo.show()
    sys.exit(app.exec_())