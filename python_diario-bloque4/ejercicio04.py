'''
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. Muestra por
pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de
interés introducida. Recordar que un capital C dolares a un interés del x por cien durante n años se convierte
C * (1 + x/100)elevado a n (años).
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés
anual se convierte en 24117.14 dolares al cabo de 20 años.
'''

##### IMPORTS #####
import re


##### FUNCIONES #####
def tomar_capital():
    expresion = "^([0-9]+\.[0-9]+|[0-9]+|)$"
    capital = 0.0

    while capital == 0:
        capital_temp: str = input("Dime el capital: ")
        if re.match(expresion, capital_temp) is not None:
            if float(capital_temp) > 0:
                capital = float(capital_temp)
            else:
                print("El capital debe ser un número mayor que cero.")
        else:
            print("\nEl capital debe ser un número")

    return capital


def tomar_interes():
    expresion = "^([0-9]+\.[0-9]+|[0-9]+)$"
    interes = 0.0

    while interes == 0:
        interes_temp = input("Dime el interes: ")
        if re.match(expresion, interes_temp) is not None:
            if float(interes_temp) > 0:
                interes = float(interes_temp)
            else:
                print("El interes debe ser un número mayor que cero.")
        else:
            print("\nEl interes debe ser un número")

    return interes


def tomar_anyos():
    anyos = 0

    while anyos == 0:
        anyos_temp = input("Dime los años: ")
        if anyos_temp.isdigit():
            if float(anyos_temp) >= 0:
                anyos = int(anyos_temp)
            else:
                print("Los años debe ser un número mayor que cero.")
        else:
            print("\nLos años deben ser un número entero")

    return anyos


##### MAIN #####
capital = tomar_capital()
interes = tomar_interes()
anyos = tomar_anyos()

total = capital * (1 + interes / 100) ** anyos

print("El capital total será: " + str(round(total, 2)))
