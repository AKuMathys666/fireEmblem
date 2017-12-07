import pygame
from pygame.locals import *
from random import *
from caracter import *
from copy import *
from function import *
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

        cible=getEnemieToAttack(feuille[0],feuille[1][selectedPlayer])
        selectAtk = choice(list(range(len(cible)+1)))
        feuille[0][getCharName(feuille[0],cible[selectAtk][2].getName())],feuille[1][selectedPlayer]=attack(cible[selectAtk],feuille[1][selectedPlayer])
                                                    
        attak()#make an attak

        
        

#prendre cordonné du joueur, prendre les case autour valide, appliquer a nouveau movepossible tant que mouvement!=0
#recuper la liste des coordonné, factoriser les doublon et retourner cette liste
def movePossible(feuille,selectedPlayer,myMap):
    playerListAtPos=[]
    playerListAtPos.append(selectedPlayer)
    listPos=[]
    listPos.append(selectedPlayer[1])
    print("pos :",int((selectedPlayer[1].top+90)/90)," ",int((selectedPlayer[1].left)/90))
    for characters in playerListAtPos:
        mouvement=copy(characters[2].getMove())
        if mouvement > 0:
            character=[]
            character.append(pygame.Surface.copy(characters[0]))
            character.append(deepcopy(characters[1]))
            character.append(deepcopy(characters[2]))
            if character[1].top+90 < 720 :
                if deplacementValide(int((character[1].top+90)/90),int((character[1].left)/90),myMap,feuille[0],feuille[1],character[2].getTypeMove()):
                    if myMap[int((character[1].top+90)/90)][int((character[1].left)/90)]==3 and character[2].getTypeMove()=="Infanterie":
                        if mouvement-2 >=0:
                            character[1] = character[1].move(0,90)
                            character[2].moves-=2
                            if character[1] not in listPos:
                                listPos.append(character[1])
                                playerListAtPos.append(character)
                    else:
                        character[1] = character[1].move(0,90)
                        character[2].moves-=1
                        if character[1] not in listPos:
                            listPos.append(character[1])
                            playerListAtPos.append(character)
            character=[]
            character.append(pygame.Surface.copy(characters[0]))
            character.append(deepcopy(characters[1]))
            character.append(deepcopy(characters[2]))
            if character[1].top-90 >= 0 :
                if deplacementValide(int((character[1].top-90)/90),int((character[1].left)/90),myMap,feuille[0],feuille[1],character[2].getTypeMove()):
                    if myMap[int((character[1].top-90)/90)][int((character[1].left)/90)]==3 and character[2].getTypeMove()=="Infanterie":
                        if mouvement-2 >=0:
                            character[1] = character[1].move(0,-90)
                            character[2].moves-=2
                            if character[1] not in listPos:
                                listPos.append(character[1])
                                playerListAtPos.append(character)
                                mouvement-=2
                    else:
                        character[1] = character[1].move(0,-90)
                        character[2].moves-=1
                        if character[1] not in listPos:
                            listPos.append(character[1])
                            playerListAtPos.append(character)
            character=[]
            character.append(pygame.Surface.copy(characters[0]))
            character.append(deepcopy(characters[1]))
            character.append(deepcopy(characters[2]))
            if character[1].left+90 < 540 :
                if deplacementValide(int((character[1].top)/90),int((character[1].left+90)/90),myMap,feuille[0],feuille[1],character[2].getTypeMove()):
                    if myMap[int((character[1].top)/90)][int((character[1].left+90)/90)]==3 and character[2].getTypeMove()=="Infanterie":
                        if mouvement-2 >=0:
                            character[1] = character[1].move(90,0)
                            character[2].moves-=2
                            if character[1] not in listPos:
                                listPos.append(character[1])
                                playerListAtPos.append(character)
                                mouvement-=2
                    else:
                        character[1] = character[1].move(90,0)
                        character[2].moves-=1
                        if character[1] not in listPos:
                            listPos.append(character[1])
                            playerListAtPos.append(character)
            character=[]
            character.append(pygame.Surface.copy(characters[0]))
            character.append(deepcopy(characters[1]))
            character.append(deepcopy(characters[2]))
            if character[1].left-90 >= 0 :
                if deplacementValide(int((character[1].top)/90),int((character[1].left-90)/90),myMap,feuille[0],feuille[1],character[2].getTypeMove()):
                    if myMap[int((character[1].top)/90)][int((character[1].left-90)/90)]==3 and character[2].getTypeMove()=="Infanterie":
                        if mouvement-2 >=0:
                            character[1] = character[1].move(-90,0)
                            if character[1] not in listPos:
                                listPos.append(character[1])
                                playerListAtPos.append(character)
                                mouvement-=2
                    else:
                        character[1] = character[1].move(-90,0)
                        character[2].moves-=1
                        if character[1] not in listPos:
                            listPos.append(character[1])
                            playerListAtPos.append(character)
    for item in listPos:
        print(int((item.top+90)/90)," ",int((item.left)/90))
    for item in playerListAtPos:
        print(item[2].getMove())
    return listPos

    
#feuille => mvt perso 1 => atk perso 1 => mvt perso 2 => atk perso 2 => mvt perso 3 => atk perso 3 => mvt perso 4 => atk perso 4

