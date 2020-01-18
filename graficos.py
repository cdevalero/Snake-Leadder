import pygame                                               #Libreria pygame, debe estar previamente instaldada
import sys

from pygame.locals import *

#Colores de las fichas
naranja = pygame.Color(255,164,32)
rojo = pygame.Color(255,0,0)
azul = pygame.Color(0,0,255)
blanco = pygame.Color(255,255,255)


#inicializacion de pygame, para la visualizacion de ventanas
pygame.init()
inicio = pygame.display.set_mode((900,400))                 #Dimension de la pantalla de inicio
pygame.display.set_caption("Escaleras y serpientes")        #Nombre de la ventana
pygame.draw.rect(inicio, azul, (425,175,50,50))
pygame.draw.line(inicio,(255,255,255),(450,0),(450,400))
pygame.draw.line(inicio,(255,255,255),(0,200),(900,200))


while True:
    # inicio.fill(blanco)
    for evento in pygame.event.get():
        if evento.type == QUIT:                             #detecta cuando el usuario le da a la X en el programa
            pygame.quit()
            sys.exit()
    pygame.display.update()                                 #Refresco de la ventana 