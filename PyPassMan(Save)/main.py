import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_Dialog
import os 

app = QtWidgets.QApplication(sys.argv)
    
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def saving():
    soc = ui.lineEdit.text()
    log = ui.lineEdit_2.text()
    passw = ui.lineEdit_3.text()

    soc1 = ('Social Network:') + soc
    log1 = ('Login:') + log
    passw1 = ('Password:') + passw

    all1 = soc  + (' ; ') + soc + log1 + (' ; ') + soc + passw1

    file = open('login.txt', 'a')
    file.write('\n' + all1)
    file.close

    ui.label.setText(f'Status: Saved!')

ui.pushButton.clicked.connect(saving)

sys.exit(app.exec_())