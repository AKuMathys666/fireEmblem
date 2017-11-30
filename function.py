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
	