##### IMPORTS #####
import re
from tkinter import Tk, Entry, Button, END, EW


##### CLASES #####
class Calculadora():
    ventana = Tk()
    texto_pantalla = Entry()
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
    boton_resultado = Button()
    boton_borrar = Button()
    boton_suma = Button()
    boton_resta = Button()
    boton_multiplicacion = Button()
    boton_division = Button()

    numero1 = 0.0 # Las operaciones se harán siempre con float, si es entero despues se formateará para mostrarlo correctamente.
    numero2 = 0.0
    operador = "" # Suma = +, resta = -, multiplicación = *, división = / 
    operacion_pendiente = False # Para comprobar si es la primera vez que se pulsa un botón de operación.


    def obtener_numero(self):
    # Obtiene el número de la pantalla y lo convierte a float.
        numero_texto = self.pantalla.get()
        numero_texto = numero_texto.replace(",", ".") # Remplaza la coma por punto para que se convierta correctamente en float.
        return float(numero_texto)
    # end obtener_numero

   
    def numero_a_texto(self, numero):
         # Formatea un número para presentarlo correctamente en la pantalla.
        patron_int = re.compile(r"\d\.[0]+")

        numero = round(numero, 6) # redondeo a 6 decimales para evitar problemas de precisión

        texto = str(numero)
        if patron_int.match(texto): # Si es un entero, lo muestra como entero
            resultado = "{:d}".format(texto)
        else: # Si no es entero lo muestra como float.
            resultado = "{:f".format(texto)
        resultado = resultado.replace(".", ",") # Sustituye los puntos por comas para mostrarlo en el formato habitual en España.

        return resultado
    # end numero_a_texto

    def operar(self, num1, num2, ope):
        if ope == "+":
            resultado = num1 + num2
        elif ope == "-":
            resultado = num1 - num2
        elif ope == "*":
            resultado = num1 * num2
        elif ope == "/":
            resultado = num1 / num2
        return resultado
    # end operar

#     def click_resultado(self):
#         num1 = self.numero1
#         num2 = self.numero2
#         ope = self.operador
# 
#         resultado = self.operar(self.numero1, self.numero2, self.operador)
# 
#         if ope == "suma":
#             resultado = num1 + num2
#         elif ope == "resta":
#             resultado = num1 - num2
#         elif ope == "multiplicación":
#             resultado = num1 * num2
#         elif ope == "division":
#             resultado = num1 / num2
#         if type(resultado) == "float":
#             res_temp = str(resultado)
#             if not re.match(r"\d\.[0]+", res_temp):
#                 res = float(res_temp)
#             else:
#                 res = int(res_temp)
#         else:
#             res = int(resultado)
#         self.pantalla.delete(0)
#         self.pantalla.insert(0, str(res))
#         self.numero1 = 0
#         self.numero2 = 0
#         self.operador = ""
#         self.operacion_pendiente = False
# 
#     # end click_resultado

    def click_borrar(self):
        self.pantalla.delete(0, END)
        self.pantalla.insert(0, "0")

    def click_numero(self, valor):
        if valor == ",":
            if valor not in self.pantalla.get(): # Cuando ya hay una coma y se pulsa de nuevo coma, no hace nada, si no añade la coma.
                self.pantalla.insert(END, valor)
        elif valor == "0":
            if self.pantalla.get() != "0": # Si la pantalla solo tiene 0 y se pulsa 0, no hace nada, si no, añade 0.
                self.pantalla.insert(END, valor)
        else:
            if self.pantalla.get() == "0": # Si la pantalla solo tiene 0, se borra para añadir el número pulsado.
                self.pantalla.delete(0, END)
            self.pantalla.insert(END, valor)
    # end click_numero

    def click_operador(self, valor):
        num1 = 0.0
        operador = valor
        if self.operacion_pendiente:
            self.numero2 = self.obtener_numero()
        else:
            self.numero1 = self.obtener_numero()

        if operador == "resultado":
            self.operar(self.numero1, self.numero2, self.operador)
        else:
            pass

    # end click_operador

    def __init__(self, parametro_ventana: Tk):
        self.ventana = parametro_ventana
        self.ventana.title = "Calculadora"

        # La ventana tendrá una cuadrícula de 6 x 4

        self.pantalla = Entry(self.ventana)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=10)
        self.boton_1 = Button(self.ventana, text="1", command=lambda: self.click_numero("1"))
        self.boton_1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_2 = Button(self.ventana, text="2", command=lambda: self.click_numero("2"))
        self.boton_2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_3 = Button(self.ventana, text="3", command=lambda: self.click_numero("3"))
        self.boton_3.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_suma = Button(self.ventana, text="+")
        self.boton_suma.grid(row=1, column=3, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_4 = Button(self.ventana, text="4", command=lambda: self.click_numero("4"))
        self.boton_4.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_5 = Button(self.ventana, text="5", command=lambda: self.click_numero("5"))
        self.boton_5.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_6 = Button(self.ventana, text="6", command=lambda: self.click_numero("6"))
        self.boton_6.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_resta = Button(self.ventana, text="-")
        self.boton_resta.grid(row=2, column=3, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_7 = Button(self.ventana, text="7", command=lambda: self.click_numero("7"))
        self.boton_7.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_8 = Button(self.ventana, text="8", command=lambda: self.click_numero("8"))
        self.boton_8.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_9 = Button(self.ventana, text="9", command=lambda: self.click_numero("9"))
        self.boton_9.grid(row=3, column=2, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_multiplicacion = Button(self.ventana, text="x")
        self.boton_multiplicacion.grid(row=3, column=3, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_0 = Button(self.ventana, text="0", command=lambda: self.click_numero("0"))
        self.boton_0.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_decimal = Button(self.ventana, text=",", command=lambda: self.click_numero(","))
        self.boton_decimal.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, columnspan = 2, sticky=EW)
        self.boton_division = Button(self.ventana, text=u"\u00F7")
        self.boton_division.grid(row=4, column=3, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        self.boton_resultado = Button(self.ventana, text="=")
        self.boton_resultado.grid(row=5, column=0, padx=5, pady=5, ipadx=5, ipady=5, columnspan=3, sticky=EW)
        self.boton_borrar = Button(self.ventana, text="\u232B", command=self.click_borrar)
        self.boton_borrar.grid(row=5, column=3, padx=5, pady=5, ipadx=5, ipady=5, sticky=EW)
        
        self.pantalla.insert(END, "0") # Inicializa la pantalla a 0.
    # end constructor

##### MAIN #####


ventana: Tk = Tk()
calculadora: Calculadora = Calculadora(ventana)
ventana.mainloop()
