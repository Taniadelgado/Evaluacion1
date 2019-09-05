#Tania Delgado - Anyely Gomez
#Evaluación Nro. 1 - Pensamiento computacional

import os
from random import randint, uniform, random

players=[]
juego=[]
suma = 0
n = 0
op = 0
ganar = False
con = 0

def nivel(op):
    if op==1:
        return 20
    elif op==2:
        return 30
    elif op==3:
        return 50

def dados():
    d1 = randint(1,6)
    d2 = randint(1,6)
    suma = d1 + d2
    
    print("\n:::LANZAMIENTO DE DADOS:::\n")
    uno = input("Presione 1 para lanzar los dados: ")
    
    print("\nDado 1 =  {}".format(d1))
    print("Dado 2 =  {}".format(d2))
    print("\nLa suma de los dados es: {}".format(suma))    

    return suma


def player(cantidad):
    for i in range (1,cantidad+1):
        players.append(i)


    
def tablero(n):
    for i in range(0,n):
        juego.append([players[i],0])

os.system("cls")
print("    :::CARRERA NUMERICA:::\n")
print("\t2 - Jugadores")
print("\t3 - Jugadores")
print("\t4 - Jugadores")
n = input("\nDigite la cantidad de jugadores: ")
while n<2 or n>4:
    print("El numero ingresado es incorrecto...")
    n = input("\nDigite la cantidad de jugadores: ")

player(n)

print("\n:::NIVEL DE TABLERO:::\n")
print("1. Nivel basico(Tablero de 20 posiciones)")
print("2. Nivel intermedio(Tablero de 30 posiciones)")
print("3. Nivel avanzado(Tablero de 50 posiciones)\n")
op = input("Digite el nivel que desea jugar: ")
while op<1 or op>3:
    print("El numero ingresado es incorrecto...")
    op = input("\nDigite el nivel que desea jugar: ")

opcion = nivel(op)
print("\nTablero de {}".format(nivel(op))+" opciones\n")
tablero(n)

while ganar==False:
    print("\n:::COMIENZA EL JUEGO:::\n")
    for i in range(0,len(juego)):
        print("\nTurno del jugador: {}".format(juego[i][0]))
        juego[i][1]=dados()+juego[i][1]
        print("\nEl jugador se encuentra en la poscicion: {}".format(juego[i][1]))
        if juego[i][1]>=opcion:
            ganar=True
            print("Ha ganado el jugador {}".format(juego[i][0])+"\n")
            break