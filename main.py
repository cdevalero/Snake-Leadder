import time
import random
import sys

#constantes 
TIEMPO_DE_ESPERA = 1            
META = 100
MAX_DADO = 12         #numero maximo que puede sacar el dado (6), dos dados (12)
MIN_DADO = 2            #numero minimo que puede sacar el dado (1), dos daos (2)

#casillas serpientes
serpientes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    76: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

cambio = [50 ,25, 75]

escaleras = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

def ganador(nombre_jugador, posicion):
    time.sleep(TIEMPO_DE_ESPERA)
    if posicion >= META:
        print("\n\n\n\n\n" + nombre_jugador + " GANO EL JUEGO")
        print("\n FELICITACIONES " + nombre_jugador)
        sys.exit(1)

def escalerasSerpientes(nombre_jugador, posicion_jugador, dado):
    time.sleep(TIEMPO_DE_ESPERA)
    posicion_actual = posicion_jugador
    posicion_obtenida = posicion_jugador + dado

    print("\n" + nombre_jugador + " esta en  " + str(posicion_obtenida))

    if posicion_obtenida in serpientes:
        posicion_final = serpientes.get(posicion_obtenida)
        print("\n" + nombre_jugador + " Se lo comio una serpiente, ahora esta en  " + str(posicion_final))

    elif posicion_obtenida in escaleras:
        posicion_final = escaleras.get(posicion_obtenida)
        print("\n" + nombre_jugador + " Subio una escalera, ahora esta " + str(posicion_final))

    else:
        posicion_final = posicion_obtenida

    return posicion_final

#Rol del dado
def get_dadoValor():
    time.sleep(TIEMPO_DE_ESPERA)
    dado_obtenido = random.randint(MIN_DADO, MAX_DADO)
    print(str(dado_obtenido))           #Muestra el valor del dado obtenido
    return dado_obtenido

#Turno del jugador
def turno(nombre, posicion):
    time.sleep(TIEMPO_DE_ESPERA)
    input_1 = input("\n" + nombre + ": " + " Lanza el dado ")            #imput para gira el dado
    dado_obtenido = get_dadoValor()
    time.sleep(TIEMPO_DE_ESPERA)
    posicion = escalerasSerpientes(nombre, posicion, dado_obtenido)
    ganador(nombre, posicion)
    return posicion

#Asigna nombre a los jugadores
def definirJugadores():
    J1 = "Amarillo"
    J2 = "Azul"
    J3 = "Rojo"
    J4 = "Blanco"
    return J1, J2, J3, J4

def Mensaje_inicioPartida():
    mensaje = """
    La partida acaba de iniciar.
    
    """
    print(mensaje)

#Funcion de inicio de la partida
def inicioPartida():
    Mensaje_inicioPartida()             #Mensaje de consola que lanza al inicar partida
    time.sleep(TIEMPO_DE_ESPERA)
    J1_nombre, J2_nombre, J3_nombre, J4_nombre = definirJugadores() #Definiendo jugadores (nombre)
    time.sleep(TIEMPO_DE_ESPERA)

    J1_posicion = 0
    J2_posicion = 0
    J3_posicion = 0
    J4_posicion = 0

    sentido = 1

    while True:
        J1_posicion = turno(J1_nombre, J1_posicion)
        J2_posicion = turno(J2_nombre, J2_posicion)
        J3_posicion = turno(J3_nombre, J3_posicion)
        J4_posicion = turno(J4_nombre, J4_posicion)


#Inicio de la aplicacion
if __name__ == "__main__":
    inicioPartida()