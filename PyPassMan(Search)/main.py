import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_Dialog
import os 

app = QtWidgets.QApplication(sys.argv)
    
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def searching():
    soc = ui.lineEdit.text()

    soc1 = soc
    
    with open('login.txt') as file:
        lines = file.readlines()

        for line in lines:
            if soc1 in line:
                ui.label.setText('Data: ' + line)

    ui.label.setText('Data: ' + line)
    
ui.pushButton.clicked.connect(searching)

sys.exit(app.exec_())


