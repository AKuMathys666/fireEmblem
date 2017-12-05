import pygame
from pygame.locals import *
from random import *
from caracter import *
from copy import *

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
    if turn ==1:
        tree=[]
        nbPlayer,playerAlive = alive(player)
        tree.append(getPermutation(playerAlive))))
        for item in tree:
            print(item[2].display())
    return 0

def alive(listCharacter):
    nbAlive=0
    alive = []
    for item in listCharacter:
        if item[2].getHp()!=0:
            alive.append(item)
            nbAlive+=1
    return nbAlive,alive

def getPermutation(playerAlive):
    permutation=[]
    countPlayerAlive = len(playerAlive)
    if countPlayerAlive ==4 :
        


            
