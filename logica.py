import time
import random
import sys
import logicaTablero            #Logica de los tableros posibles
import graficos
import pygame

#constantes 
TIEMPO_DE_ESPERA = 0.1            
META = 100
MAX_DADO = 6           #numero maximo que puede sacar el dado (6), dos dados (12)
MIN_DADO = 1            #numero minimo que puede sacar el dado (1), dos daos (2)

#Objeto Jugador
class jugador:
    nombre = ""
    posicion = 1
    estado = False

class tableroJuego:
    nombre = 0
    giro = logicaTablero.giro
    serpientes = logicaTablero.serpientes
    escaleras = logicaTablero.escaleras

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
    if jugador.posicion == META:
        graficos.inicio.blit(graficos.fondo_juego, (0,0))
        if (jugador.nombre == "Naranja"):
            puntuacion = graficos.fuente5.render(jugador.nombre +" !!!!! GANADOR !!!!!",0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(100,100))
        if (jugador.nombre == "Rojo"):
            puntuacion = graficos.fuente5.render(jugador.nombre +" !!!!! GANADOR !!!!!",0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(100,100))
        if (jugador.nombre == "Azul"):
            puntuacion = graficos.fuente5.render(jugador.nombre +" !!!!! GANADOR !!!!!",0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(100,100))
        if (jugador.nombre == "Blanco"):
            puntuacion = graficos.fuente5.render(jugador.nombre +" !!!!! GANADOR !!!!!",0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(100,100))
        pygame.display.update()
        time.sleep(10)
        sys.exit(1)

