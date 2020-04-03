'''
# +Sobre la actual aplicacion. Incorporar 1 boton para transformar los euros introducidos
# a otra moneda a elegir por el programador.
# + Incorporar un boton más para tranformar a otro tipo de moneda distinto
# + Mostrar un icono en el boton correspondiente de conversion

'''

# ==== IMPORTS ==== #
import sys

from PyQt5 import QtWidgets

from conversor_monedas.ventanas import ventana_python

# ==== VARIABLES GLOBALES ==== #


conversion_dolares = 1.11
conversion_yenes = 119.15
conversion_libras = 0.88
conversion_rublos = 82.92
conversion_bitcoins = 0.00016


# ==== FUNCIONES ==== #
def click_borrar():
    ui.edit_euros.setText("0,00")
    ui.grupo_botones.setExclusive(False)
    ui.boton_convertir_bitcoins.setChecked(False)
    ui.boton_convertir_yenes.setChecked(False)
    ui.boton_convertir_dolares.setChecked(False)
    ui.boton_convertir_libras.setChecked(False)
    ui.boton_convertir_rublos.setChecked(False)
    ui.grupo_botones.setExclusive(True)
    ui.label_resultado.setText("")
    ui.edit_resultado.setText("")


def click_radio_button():
    if ui.boton_convertir_dolares.isChecked():
        transformar_a_dolares()
    elif ui.boton_convertir_yenes.isChecked():
        transformar_a_yenes()
    elif ui.boton_convertir_libras.isChecked():
        transformar_a_libras()
    elif ui.boton_convertir_rublos.isChecked():
        transformar_a_rublos()
    elif ui.boton_convertir_bitcoins.isChecked():
        transformar_a_bitcoins()


def transformar_a_dolares():
    introducido = ui.edit_euros.text()
    introducido_float = float(introducido.replace(",", "."))
    dolares = introducido_float * conversion_dolares
    ui.label_resultado.setText("Cantidad(dolares): ")
    ui.edit_resultado.setText("{:.2f}".format(dolares).replace(".", ","))


def transformar_a_yenes():
    introducido = ui.edit_euros.text()
    introducido_float = float(introducido.replace(",", "."))
    yenes = introducido_float * conversion_yenes
    ui.label_resultado.setText("Cantidad(yenes): ")
    ui.edit_resultado.setText("{:.2f}".format(yenes).replace(".", ","))


def transformar_a_libras():
    introducido = ui.edit_euros.text()
    introducido_float = float(introducido.replace(",", "."))
    libras = introducido_float * conversion_libras
    ui.label_resultado.setText("Cantidad(libras): ")
    ui.edit_resultado.setText("{:.2f}".format(libras).replace(".", ","))

def transformar_a_rublos():
    introducido = ui.edit_euros.text()
    introducido_float = float(introducido.replace(",", "."))
    rublos = introducido_float * conversion_rublos
    ui.label_resultado.setText("Cantidad(rublos): ")
    ui.edit_resultado.setText("{:.2f}".format(rublos).replace(".", ","))
def transformar_a_bitcoins():
    introducido = ui.edit_euros.text()
    introducido_float = float(introducido.replace(",", "."))
    bitcoins = introducido_float * conversion_bitcoins
    ui.label_resultado.setText("Cantidad(bitcoins): ")
    ui.edit_resultado.setText("{:.2f}".format(bitcoins).replace(".", ","))

# ==== MAIN ==== #

# vamos a usar el archivo generado de la ventana directamente

# linea obligatoria para usar pyqt5
app = QtWidgets.QApplication(sys.argv)

# se prepara un MainWindow de pyqt5, esto seria parte del codigo recomendado de pyqt5
MainWindow = QtWidgets.QMainWindow()

# asi crea un objeto de la clase en el archivo generado y lo usa para preparar la ventana principal
# llamada MainWindow para que tenga todo lo que pusimos en el designer
ui = ventana_python.Ui_MainWindow()
ui.setupUi(MainWindow)

# todos los componentes puestos en la ventana por el designer estan ui
ui.boton_convertir_dolares.toggled.connect(click_radio_button)
ui.boton_convertir_yenes.toggled.connect(click_radio_button)
ui.boton_convertir_libras.toggled.connect(click_radio_button)
ui.boton_convertir_rublos.toggled.connect(click_radio_button)
ui.boton_convertir_bitcoins.toggled.connect(click_radio_button)
ui.boton_borrar.clicked.connect(click_borrar)

# se muestra la ventana principal de PyQt5
MainWindow.show()
sys.exit(app.exec_())
