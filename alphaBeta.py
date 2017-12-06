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
    sumOpponentHP=getSumHp(opponent)
    if sumOpponentHP==0:
        return -1   #Player win
    return 0        #No win yet

def getSumHp(listeCharacter):
    sumHP=0
    for item in listeCharacter:
        sumHP+=item[2].getHp()
    return sumHP

def makeRandomLeaf(player,opponent,myMap):
    feuille =(player[:],opponent[:])
    playerToMove = list(range(len(opposant)))
    listAction=[]
    while playerToMove :
        selectedPlayer = choice(playerToMove)
        listAction.append(selectedPlayer)
        
        listMovePosible=movePossible(feuille,selectedPlayer,myMap)
        selectedMove = choice(list(range(len(listMovePosible))))
        feuille[1][selectedPlayer][1]=listMovePosible[selectedMove] #make move
        
        listAtkPosible=atkPossible(feuille,selectedPlayerToMove,myMap)
        selectAtk = choice(list(range(len(listAtkPosible))))
        attak()#make an attak

        
        

    
def movePossible(feuille,move,myMap):
#prendre cordonné du joueur, prendre les case autour valide, appliquer a nouveau movepossible tant que mouvement!=0
#recuper la liste des coordonné, factoriser les doublon et retourner cette liste




    
#feuille => mvt perso 1 => atk perso 1 => mvt perso 2 => atk perso 2 => mvt perso 3 => atk perso 3 => mvt perso 4 => atk perso 4

