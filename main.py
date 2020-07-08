import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_Dialog
import os 

app = QtWidgets.QApplication(sys.argv)
    
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def search_def():
    os.startfile(r'PyPassMan(Search)\main.py')

def save_def():
    os.startfile(r'PyPassMan(Save)\main.py')
 
ui.pushButton.clicked.connect(save_def)
ui.pushButton_2.clicked.connect(search_def)

sys.exit(app.exec_())
