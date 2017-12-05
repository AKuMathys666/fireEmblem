import pygame
from pygame.locals import *
from random import *
from caracter import *
from copy import *
from itertools import permutations

def alphaBeta(player,opponent, A=-999, B=999):

    return(player,opponent)

def eval(playerBefore,opponentBefore,playerNow,opponentNow):

    return 0

def anyoneWin(player,opponent):
    sumPlayerHP=getSumHp(player)
    if sumPlayerHP==0:
        return 1    #Opponent(IA) win
    sumOpponentHP=opponent
    if sumOpponentHP==0:
        return -1   #Player win
    return 0        #No win yet

def getSumHp(listeCharacter):
    sumHP=0
    for item in listeCharacter:
        sumHP+=item[2].getHp()
    return sumHP

def makeTree(player,opponent,turn=1):
    feuille =(player,opponent,turn)
    tree=[]
    if turn ==1:
        tree = children(feuille)
    else:
        for item in tree:
            item = children(item)
    return tree

def alive(listCharacter):
    nbAlive=0
    alive = []
    for item in listCharacter:
        if item[2].getHp()!=0:
            alive.append(item)
            nbAlive+=1
    return nbAlive,alive

def children(feuille):
    player=feuille[0][:]
    opponent=feuille[1][:]


    
#def getPermutation(playerAlive,countPlayerAlive):
#    permutation=[]
#    if countPlayerAlive ==4 :
#1234
#1243
#1324
#1342
#1423
#1432
#2134
#2143
#2314
#2341
#2413
#2431
#3124
#3142
#3214
#3241
#3412
#3421
#4123
#4132
#4213
#4231
#4312
#4321
# !4 alternatives
#feuille => mvt perso 1 => atk perso 1 => mvt perso 2 => atk perso 2 => mvt perso 3 => atk perso 3 => mvt perso 4 => atk perso 4

