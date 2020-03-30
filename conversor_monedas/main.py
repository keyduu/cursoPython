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


# ==== FUNCIONES ==== #
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
ui.boton_convertir_dolares.clicked.connect(transformar_a_dolares)
ui.boton_convertir_yenes.clicked.connect(transformar_a_yenes)

# se muestra la ventana principal de PyQt5
MainWindow.show()
sys.exit(app.exec_())
