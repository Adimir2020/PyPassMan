# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 280)
        Dialog.setStyleSheet("background-color: #282828;")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_5.setStyleSheet("color: #ffffff;\n"
"font: 5 8pt \"Century Gothic\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 80, 281, 41))
        self.lineEdit.setStyleSheet("border: none;\n"
"background-color: #ffffff;\n"
"color: #808080;\n"
"font: 5 12pt \"Century Gothic\";\n"
"border-radius: 15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 0, 161, 41))
        self.label_4.setStyleSheet("color: #0077FF;\n"
"font: 5 22pt \"Century Gothic\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 260, 61, 16))
        self.label_3.setStyleSheet("color: #ffffff;\n"
"font: 5 8pt \"Century Gothic\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 210, 151, 41))
        self.pushButton.setStyleSheet("color:#FFFFFF;\n"
"background-color: #0077FF;\n"
"border:none;\n"
"font: 5 12pt \"Century Gothic\";\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 140, 481, 61))
        self.label.setStyleSheet("color: #0077FF;\n"
"font: 5 10pt \"Century Gothic\";\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "By: ADN"))
        self.lineEdit.setText(_translate("Dialog", " Social Network: "))
        self.label_4.setText(_translate("Dialog", "PyPassMan"))
        self.label_3.setText(_translate("Dialog", "version: 1.1"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Data:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())