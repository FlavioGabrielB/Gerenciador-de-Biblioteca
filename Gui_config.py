import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Menu import *
from Tela_cadastro_config import *
from sobre import *



class cadastro(QMainWindow):
    def __init__(self):
        super(cadastro,self).__init__()
        self.ui = config()
        self.ui.setupUi(self)


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = Ui_MainWindow()
        self.menu.setupUi(self)
        self.uii = Uii()
        self.ui = config()
        self.ui.pushButton.clicked.connect(self.voltar)
        self.menu.pushButton_2.clicked.connect(self.abrir)
        self.menu.pushButton_3.clicked.connect(self.mudajanela)

    def mudajanela(self):
        self.ui.show()
        self.hide()

    def abrir(self):
        self.uii = sobre()
        self.uii.show()
        

    def voltar(self):
        self.ui.hide()
        self.show()

class sobre(QMainWindow):
    def __init__(self):
        super(sobre,self).__init__()
        self.uii = Uii()
        self.uii.setupUi(self)



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = Menu()
    view.show()
    qt.exec()
