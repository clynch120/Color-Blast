import sys
import random
from PyQt4 import QtGui, QtCore

class GUI (QtGui.QMainWindow):

    def __init__ (self):
        super (GUI, self).__init__()
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle("Guess the number")
        self.setWindowIcon(QtGui.QIcon('py.png'))

        quitAction = QtGui.QAction("&Quit", self)
        quitAction.setShortcut ("Ctrl+Q")
        quitAction.setStatusTip("Leave The App")
        quitAction.triggered.connect(self.closeApp)

        self.statusBar()

        mainMenu= self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(quitAction)
        self.show()

    def closeApp(self):
        print ("Awesome")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    win = GUI()
    sys.exit(app.exec_())

run()

