import random
import re


def obtener_bola(importe):
    bola = random.randint(0, 4)

    print("EL GASTO ES SUPERIOR O IGUAL A 100€ Y POR LO TANTO PARTICIPA EN LA PROMOCION")
    print("            COLOR                DESCUENTO")
    print("")
    print("            BOLA BLANCA          SIN DESCUENTO")
    print("            BOLA ROJA            10% DE DESCUENTO")
    print("            BOLA AZUL            20% DE DESCUENTO")
    print("            BOLA VERDE           25% DE DESCUENTO")
    print("            BOLA AMARILLA        50% DE DESCUENTO")
    print("")

    if bola == 0:
        print("HAS OBTENIDO EN EL SORTEO LA BOLA BLANCA, NO TIENES DESCUENTO.")
    elif bola == 1:
        print("HAS OBTENIDO EN EL SORTEO LA BOLA ROJA, TIENES UN 10% DE DESCUENTO.")
        importe *= 0.9
    elif bola == 2:
        print("HAS OBTENIDO EN EL SORTEO LA BOLA AZUL, TIENES UN 20% DE DESCUENTO.")
        importe *= 0.8
    elif bola == 3:
        print("HAS OBTENIDO EN EL SORTE LA BOLA VERDE, TIENES UN 25% DE DESCUENTO.")
        importe *= 0.75
    elif bola == 4:
        print("HAS OBTENIDO EN EL SORTEO LA BOLA AMARILLA, TIENES UN 50% DE DESCUENTO.")
        importe *= 0.5
    print(("EL IMPORTE TOTAL DE LA COMPRA ES {:.2f}".format(importe)).replace(".", ",") + "€.")


# MAIN #
patron = re.compile(r"^\d+\.\d+|\d+$")
salir = False
while not salir:
    str_importe = ""
    importe = 0.0
    while not patron.match(str_importe.replace(",", ".")):
        str_importe = input("INDICA EL IMPORTE DE LA COMPRA: ")
        if not patron.match(str_importe.replace(",", ".")):
            print("\n**** Debe ser un importe correcto. ****\n")
        else:
            importe = float(str_importe.replace(",", "."))
    if importe >= 100:
        obtener_bola(importe)
    else:
        print("EL GASTO NO LLEGA A 100€, POR LO QUE NO PARTICIPA EN EL SORTEO.")
        print(("EL IMPORTE TOTAL DE LA COMPRA ES {:.2f}".format(importe)).replace(".", ",") + "€.")
    print("")
    continuar = input("SI DESEA SALIR PULSE 1, PARA CONTINUAR INTRODUZCA CUALQUIER OTRA COSA.")
    if continuar == "1":
        salir = True
