##### IMPORTS #####
from tkinter import Tk, Text, Button, END

##### FUNCIONES


##### CLASES #####
class Calculadora():
    ventana: Tk
    texto_pantalla: Text
    boton_0: Button
    boton_1: Button
    boton_2: Button
    boton_3: Button
    boton_4: Button
    boton_5: Button
    boton_6: Button
    boton_7: Button
    boton_8: Button
    boton_9: Button
    boton_0: Button
    boton_decimal: Button
    boton_resultado: Button
    boton_borrar: Button
    boton_suma: Button
    boton_resta: Button
    boton_multiplicacion: Button
    boton_division: Button
    
    numero1
    numero2

    def operar(self):
        pass
    #end operar

    def click_numero(valor: str):
        if valor != "."
            pantalla.insert(END, valor)
        else:
            if "." not in pantalla.get():
                pantalla.insert(END, valor)
    #end click_numero
                
    
    def click_operador(self, valor: str):
        numero1 = 
        operador = valor
    #end click_operador

    def __init__(self, parametro_ventana: Tk):
        ventana = parametro_ventana
        ventana.title = "Calculadora"

        # La ventana tendrá una cuadrícula de 6 x 4

        pantalla = Text(ventana)
        pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=10)
        boton_1 = Button(ventana, text="1", command=lambda: click_numero("1"))
        boton_1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        boton_2 = Button(ventana, text="2", command=lambda: click_numero("2"))
        boton_2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        boton_3 = Button(ventana, text="3", command=lambda: click_numero("3"))
        boton_3.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        boton_suma = Button(ventana, text="+")
        boton_suma.grid(row=1, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        boton_4 = Button(ventana, text="4", command=lambda: click_numero("4"))
        boton_4.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        boton_5 = Button(ventana, text="5", command=lambda: click_numero("5"))
        boton_5.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        boton_6 = Button(ventana, text="6", command=lambda: click_numero("6"))
        boton_6.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        boton_resta = Button(ventana, text="-")
        boton_resta.grid(row=2, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        boton_7 = Button(ventana, text="7", command=lambda: click_numero(pantalla, "7"))
        boton_7.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        boton_8 = Button(ventana, text="5", command=lambda: click_numero(pantalla, "8"))
        boton_8.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        boton_9 = Button(ventana, text="6", command=lambda: click_numero(pantalla, "9"))
        boton_9.grid(row=3, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        boton_multiplicacion = Button(ventana, text="x")
        boton_multiplicacion.grid(row=3, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        boton_0 = Button(ventana, text="7", command=lambda: click_numero(pantalla, "0"))
        boton_0.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_decimal = Button(self.ventana, text=".", command=lambda: click_numero(pantalla, "."))
        self.boton_decimal.grid(row=3, column=3, padx=5, pady=5, ipadx=5, ipady=5)
       
    #end constructor




##### MAIN #####

ventana: Tk = Tk()
calculadora: Calculadora = Calculadora(ventana)
ventana.mainloop()
