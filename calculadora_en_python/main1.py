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

    def click_numero(pantalla: Text, valor: str):
        pantalla.insert(END, valor)
        return

    def __init__(self, ventana: Tk):
        self.ventana = ventana

        self.ventana.title = "Calculadora"

        # La ventana tendrá una cuadrícula de 6 x 4

        self.pantalla = Text(self.ventana)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=10)
        self.boton_1 = Button(self.ventana, text="1", command=lambda: self.click_numero(self.pantalla, "1"))
        self.boton_1.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_2 = Button(self.ventana, text="2", command=lambda: self.click_numero(self.pantalla, "2"))
        self.boton_2.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_3 = Button(self.ventana, text="3", command=lambda: self.click_numero(self.pantalla, "3"))
        self.boton_3.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_suma = Button(self.ventana, text="+")
        self.boton_suma.grid(row=1, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_4 = Button(self.ventana, text="4", command=lambda: self.click_numero(self.pantalla, "4"))
        self.boton_4.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_5 = Button(self.ventana, text="5", command=lambda: self.click_numero(self.pantalla, "5"))
        self.boton_5.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_6 = Button(self.ventana, text="6", command=lambda: self.click_numero(self.pantalla, "6"))
        self.boton_6.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        self.boton_resta = Button(self.ventana, text="-")
        self.boton_resta.grid(row=2, column=3, padx=5, pady=5, ipadx=5, ipady=5)



        return


    def operar(self):
        pass

##### MAIN #####

ventana: Tk = Tk()
calculadora: Calculadora = Calculadora(ventana)
ventana.mainloop()
