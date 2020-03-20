'''
Escribe un programa que te permita jugar a una versión simplificada del juego
Master Mind. El juego consistirá en adivinar una cadena de números distintos. Al
principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras).
Después el programa debe ir pidiendo que intentes adivinar la cadena de números.
En cada intento, el programa informará de cuántos números han sido acertados (el
programa considerará que se ha acertado un número si coincide el valor y la
posición).
'''
#################
#### IMPORTS ####
#################
import re
from random import randint


###################
#### FUNCIONES ####
###################
# Genera la cadena de forma aleatoria.
def generar_cadena(longitud):
    # Caracteres disponibles para generar la cadena, es para asegurar que no se
    # repiten.
    disponibles = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cadena = ""
    # Se toman de la lista disponibles tantos caracteres como longitud se
    # indique.
    for i in range(longitud):
        # Se toma un elemento aleatorio de la lista.
        pos_elemento = randint(0, len(disponibles) - 1)
        # El elemento tomado se quita de la lista y se concatena a la cadena a
        # crear.
        cadena += disponibles.pop(pos_elemento)
    return cadena
# end generar_numero(longitud)


# Comprueba si la cadena proporcionada es la misma que la cadena a adivinar.
# Tanto la cadena a adivinar como la cadena a probar, deben ser de la misma
# longitud.
def comprobar_cadena(cadena_a_probar, cadena_a_adivinar):
    # Para ver el número de coincidencias.
    contador = 0
    # Para comprobar si se ha acertado la cadena completa.
    longitud = len(cadena_a_adivinar)

    # Se recorren ambas cadenas completas.
    for i in range(longitud):
        # Si el caracter coincide, se aumenta el contador en 1
        if cadena_a_probar[i] == cadena_a_adivinar[i]:
            contador += 1
    # Si el contador es igual a la longitud de la cadena, se ha acertado.
    if contador == longitud:
        print("¡¡¡Has acertado la cadena!!!")
        return True
    else:
        print("Para la cadena " + prueba + " has acertado " + str(contador) +
              ".")
        return False
# end comprobar_cadena(prueba, cadena)


# Obtiene la cadena a probar.
def obtener_prueba(longitud):
    comparar = "^[0-9]{" + str(longitud) + "}$"
    prueba_ok = False

    # Repite hasta tener una prueba valida
    while not prueba_ok:
        repetidos = False
        usados = []
        prueba = input("Intenta adivinar la cadena: ")
        # Comprueba si se ha introducido una cadena válida
        if not re.match(comparar, prueba):
            print("\n#### La cadena deben tener exactamente " + str(longitud) +
              " números. ####\n")
        else:
            # comprueba si la cadena tiene elementos repetidos.
            for elemento in prueba:
                # Si elemento está en usados, está repetida
                if elemento in usados:
                    repetidos = True
                    print("\n#### La cadena no puede tener números repetidos. " +
                          "####\n")
                    # No hace falta comprobar el resto de elementos.
                    break
                else:
                    usados.append(elemento)
            # Se acepta la prueba si no está repetido ningun caracter.
            prueba_ok = not repetidos
    # end while
    return prueba
# end validar_prueba(prueba, longitud)


def obtener_longitud():
    # La longitud de la cadena a crear
    longitud = 0
    # Para validar que la longitud introducida sea correcta.
    comparacion = "^[2-9]$"
    # Repite hasta que se indique una longitud válida.
    while longitud == 0:
        # Lee del teclado la longitud.
        longitud_temp = input("Dime la longitud de la cadena: ")
        # Se comprueba si es sólo 1 número del 2 al 9 incluidos.
        if re.match(comparacion, longitud_temp):
            longitud = int(longitud_temp)
        else:
            print("\n#### Tienes que indicar un número del 2 al 9. ####\n")
    return longitud
# end obtener_longitud()


##############
#### MAIN ####
##############
# Para controlar cuando acaba el programa.
acertado = False

longitud = obtener_longitud()
cadena = generar_cadena(longitud)
while not acertado:
    prueba = obtener_prueba(longitud)
    acertado = comprobar_cadena(prueba, cadena)