#Verifica si un jugadr ha caido en una escalera o serpiente y realiza la operacion
def escalerasSerpientes(jugador, dado, tablero):
    time.sleep(TIEMPO_DE_ESPERA)
    posicion_actual = jugador.posicion
    posicion_obtenida = jugador.posicion + dado

    if posicion_obtenida > META:
        return posicion_actual

    if (jugador.nombre == "Naranja"):
        puntuacion = graficos.fuente.render(str(posicion_obtenida),0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(65,130))
    if (jugador.nombre == "Rojo"):
        puntuacion = graficos.fuente.render(str(posicion_obtenida),0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(170,130))
    if (jugador.nombre == "Azul"):
        puntuacion = graficos.fuente.render(str(posicion_obtenida),0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(275,130))
    if (jugador.nombre == "Blanco"):
        puntuacion = graficos.fuente.render(str(posicion_obtenida),0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(380,130))

    if posicion_obtenida in tablero.serpientes:
        posicion_final = tablero.serpientes.get(posicion_obtenida)
        if (jugador.nombre == "Naranja"):
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(65,130))
            puntuacion = graficos.fuente2.render(jugador.nombre + " Se lo comio una serpiente, bajo a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(65,180))
        if (jugador.nombre == "Rojo"):
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(170,130))
            puntuacion = graficos.fuente2.render(jugador.nombre + " Se lo comio una serpiente, bajo a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(25,180))
        if (jugador.nombre == "Azul"):
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(275,130))
            puntuacion = graficos.fuente2.render(jugador.nombre + " Se lo comio una serpiente, bajo a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(25,180))
        if (jugador.nombre == "Blanco"):
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(380,130))
            puntuacion = graficos.fuente2.render(jugador.nombre + " Se lo comio una serpiente, bajo a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(25,180))

    elif posicion_obtenida in tablero.escaleras:
        posicion_final = tablero.escaleras.get(posicion_obtenida)
        if (jugador.nombre == "Naranja"):
            nombre = graficos.fuente2.render(jugador.nombre + " Subio una escalera, subio a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(nombre,(65,180))
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(65,130))
        if (jugador.nombre == "Rojo"):
            nombre = graficos.fuente2.render(jugador.nombre + " Subio una escalera, subio a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(nombre,(25,180))
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(170,130))
        if (jugador.nombre == "Azul"):
            nombre = graficos.fuente2.render(jugador.nombre + " Subio una escalera, subio a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(nombre,(25,180))
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(275,130))
        if (jugador.nombre == "Blanco"):
            nombre = graficos.fuente2.render(jugador.nombre + " Subio una escalera, subio a " + str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(nombre,(25,180))
            puntuacion = graficos.fuente.render(str(posicion_final),0,(0,0,0),(255,255,255))
            graficos.inicio.blit(puntuacion,(380,130))

    else:
        posicion_final = posicion_obtenida

    return posicion_final

#Rol del dado
def get_dadoValor():
    dado_obtenido = random.randint(MIN_DADO, MAX_DADO)
    if dado_obtenido == 1:
        graficos.inicio.blit(graficos.dado_1,(37,225))
    elif dado_obtenido == 2:
        graficos.inicio.blit(graficos.dado_2,(37,225))
    elif dado_obtenido == 3:
        graficos.inicio.blit(graficos.dado_3,(37,225))
    elif dado_obtenido == 4:
        graficos.inicio.blit(graficos.dado_4,(37,225))
    elif dado_obtenido == 5:
        graficos.inicio.blit(graficos.dado_5,(37,225))
    elif dado_obtenido == 6:
        graficos.inicio.blit(graficos.dado_6,(37,225))
    return dado_obtenido

#Cambia el sentido de la partida 
def cambio(jugador, turno_jugador, sentido, tablero):
    if jugador.posicion in tablero.giro:
        if sentido == 0:
            turno_jugador = horario.get(turno_jugador)
        if sentido == 1:
            turno_jugador = antiHorario.get(turno_jugador)
        nombre = graficos.fuente3.render(str(sentido),0,(0,0,0),(255,255,255))
        graficos.inicio.blit(nombre,(810,20))
        if (sentido == 0):
            sentido = 1 
        elif (sentido == 1):
            sentido = 0
        return (turno_jugador, sentido)
    if sentido == 1:
        return (turno_jugador - 1), sentido
    return (turno_jugador + 1), sentido

#Turno del jugador
def turno(jugador, tablero):
    clik = pygame.mouse.get_pos()
    time.sleep(TIEMPO_DE_ESPERA)
    if (clik[0] > 262 and clik[0] < 450 and clik[1] > 225 and clik[1] < 400):
        dado_obtenido = get_dadoValor()

    #Revisa si el jugador esta maccado para poder jugar correctamente
    if (jugador.estado == True and dado_obtenido != 6):
        nombre = graficos.fuente2.render("Quemado saca 6 para volver a jugar",0,(255,255,0),(0,0,0))
        graficos.inicio.blit(nombre,(25,180))
        return jugador.posicion
    elif (jugador.estado == True and dado_obtenido == 6):
        jugador.estado = False
    
    #Si saca 6 vuelve a jugar, si saca 6, 3 veces vuleve a la casilla 1
    if dado_obtenido == 6:
        nombre = graficos.fuente2.render("Doblete",0,(0,0,255),(0,0,0))
        graficos.inicio.blit(nombre,(25,180))
        dado_extra = get_dadoValor()
        dado_obtenido = dado_obtenido + dado_extra 
        
        if dado_extra == 6:
            #input_1 = input("\n" + jugador.nombre + ": " + " Lanza el dado ") 
            dado_extra = get_dadoValor()
            dado_obtenido = dado_obtenido + dado_extra
            nombre = graficos.fuente2.render("Triplete",0,(0,0,255),(0,0,0))
            graficos.inicio.blit(nombre,(25,180))
            if dado_extra == 6:
                nombre = graficos.fuente2.render("Quemado saca 6 para volver a jugar",0,(255,255,0),(255,255,255))
                graficos.inicio.blit(nombre,(25,180))
                jugador.estado = True
                jugador.posicion = 1
                return jugador.posicion
    time.sleep(TIEMPO_DE_ESPERA)
    jugador.posicion = escalerasSerpientes(jugador, dado_obtenido, tablero)
    ganador(jugador)
    return jugador.posicion

#Escoge cual de los 6 tableros va a usar en funcion de en numero que salga en el dado
def definirTablero():
    #input_1 = input("\nLanza el dado para escoger que tablero se va a jugar") 
    dado_obtenido = get_dadoValor()
    tablero = tableroJuego()
    if dado_obtenido == 1:
        tablero.nombre = 1
        tablero.giro = logicaTablero.giro1
        tablero.escaleras = logicaTablero.escaleras1
        tablero.serpientes = logicaTablero.serpientes1
    elif dado_obtenido == 2:
        tablero.nombre = 2
        tablero.giro = logicaTablero.giro2
        tablero.escaleras = logicaTablero.escaleras2
        tablero.serpientes = logicaTablero.serpientes2
    elif dado_obtenido == 3:
        tablero.nombre = 3
        tablero.giro = logicaTablero.giro3
        tablero.escaleras = logicaTablero.escaleras3
        tablero.serpientes = logicaTablero.serpientes3
    elif dado_obtenido == 4:
        tablero.nombre = 4
        tablero.giro = logicaTablero.giro4
        tablero.escaleras = logicaTablero.escaleras4
        tablero.serpientes = logicaTablero.serpientes4
    elif dado_obtenido == 5:
        tablero.nombre = 5
        tablero.giro = logicaTablero.giro5
        tablero.escaleras = logicaTablero.escaleras5
        tablero.serpientes = logicaTablero.serpientes5
    elif dado_obtenido == 6:
        tablero.nombre = 6
        tablero.giro = logicaTablero.giro6
        tablero.escaleras = logicaTablero.escaleras6
        tablero.serpientes = logicaTablero.serpientes6
    return tablero

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

#Funcion de inicio de la partida
def play(turno_para_jugar, sentido, J1, J2, J3, J4, tablero):
    if turno_para_jugar == 1:
        J1.posicion= turno(J1, tablero)
        turno_para_jugar, sentido = cambio(J1, turno_para_jugar, sentido, tablero)
    elif turno_para_jugar == 2:
        J2.posicion= turno(J2, tablero)
        turno_para_jugar, sentido = cambio(J2, turno_para_jugar, sentido, tablero)
    elif turno_para_jugar == 3:
        J3.posicion= turno(J3, tablero)
        turno_para_jugar, sentido = cambio(J3, turno_para_jugar, sentido, tablero)
    elif turno_para_jugar == 4:
        J4.posicion= turno(J4, tablero)
        turno_para_jugar, sentido = cambio(J4, turno_para_jugar, sentido, tablero)

    elif turno_para_jugar == 5:
        turno_para_jugar = 1
    elif turno_para_jugar == 0:
        turno_para_jugar = 4

    return turno_para_jugar, sentido