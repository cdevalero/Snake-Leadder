import pygame                                               #Libreria pygame, debe estar previamente instaldada
import sys
import logica
import time
import random
import sys
import graficos
from pygame.locals import *

#inicializacion de pygame, para la visualizacion de ventanas
pygame.init()

def pantalla_3(turno, sentido, j1, j2, j3 ,j4, tablero):
    turno, sentido = logica.play(turno, sentido, j1, j2, j3 ,j4, tablero)
    return turno, sentido


def pantalla_2():
    clik = pygame.mouse.get_pos()
    time.sleep(logica.TIEMPO_DE_ESPERA)
    if (clik[0] > 550 and clik[0] <750 and clik[1] > 275 and clik[1] <375):
        tablero = logica.definirTablero()
        graficos.inicio.blit(graficos.fondo_juego, (0,0))
        if (tablero.nombre == 1):
            graficos.inicio.blit(graficos.tablero_1,(500,25))
        if (tablero.nombre == 2):
            graficos.inicio.blit(graficos.tablero_2,(500,25))
        if (tablero.nombre == 3):
            graficos.inicio.blit(graficos.tablero_3,(500,25))
        if (tablero.nombre == 4):
            graficos.inicio.blit(graficos.tablero_4,(500,25))
        if (tablero.nombre == 5):
            graficos.inicio.blit(graficos.tablero_5,(500,25))
        if (tablero.nombre == 6):
            graficos.inicio.blit(graficos.tablero_6,(500,25))
        graficos.inicio.blit(graficos.j_naranja,(26,26))
        graficos.inicio.blit(graficos.J_rojo,(132,26))
        graficos.inicio.blit(graficos.J_azul,(238,26))
        graficos.inicio.blit(graficos.j_blanco,(344,26))
        graficos.inicio.blit(graficos.boton_jugar,(262,225))
        puntuacion = graficos.fuente.render("1",0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(65,130))
        puntuacion = graficos.fuente.render("1",0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(170,130))
        puntuacion = graficos.fuente.render("1",0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(275,130))
        puntuacion = graficos.fuente.render("1",0,(0,0,0),(255,255,255))
        graficos.inicio.blit(puntuacion,(380,130))
        return 3, tablero

def pantalla_1():
    clik = pygame.mouse.get_pos()
    time.sleep(logica.TIEMPO_DE_ESPERA)
    if   (clik[0] > 550 and clik[0] < 750 and clik[1] > 25 and clik[1] <125):  # Servidor
        graficos.inicio.blit(graficos.fondo_juego, (0,0))
        graficos.inicio.blit(graficos.mini_t1, (100,5))
        graficos.inicio.blit(graficos.mini_t2, (100,135))
        graficos.inicio.blit(graficos.mini_t3, (100,265))
        graficos.inicio.blit(graficos.mini_t4, (240,5))
        graficos.inicio.blit(graficos.mini_t5, (240,135))
        graficos.inicio.blit(graficos.mini_t6, (240,265))
        graficos.inicio.blit(graficos.escoger_tablero, (550,275)) 
        # envia la trama
        return 2
    elif (clik[0] > 550 and clik[0] < 750 and clik[1] > 150 and clik[1] <250): # Cliente
        # espera la trama
        return 3; 
    elif (clik[1] > 275 and clik[1] <375 and clik[0] > 550 and clik[0] < 750):  # Juego. PUEDE QUE NO ME INTERESE ESTE BOTON    
        graficos.inicio.blit(graficos.fondo_juego, (0,0))
        graficos.inicio.blit(graficos.mini_t1, (100,5))
        graficos.inicio.blit(graficos.mini_t2, (100,135))
        graficos.inicio.blit(graficos.mini_t3, (100,265))
        graficos.inicio.blit(graficos.mini_t4, (240,5))
        graficos.inicio.blit(graficos.mini_t5, (240,135))
        graficos.inicio.blit(graficos.mini_t6, (240,265))
        graficos.inicio.blit(graficos.escoger_tablero, (550,275)) 
        return 2
    return 1


def empezarPartida():
    turno_para_jugar = 1
    sentido = 0
    ventana = 1
    J1, J2, J3, J4 = logica.definirJugadores()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:                             #detecta cuando el usuario le da a la X en el programa
                pygame.quit()
                sys.exit()
        if (ventana == 3  and pygame.mouse.get_pressed() == (1,0,0)):
            turno_para_jugar, sentido = pantalla_3(turno_para_jugar, sentido, J1, J2, J3, J4, tablero)
        elif (ventana == 2  and pygame.mouse.get_pressed() == (1,0,0)):
            ventana, tablero = pantalla_2()
        elif (ventana == 1  and pygame.mouse.get_pressed() == (1,0,0)):
            ventana = pantalla_1()
        pygame.display.update()            


#Inicio de la aplicacion
if __name__ == "__main__":
    empezarPartida()