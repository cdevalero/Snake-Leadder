import pygame                                               #Libreria pygame, debe estar previamente instaldada
import sys

from pygame.locals import *

#Colores de las fichas
naranja = pygame.Color(255,164,32)
rojo = pygame.Color(255,0,0)
azul = pygame.Color(0,0,255)
blanco = pygame.Color(255,255,255)

pygame.display.set_caption("Escaleras y serpientes")

# Imagens del juego
fondo_juego = pygame.image.load("imagenes/fondo.png")
logo_juego = pygame.image.load("imagenes/logo.png")
boton_servidor_juego = pygame.image.load("imagenes/boton_servidor.png")
boton_buscar_partida = pygame.image.load("imagenes/boton_buscar_partida.png")
boton_empezar = pygame.image.load("imagenes/boton_empezar.png")
dado_1 = pygame.image.load("imagenes/Dado_1.png")
dado_2 = pygame.image.load("imagenes/Dado_2.png")
dado_3 = pygame.image.load("imagenes/Dado_3.png")
dado_4 = pygame.image.load("imagenes/Dado_4.png")
dado_5 = pygame.image.load("imagenes/Dado_5.png")
dado_6 = pygame.image.load("imagenes/Dado_6.png")
boton_jugar = pygame.image.load("imagenes/boton_jugar.png")
boton_esperar = pygame.image.load("imagenes/boton_esperar.png")
J_azul = pygame.image.load("imagenes/jugador_AZUL.png")
J_rojo = pygame.image.load("imagenes/jugador_ROJO.png")
j_naranja = pygame.image.load("imagenes/jugador_NARANJA.png")
j_blanco = pygame.image.load("imagenes/jugador_BLANCO.png")
mini_t1 = pygame.image.load("imagenes/Tablero_1_mini.png")
mini_t2 = pygame.image.load("imagenes/Tablero_2_mini.png")
mini_t3 = pygame.image.load("imagenes/Tablero_3_mini.png")
mini_t4 = pygame.image.load("imagenes/Tablero_4_mini.png")
mini_t5 = pygame.image.load("imagenes/Tablero_5_mini.png")
mini_t6 = pygame.image.load("imagenes/Tablero_6_mini.png")
tablero_1 = pygame.image.load("imagenes/Tablero_1.png")
tablero_2 = pygame.image.load("imagenes/Tablero_2.png")
tablero_3 = pygame.image.load("imagenes/Tablero_3.png")
tablero_4 = pygame.image.load("imagenes/Tablero_4.png")
tablero_5 = pygame.image.load("imagenes/Tablero_5.png")
tablero_6 = pygame.image.load("imagenes/Tablero_6.png")

#inicializacion de pygame, para la visualizacion de ventanas
pygame.init()

# Pantalla Menu de inicio
inicio = pygame.display.set_mode((900,400))                 #Dimension de la pantalla de inicio

inicio.blit(fondo_juego, (0,0))
inicio.blit(logo_juego, (20,0))
inicio.blit(boton_servidor_juego, (550,25))
inicio.blit(boton_buscar_partida, (550,150))
inicio.blit(boton_empezar, (550,275))

# Pantalla escoger tablero

#pantalla_tablero = pygame.display.set_mode((900,400))

#pantalla_tablero.blit(fondo_juego, (0,0))
#pantalla_tablero.blit(mini_t1, (100,5))
#pantalla_tablero.blit(mini_t2, (100,135))
#pantalla_tablero.blit(mini_t3, (100,265))
#pantalla_tablero.blit(mini_t4, (240,5))
#pantalla_tablero.blit(mini_t5, (240,135))
#pantalla_tablero.blit(mini_t6, (240,265))


while True:
    # inicio.fill(blanco)
    for evento in pygame.event.get():
        if evento.type == QUIT:                             #detecta cuando el usuario le da a la X en el programa
            pygame.quit()
            sys.exit()
    pygame.display.update()                                 #Refresco de la ventana 