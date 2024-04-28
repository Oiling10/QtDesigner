import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtCore import Qt

qtCreatorFile="Practica_Gui.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Practica(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Practica()
    window.show()
    sys.exit(app.exec_())
    