##### IMPORTS #####
import re
from tkinter import Tk, Text, Button, END


##### CLASES #####
class Calculadora():
    ventana = Tk()
    texto_pantalla = Text()
    boton_0 = Button()
    boton_1 = Button()
    boton_2 = Button()
    boton_3 = Button()
    boton_4 = Button()
    boton_5 = Button()
    boton_6 = Button()
    boton_7 = Button()
    boton_8 = Button()
    boton_9 = Button()
    boton_0 = Button()
    boton_decimal = Button()
    boton_resultado = Button(9)
    boton_borrar = Button()
    boton_suma = Button()
    boton_resta = Button()
    boton_multiplicacion = Button()
    boton_division = Button()

    numero1 = None
    numero2 = None
    operador = ""
    operacion_pendiente = False

    def operar(self, num1, num2, ope):
        if ope == "suma":
            resultado = num1 + num2
        elif ope == "resta":
            resultado = num1 - num2
        elif ope == "multiplicación":
            resultado = num1 * num2
        elif ope == "division":
            resultado = num1 / num2
        if type(resultado) == "float":
            res_temp = str(resultado)
            if not re.match(r"\d\.[0]+", res_temp):
                res = float(res_temp)
            else:
                res = int(res_temp)
        else:
            res = int(resultado)
        return res

    # end operar

    def click_resultado(self):
        num1 = self.numero1
        num2 = self.numero2
        ope = self.operador

        if ope == "suma":
            resultado = num1 + num2
        elif ope == "resta":
            resultado = num1 - num2
        elif ope == "multiplicación":
            resultado = num1 * num2
        elif ope == "division":
            resultado = num1 / num2
        if type(resultado) == "float":
            res_temp = str(resultado)
            if not re.match(r"\d\.[0]+", res_temp):
                res = float(res_temp)
            else:
                res = int(res_temp)
        else:
            res = int(resultado)
        self.pantalla.delete(0)
        self.pantalla.insert(0, str(res))
        self.numero1 = 0
        self.numero2 = 0
        self.operador = ""
        self.operacion_pendiente = False

    # end click_resultado

    def click_numero(self, valor):
        if valor != ".":
            self.pantalla.insert(END, valor)
        else:
            if "." not in self.pantalla.get():
                self.pantalla.insert(END, valor)

    # end click_numero

    def click_operador(self, valor: str):
        numero1 = 0
        operador = valor

    # end click_operador

    def __init__(self, parametro_ventana: Tk):
        self.ventana = parametro_ventana
        self.ventana.title = "Calculadora"

        # La ventana tendrá una cuadrícula de 6 x 4

        self.pantalla = Text(self.ventana)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=10)
        self.boton_1 = Button(self.ventana, text="1", command=lambda: self.click_numero("1"))
        self.boton_1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_2 = Button(self.ventana, text="2", command=lambda: self.click_numero("2"))
        self.boton_2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_3 = Button(self.ventana, text="3", command=lambda: self.click_numero("3"))
        self.boton_3.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_suma = self.Button(self.ventana, text="+")
        self.boton_suma.grid(row=1, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_4 = Button(self.ventana, text="4", command=lambda: self.click_numero("4"))
        self.boton_4.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_5 = Button(self.ventana, text="5", command=lambda: self.click_numero("5"))
        self.boton_5.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_6 = Button(self.ventana, text="6", command=lambda: self.click_numero("6"))
        self.boton_6.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_resta = Button(self.ventana, text="-")
        self.boton_resta.grid(row=2, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_7 = Button(self.ventana, text="7", command=lambda: self.click_numero("7"))
        self.boton_7.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_8 = Button(self.ventana, text="5", command=lambda: self.click_numero("8"))
        self.boton_8.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_9 = Button(self.ventana, text="6", command=lambda: self.click_numero("9"))
        self.boton_9.grid(row=3, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_multiplicacion = Button(self.ventana, text="x")
        self.boton_multiplicacion.grid(row=3, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_0 = Button(self.ventana, text="7", command=lambda: self.click_numero("0"))
        self.boton_0.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_decimal = Button(self.ventana, text=".", command=lambda: self.click_numero("."))
        self.boton_decimal.grid(row=3, column=3, padx=5, pady=5, ipadx=5, ipady=5)

    # end constructor


##### MAIN #####

ventana: Tk = Tk()
calculadora: Calculadora = Calculadora(ventana)
ventana.mainloop()
