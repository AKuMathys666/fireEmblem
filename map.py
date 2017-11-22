from random import *
import pygame
from pygame.locals import *
pygame.init()

#0 = Tout le monde
#2 = Flier
#3 = Tout sauf cavalier
#-1 = Personne
#6 = Case depart Joueur
#7 = Case depart Ordi

terrain_disponible=9
aleatoire=(choice(range(terrain_disponible)))


if aleatoire == 1:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/S0102.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[0,0,0,0,0,0], 
           [0,0,0,0,0,2],
           [0,0,2,0,0,2],
           [0,3,2,0,7,7],
           [0,2,0,0,7,7],
           [6,2,0,0,0,0],
           [6,3,2,2,2,2],
           [0,6,6,0,3,2]]

if aleatoire == 2:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/S0305.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[-1,-1,-1,-1,-1,-1], 
           [0,7,7,7,7,0],
           [0,0,0,0,0,0],
           [-1,0,0,0,0,-1],
           [0,0,0,0,0,0],
           [-1,0,0,0,0,-1],
           [0,0,0,0,0,0],
           [-1,6,6,6,6,-1]]

if aleatoire == 3:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/S0405.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[0,0,2,0,0,0], 
           [0,0,2,0,0,0],
           [0,2,2,0,0,0],
           [7,0,0,7,0,0],
           [7,0,7,0,2,0],
           [2,2,2,2,0,0],
           [0,0,0,0,0,0],
           [0,0,6,6,6,6]]

if aleatoire == 4:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/S0405.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[0,7,7,7,7,3], 
           [0,0,0,0,3,0],
           [0,0,0,0,0,3],
           [0,0,0,0,3,0],
           [0,0,0,0,0,0],
           [0,0,0,0,3,0],
           [0,0,0,0,3,0],
           [0,6,6,6,6,0]]

if aleatoire == 5:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/S1401.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[2,0,0,3,3,3], 
           [7,7,7,7,0,0],
           [0,3,0,3,0,0],
           [0,0,0,3,0,3],
           [0,0,0,0,0,0],
           [0,3,0,0,0,0],
           [0,0,0,0,6,6],
           [3,0,3,0,6,6]]

if aleatoire == 6:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/X0022.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[-1,-1,0,3,-1,0], 
           [0,0,0,0,-1,7],
           [0,0,7,0,0,0],
           [-1,-1,0,0,-1,7],
           [-1,-1,0,0,-1,0],
           [0,0,0,0,-1,-1],
           [3,0,0,0,0,0],
           [3,0,0,0,3,7]]

if aleatoire == 7:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/X0081.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[2,0,7,7,7,7], 
           [2,0,0,0,3,0],
           [2,2,2,0,0,0],
           [2,2,2,0,0,3],
           [2,2,2,0,0,0],
           [2,2,0,3,0,0],
           [2,0,0,0,0,0],
           [0,0,6,6,6,6]]

if aleatoire == 8:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/S0202.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[0,0,0,2,0,3], 
           [0,7,0,0,0,0],
           [7,0,0,2,0,6],
           [7,0,0,2,0,6],
           [0,7,2,2,0,6],
           [0,0,2,0,0,6],
           [0,0,0,0,0,0],
           [0,2,2,0,0,0]]


if aleatoire == 9:
    print(aleatoire)
    fenetre = pygame.display.set_mode((540,720),RESIZABLE)
    fond = pygame.image.load("img/Maps/S0502.png").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    t_map=[[-1,-1,-1,-1,-1,-1], 
           [7,7,-1,-1,7,7],
           [0,0,0,0,0,0],
           [0,0,-1,0,-1,0],
           [0,0,-1,-1,0,0],
           [0,0,-1,-1,0,0],
           [3,0,0,0,0,3],
           [6,6,0,0,6,6]]
