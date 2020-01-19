import pygame                                               #Libreria pygame, debe estar previamente instaldada
from pygame.locals import *

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
escoger_tablero = pygame.image.load("imagenes/boton_escoger.png")
cuadro = pygame.image.load("imagenes/cuadro.png")

# Fuente
pygame.font.init()
fuente = pygame.font.Font(None, 40)
fuente2 = pygame.font.Font(None, 30)
fuente3 = pygame.font.Font(None, 80)
fuente5 = pygame.font.Font(None, 200)

# Pantalla Menu de inicio
inicio = pygame.display.set_mode((900,400))                 #Dimension de la pantalla de inicio

inicio.blit(fondo_juego, (0,0))
inicio.blit(logo_juego, (20,0))
inicio.blit(boton_servidor_juego, (550,25))
inicio.blit(boton_buscar_partida, (550,150))
inicio.blit(boton_empezar, (550,275))