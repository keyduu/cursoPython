'''
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir
que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''


#####################
##### FUNCIONES #####
#####################
## Para verificar que las palabras son correctas, para ello tienen que estar compuestas solo por letras y además
# tener más de 3 letras.
def verificar_palabra(palabra):
    if len(palabra) <= 3:
        print("\n### La palabra " + palabra + " debe tener más de 3 letras. ###\n")
        return False
    if not palabra.isalpha():
        print("\n### La palabra " + palabra + " debe con tener solo letras. ###\n")
        return False
    return True


################
##### MAIN #####
################

palabra1 = ""
palabra2 = ""

palabra1_ok = False
palabra2_ok = False

# El bucle es para asegurar que la palabra esz valida.
while not palabra1_ok:
    palabra1 = input("Dime la primera palabra: ")
    palabra1_ok = verificar_palabra(palabra1)
# El bucle es para asegurar que la palabra esz valida.
while not palabra2_ok:
    palabra2 = input("Dime la segunda palabra: ")
    palabra2_ok = verificar_palabra(palabra2)

if palabra1[-3:] == palabra2[-3:]:
    print("La palabra tiene rima completa.")
elif palabra1[-2:] == palabra2[-2:]:
    print("Las palabra riman solo un poco.")
else:
    print("Las palabras no riman.")
