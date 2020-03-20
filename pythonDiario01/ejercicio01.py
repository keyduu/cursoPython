#Reino del Dragon....
import random
import time

puntos = 0

def introduccion():
    print ("Estamos en una tierra llena de dragones. Delante de nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    print ("y compartira el tesoro contigo. El otro dragon")
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print ("")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("Ha que cueva quieres entrar? 1 o 2?")
        cueva = input()
       
    return cueva

def cheqcueva(CambiarCueva):
    global puntos
    
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)
   
    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print ("Te entrega el tesoro...")
        # Añade 100 puntos a la puntuación.
        puntos += 100
    else:
        print ("El dragon te come de un bocado....")
        # Imprime la puntuación y pone puntos a 0 para empezar de nuevo.
        print("Tu puntuación es: " + str(puntos))
        puntos = 0
        

EmpezarNuevo = ("si")

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
   
    introduccion()
   
    NumCaverna = CambiarCueva()
   
    cheqcueva(NumCaverna)
   
    print ("Quieres jugar de nuevo? (si o no)")
    EmpezarNuevo = input()
