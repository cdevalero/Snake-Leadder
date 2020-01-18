import time
import random
import sys
import logicaTablero            #Logica de los tableros posibles

#constantes 
TIEMPO_DE_ESPERA = 1            
META = 100
MAX_DADO = 6           #numero maximo que puede sacar el dado (6), dos dados (12)
MIN_DADO = 1            #numero minimo que puede sacar el dado (1), dos daos (2)

#Objeto Jugador
class jugador:
    nombre = ""
    posicion = 1
    estado = False

# Sentido que puede tomar el juego horario (1,2,3,4)
horario = {
    1: 4,
    2: 1,
    3: 2,
    4: 3
}

# Sentido que puede tomar el juego amti-horario (4,3,2,1)
antiHorario = {
    1: 2,
    2: 3,
    3: 4,
    4: 1
}

#Busca si el jugador cumple las condiciones para ganar la partida
def ganador(jugador):
    time.sleep(TIEMPO_DE_ESPERA)
    if jugador.posicion = META:
        print("\n\n\n\n\n" + jugador.nombre + " GANO EL JUEGO")
        print("\n FELICITACIONES " + jugador.nombre)
        sys.exit(1)

#Verifica si un jugadr ha caido en una escalera o serpiente y realiza la operacion
def escalerasSerpientes(jugador, dado):
    time.sleep(TIEMPO_DE_ESPERA)
    posicion_actual = jugador.posicion
    posicion_obtenida = jugador.posicion + dado

    if posicion_obtenida > MAX_DADO:
        print("Necesitas " + str(MAX_DADO - posicion_actual) + " Para Ganar")
        return posicion_actual

    print("\n" + jugador.nombre + " esta en  " + str(posicion_obtenida))

    if posicion_obtenida in logicaTablero.serpientes:
        posicion_final = logicaTablero.serpientes.get(posicion_obtenida)
        print("\n" + jugador.nombre + " Se lo comio una serpiente, ahora esta en  " + str(posicion_final))

    elif posicion_obtenida in logicaTablero.escaleras:
        posicion_final = logicaTablero.escaleras.get(posicion_obtenida)
        print("\n" + jugador.nombre + " Subio una escalera, ahora esta " + str(posicion_final))

    else:
        posicion_final = posicion_obtenida

    return posicion_final

#Rol del dado
def get_dadoValor():
    time.sleep(TIEMPO_DE_ESPERA)
    dado_obtenido = random.randint(MIN_DADO, MAX_DADO)
    print("Dado: " + str(dado_obtenido) )           #Muestra el valor del dado obtenido
    return dado_obtenido

#Cambia el sentido de la partida 
def cambio(jugador, turno_jugador, sentido):
    if jugador.posicion in logicaTablero.giro:
        if sentido == 1:
            turno_jugador = horario.get(turno_jugador)
        if sentido == 2:
            turno_jugador = antiHorario.get(turno_jugador)
        print("\n !!!Cambio de sentido!!! ")
        if (sentido == 1):
            sentido = 2 
        elif (sentido == 2):
            sentido = 1
        return (turno_jugador, sentido)
    if sentido == 2:
        return (turno_jugador - 1), sentido
    return (turno_jugador + 1), sentido

#Turno del jugador
def turno(jugador):
    time.sleep(TIEMPO_DE_ESPERA)
    input_1 = input("\n" + jugador.nombre + ": " + " Lanza el dado ")            #imput para gira el dado
    dado_obtenido = get_dadoValor()

    #Revisa si el jugador esta maccado para poder jugar correctamente
    if (jugador.estado == True and dado_obtenido != 6):
        print("\n Tienes que sacar 6 para poder volver a jugar \n")
        print("\n" + jugador.nombre + " esta en  " + str(jugador.posicion))
        return jugador.posicion
    elif (jugador.estado == True and dador_obtenido == 6):
        jugador.estado = False

    #Si saca 6 vuelve a jugar, si saca 6, 3 veces vuleve a la casilla 1
    if dado_obtenido == 6:
        input_1 = input("\n" + jugador.nombre + ": " + " Lanza el dado ") 
        dado_extra = get_dadoValor()
        dado_obtenido = dado_obtenido + dado_extra 
        print("\n las suma de los dados es " + str(dado_obtenido))
        if dado_extra == 6:
            input_1 = input("\n" + jugador.nombre + ": " + " Lanza el dado ") 
            dado_extra = get_dadoValor()
            dado_obtenido = dado_obtenido + dado_extra
            print("\n las suma de los dados es " + str(dado_obtenido))
            if dado_extra == 6:
                print("\n Jugador " + jugador.nombre + " Marcado, saca 6 para segir jugando")
                print("\n" + jugador.nombre + " esta en  " + str(jugador.posicion))
                jugador.estado = True
                jugador.posicion = 1
                return jugador.posicion

    time.sleep(TIEMPO_DE_ESPERA)
    jugador.posicion = escalerasSerpientes(jugador, dado_obtenido)
    ganador(jugador)
    return jugador.posicion

#Asigna nombre a los jugadores
def definirJugadores():
    J1 = jugador()
    J1.nombre = "Naranja"
    J2 = jugador()
    J2.nombre = "Rojo"
    J3 = jugador()
    J3.nombre = "Azul"
    J4 = jugador()
    J4.nombre = "Blanco"
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
    J1, J2, J3, J4 = definirJugadores() #Definiendo jugadores
    time.sleep(TIEMPO_DE_ESPERA)

    turno_para_jugar = 1
    sentido = 1

    while True:

        if turno_para_jugar == 1:
            J1.posicion= turno(J1)
            turno_para_jugar, sentido = cambio(J1, turno_para_jugar, sentido)
        if turno_para_jugar == 2:
            J2.posicion= turno(J2)
            turno_para_jugar, sentido = cambio(J2, turno_para_jugar, sentido)
        if turno_para_jugar == 3:
            J3.posicion= turno(J3)
            turno_para_jugar, sentido = cambio(J3, turno_para_jugar, sentido)
        if turno_para_jugar == 4:
            J4.posicion= turno(J4)
            turno_para_jugar, sentido = cambio(J4, turno_para_jugar, sentido)

        if turno_para_jugar == 5:
            turno_para_jugar = 1
        if turno_para_jugar == 0:
            turno_para_jugar = 4

#Inicio de la aplicacion
if __name__ == "__main__":
    inicioPartida()