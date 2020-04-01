from tkinter import *
from os import path
import time  # @NoMove
import re


######################
# Variables globales #
######################
inicio = 0
fin = 0
nombre = ""
adivinadas = []
diferencias = [[525, 563, 109, 136],
               [616, 651, 48, 77],
               [798, 823, 102, 122],
               [636, 665, 168, 181],
               [818, 848, 199, 213]]


#######################
# Funciones generales #
#######################
# Funcion auxiliar: permite ordenar por tiempos en la funcion
# obtener_puntuaciones()
def obtener_tiempo(elemento):
    # Obtengo el segundo elemento y lo transformo en float y lo devuelvo.
    return float(elemento[1])


def obtener_puntuaciones():
    # Si no existe el fichero, lo crea.
    if not path.isfile("puntuacion.txt"):
        fichero = open("puntuacion.txt", "w")
        fichero.close()
    fichero = open("puntuacion.txt", "r")
    lista_puntuaciones = []
    # Lee línea a línea el fichero y introduce cada línea en una lista
    # cada elemento de la lista tendrá 2 elementos, el nombre y el tiempo.
    for linea in fichero:
        elemento = linea.split(";")
        lista_puntuaciones.append(elemento)
    # ordeno la lista por los tiempos obtenidos.
    lista_puntuaciones.sort(key = obtener_tiempo)
    return lista_puntuaciones
# end obtener_puntuaciones()


# Escribe la puntuacion en el fichero de puntuaciones, lo añade al final.
def escribir_puntuacion(nombre, tiempo):
    fichero = open("puntuacion.txt", "a")
    linea = nombre + ";" + str(tiempo) + "\n"
    fichero.write(linea)
    fichero.close
# end escribir_puntuacion()


def comprobar_diferencia(x, y):
    global diferencias, adivinadas

    adivinada = False
    repetida = False

    # Se recorren las diferencias para comprobar si las coordenadas se encuentra
    # en alguna de las diferencias.
    for i in range(len(diferencias)):
        # Se comprueba si está dentro de la diferencia.
        if (diferencias[i][0] <= x <= diferencias[i][1]
            and diferencias[i][2] <= y <= diferencias[i][3]):
            # No se ha pinchado anteriormente.
            if i not in adivinadas:
                # No es la última diferencia.
                if len(adivinadas) < len(diferencias) - 1:
                    # Se añade a las diferencias ya pinchadas.
                    adivinadas.append(i)
                    messagebox.showinfo("Acertaste", "Enhorabuena, has " +
                                        "encontrado una diferencia.\nTe " +
                                        "quedan por encontrar " +
                                        str(len(diferencias) -
                                            len(adivinadas)))
                    adivinada = True
                    # Se sale del bucle, ya no es necesario comprobar el resto
                    # de diferencias.
                    break
                else:
                    # Última diferencia marcada
                    # Se toma el tiempo de fin
                    fin = time.time()
                    # Se redondea para que tenga solo 4 decimales.
                    tiempo = round(fin - inicio, 4)
                    messagebox.showinfo("Fin del juego", "Has acertado todas."
                                        +"\nTiempo que has tarﬁdado: "
                                        +str(tiempo) + " segundos.")
                    adivinada = True
                    # Se graba en el archivo.
                    escribir_puntuacion(nombre, tiempo)
                    # Se cierra la ventana principal y termina el juego.
                    ventana_principal.destroy()
            else:
                # Ya se había pinchado anteriormente
                repetida = True
                # Se sale del bulce porque no es necesario comprobar el resto
                # de las diferencias.
                break
    if repetida:
        # Diferencia ya marcada.
        messagebox.showwarning("Repetida", "Esa diferencia ya la habías " +
                               "descubierto!")
    elif not adivinada:
        # Click fuera de las diferencias.
        messagebox.showwarning("Fallo", "No es una diferencia.")
# end comprobar_diferencias()


#######################
# Funciones de evento #
#######################
def click_raton(evento):
    global inicio

    x = evento.x
    y = evento.y

    if inicio == 0:
        inicio = time.time()

    comprobar_diferencia(x, y)
# end click_raton()


def click_acceder():
    global nombre

    # Expresxión regular para comprobar si el nombre es válido.
    expresion = "[a-zA-Z0-9\.\-]"
    # Se obtiene el texto del cuadro de texto.
    temp_nombre = entry_nombre.get()
    # Comprueba si el nombre está vacío.
    if temp_nombre != "":
        # Se comprueba el nombre con la expresión regular.
        correcto = re.match(expresion, temp_nombre)
        if correcto:
            nombre = temp_nombre
            ventana_nombre.destroy()
        else:
            # No es un nombre válido
            messagebox.showerror("Error", "Nombre no válido.\n" +
                                "El nombre solo admite, números " +
                                "letras, el caracter punto y el " +
                                "caracter guión.")
    else:
        # Nombre vacío
        messagebox.showerror("Error", "El nombre no puede estar en blanco.")
# end click_acceder()

##################
###### Main ######
##################


# los nombres y puntuaciones del fichero.
lista_puntuaciones = obtener_puntuaciones()

ventana_nombre = Tk()
# Muestra un mensaje con las instrucciones.
messagebox.showinfo("Como jugar", "En primer lugar, se debe indicar el "
                    +"nombre, despues se mostrará una imagen con otra "
                    +"imagen igual salvo por 5 diferencias. Se deben "
                    +"hacer click en las 5 diferencias para coger el "
                    +"tiempo y registrarlo.")

# Se crean los elementos de la primera ventana.
label_nombre = Label(ventana_nombre, text = "Tu nombre:")
label_nombre.grid(row = 0, column = 0, padx = 5, pady = 5)
entry_nombre = Entry(ventana_nombre, textvariable = nombre)
entry_nombre.grid(row = 0, column = 1, padx = 5, pady = 5)
boton_acceder = Button(ventana_nombre, text = "Acceder", command = click_acceder)
boton_acceder.grid(row = 1, columnspan = 2, pady = 5)

# Se pinta la lista de tiempos
encabezado_a_label = Label(ventana_nombre, text = "Nombre", borderwidth = 2)
encabezado_a_label.grid(row = 2, column = 0)
encabezado_b_label = Label(ventana_nombre, text = "Tiempo", borderwidth = 2)
encabezado_b_label.grid(row = 2, column = 1)
for i in range(len(lista_puntuaciones)):
    # muestra un máximo de 10 tiempos, que serán los 10 mejores.
    if i == 10:
        break
    indice = i + 4
    a = Entry(ventana_nombre)
    a.insert(0, lista_puntuaciones[i][0])
    a.grid(row = indice, column = 0, padx = 5)
    b = Entry(ventana_nombre)
    b.insert(0, lista_puntuaciones[i][1])
    b.grid(row = indice, column = 1, padx = 5)
ventana_nombre.mainloop()

# Se pinta la ventana principal.
ventana_principal = Tk()
ventana_principal.geometry("920x350")
canvas = Canvas(ventana_principal, width = 920, height = 350)
imagen = PhotoImage(file ="imagen.png")
canvas.create_image(0, 0, image = imagen, anchor = NW)
canvas.bind("<Button 1>", click_raton)
canvas.pack(expand = YES, fill = BOTH)
ventana_principal.mainloop()
