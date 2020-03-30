# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas\ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 179)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_convertir_dolares = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_dolares.setGeometry(QtCore.QRect(10, 90, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.boton_convertir_dolares.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ventanas\\coin-dollar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_dolares.setIcon(icon)
        self.boton_convertir_dolares.setIconSize(QtCore.QSize(32, 32))
        self.boton_convertir_dolares.setObjectName("boton_convertir_dolares")
        self.boton_convertir_yenes = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_yenes.setGeometry(QtCore.QRect(270, 90, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.boton_convertir_yenes.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ventanas\\coin-yen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_convertir_yenes.setIcon(icon1)
        self.boton_convertir_yenes.setIconSize(QtCore.QSize(32, 32))
        self.boton_convertir_yenes.setObjectName("boton_convertir_yenes")
        self.edit_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_euros.setGeometry(QtCore.QRect(270, 10, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.edit_euros.setFont(font)
        self.edit_euros.setObjectName("edit_euros")
        self.edit_resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_resultado.setEnabled(False)
        self.edit_resultado.setGeometry(QtCore.QRect(270, 50, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.edit_resultado.setFont(font)
        self.edit_resultado.setObjectName("edit_resultado")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(10, 50, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_resultado.setObjectName("label_resultado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor de monedas"))
        self.boton_convertir_dolares.setText(_translate("MainWindow", "Convertir a Dolares"))
        self.boton_convertir_yenes.setText(_translate("MainWindow", "Convertir a Yenes"))
        self.label.setText(_translate("MainWindow", "Cantidad en Euros:"))
