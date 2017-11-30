import pygame
from pygame.locals import *
from random import *

def getArrayPos(anyArray,number):
	arrayreturn = []
	for i,line in enumerate(anyArray):
		for j,val in enumerate(line):
			if val == number:
				arrayreturn.append([i*90,j*90])
	return arrayreturn

def samePos(x,y,player,opponent):
	valReturn = True
	for item in player :
		if item[1].top/90== x:
			if item[1].left/90== y:
				valReturn = False #Joueur sur la case ciblé
	for item in opponent :
		if item[1].top/90== x:
			if item[1].left/90== y:
				valReturn = False # Enemie sur la case ciblé
	return valReturn
	
def deplacementValide(x,y,map,player,opponent,type_deplacement):
	
	if type_deplacement==0:#Infanterie
		if map[x][y] in (0,3,6,7):
			return samePos(x,y,player,opponent)
	elif type_deplacement==1:#Cavalier
		if map[x][y] in (0,6,7):
			return samePos(x,y,player,opponent)
	elif type_deplacement==2:#Flier
		if map[x][y] in (0,2,3,6,7):
			return samePos(x,y,player,opponent)
	else:#Tank
		if map[x][y] in (0,3,6,7):
			return samePos(x,y,player,opponent)
	return False
	
def getFond(aleatoire):
	if aleatoire==0:
		fond = pygame.image.load("img/Maps/S0102.png").convert()
		print("S0102")
	if aleatoire==1:
		fond = pygame.image.load("img/Maps/S0305.png").convert()
		print("S0305")
	if aleatoire==2:
		fond = pygame.image.load("img/Maps/S0405.png").convert()
		print("S0405")
	if aleatoire==3:
		fond = pygame.image.load("img/Maps/S0504.png").convert()
		print("S0504")
	if aleatoire==4:
		fond = pygame.image.load("img/Maps/S1401.png").convert()
		print("S1401")
	if aleatoire==5:
		fond = pygame.image.load("img/Maps/X0022.png").convert()
		print("X0022")
	if aleatoire==6:
		fond = pygame.image.load("img/Maps/X0081.png").convert()
		print("X0081")
	if aleatoire==7:
		fond = pygame.image.load("img/Maps/S0202.png").convert()
		print("S0202")
	if aleatoire==8:
		fond = pygame.image.load("img/Maps/S0502.png").convert()
		print("S0502")
	return fond
	