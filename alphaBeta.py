import pygame
from pygame.locals import *
from random import *
from caracter import *
from copy import *
from function import *
from itertools import permutations
import time



def evaluationIA(player,opponent,myMap):
    startNode=(player[:],opponent[:])
    currentBestAction=list()
    currentBestAction=makeRandomIALeaf(startNode[0],startNode[1],myMap)
    afterPlayerTurn=makeRandomPlayerLeaf(currentBestAction[-1][0],currentBestAction[-1][1],myMap)
    bestEval=eval(startNode[0],startNode[1],afterPlayerTurn[0],afterPlayerTurn[1])
    t_end = time.time() + 3 # 3 secondes de process
    nbIa=0
    nbPlayer=0
    while time.time() < t_end:
        newIaLeaf=list()
        newIaLeaf=makeRandomIALeaf(startNode[0],startNode[1],myMap)
        nbIa+=1
        currentEval=-9999
        for i in range(5):
            playerLeaf=makeRandomPlayerLeaf(newIaLeaf[-1][0],newIaLeaf[-1][1],myMap)
            nbPlayer+=1
            playerLeafEval=eval(startNode[0],startNode[1],playerLeaf[0],playerLeaf[1])
            if currentEval != max(currentEval,playerLeafEval):
                currentEval=max(currentEval,playerLeafEval)
        if bestEval != min(bestEval,currentEval):
            bestEval=min(bestEval,currentEval)
            currentBestAction=newIaLeaf
    return currentBestAction

def eval(playerBefore,opponentBefore,playerNow,opponentNow):
    playerTotalHpBefore=getSumHp(playerBefore)
    playerTotalHpAfter=getSumHp(playerNow)
    iATotalHpBefore=getSumHp(opponentBefore)
    iATotalHpAfter=getSumHp(opponentNow)
    if iATotalHpAfter==0:
        return 9999
    if playerTotalHpAfter==0:
        return -9999
    playerLose=playerTotalHpBefore-playerTotalHpAfter
    iALose=iATotalHpBefore-iATotalHpAfter
    playerRatio=playerTotalHpAfter/playerTotalHpBefore
    iARatio=iATotalHpAfter/iATotalHpBefore
    val=int(max(playerLose,iALose)*(playerRatio-iARatio))
    return val

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

def makeRandomIALeaf(player,opponent,myMap):
    blockPrint()
    feuille=[[],[]]
    for perso in player:
        feuille[0].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
    for perso in opponent:
        feuille[1].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
    
    #Opponent turn
    playerToMove = list(range(len(opponent)))
    listAction=[]
    while playerToMove and anyoneWin(feuille[0],feuille[1])==0:
        selectedPlayer = choice(playerToMove)
        if feuille[1][selectedPlayer][2].getHp()!=0:
            listMovePosible=movePossible(feuille,feuille[1][selectedPlayer],myMap)
            # permet de valoriser les cases ou une attaque en leurs donnant un poid 4 fois plus élevé que les casses ou il n'y a personne à attaquer
            betterMove=[]
            i=0
            for move in listMovePosible:
                copyFeuille=[[],[]]
                for perso in feuille[0]:
                    copyFeuille[0].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
                for perso in feuille[1]:
                    copyFeuille[1].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
                copyFeuille[1][selectedPlayer]=listMovePosible[i]
                copyCible=getEnemieToAttack(copyFeuille[0],copyFeuille[1][selectedPlayer])
                if len(copyCible)!=0:
                    copySelectAtk = choice(range(len(copyCible)))
                else:
                    copySelectAtk=0
                if copySelectAtk!=0:
                    betterMove.append(move)
                    betterMove.append(move)
                    betterMove.append(move)
                    betterMove.append(move)
                else:
                    betterMove.append(move)
                i+=1
            selectedMove = choice(range(len(betterMove)))
            #make move
            feuille[1][selectedPlayer]=betterMove[selectedMove]
            listAction.append((feuille[0][:],feuille[1][:]))

            cible=getEnemieToAttack(feuille[0],feuille[1][selectedPlayer])
            if len(cible)!=0:
                selectAtk = choice(range(len(cible)))
            else:
                selectAtk=-1
            #make an attak
            if selectAtk!=-1:
                feuille[0][getCharName(feuille[0],cible[selectAtk][2].getName())],feuille[1][selectedPlayer]=attack(cible[selectAtk],feuille[1][selectedPlayer])
            playerToMove.remove(selectedPlayer)
            listAction.append((feuille[0][:],feuille[1][:]))
    enablePrint()
    return listAction


def makeRandomPlayerLeaf(player,opponent,myMap):
    blockPrint()
    feuille=[[],[]]
    for perso in player:
        feuille[0].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
    for perso in opponent:
        feuille[1].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
    
    #Player turn
    playerToMove = list(range(len(player)))
    listAction=[]
    while playerToMove :
        selectedPlayer = choice(playerToMove)
        if feuille[1][selectedPlayer][2].getHp()!=0:
            listAction.append(selectedPlayer)
            listMovePosible=movePossible(feuille,feuille[0][selectedPlayer],myMap)
            # permet de valoriser les cases ou une attaque en leurs donnant un poid 4 fois plus élevé que les casses ou il n'y a personne à attaquer
            betterMove=[]
            i=0
            for move in listMovePosible:
                copyFeuille=[[],[]]
                for perso in feuille[0]:
                    copyFeuille[0].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
                for perso in feuille[1]:
                    copyFeuille[1].append([pygame.Surface.copy(perso[0]),deepcopy(perso[1]),deepcopy(perso[2])])
                copyFeuille[1][selectedPlayer]=listMovePosible[i]
                copyCible=getEnemieToAttack(copyFeuille[1],copyFeuille[0][selectedPlayer])
                if len(copyCible)!=0:
                    copySelectAtk = choice(range(len(copyCible)))
                else:
                    copySelectAtk=0
                #make an attak
                if copySelectAtk!=0:
                    betterMove.append(move)
                    betterMove.append(move)
                    betterMove.append(move)
                    betterMove.append(move)
                else:
                    betterMove.append(move)
                i+=1
            selectedMove = choice(range(len(betterMove)))
            feuille[0][selectedPlayer]=betterMove[selectedMove] #make move

            cible=getEnemieToAttack(feuille[1],feuille[0][selectedPlayer])
            if len(cible)!=0:
                selectAtk = choice(range(len(cible)))
            else:
                selectAtk=0
            #make an attak
            if selectAtk!=0:
                feuille[1][getCharName(feuille[1],cible[selectAtk][2].getName())],feuille[0][selectedPlayer]=attack(cible[selectAtk],feuille[0][selectedPlayer])
            playerToMove.remove(selectedPlayer)
    enablePrint()
    return feuille[0][:],feuille[1][:]
        
        

#prendre cordonné du joueur, prendre les case autour valide, appliquer a nouveau movepossible tant que mouvement!=0
#recuper la liste des coordonné, factoriser les doublon et retourner cette liste
def movePossible(feuille,selectedPlayer,myMap):
    if selectedPlayer in feuille[0]:
        me=0
        you=1
    else:
        me=1
        you=0
    mouvementDepart=copy(selectedPlayer[2].getMove())
    playerListAtPos=[]
    playerListAtPos.append(selectedPlayer)
    listPos=[]
    listPos.append(selectedPlayer[1])
    for characters in playerListAtPos:
        mouvement=copy(characters[2].getMove())
        if mouvement > 0:
            character=[]
            character.append(pygame.Surface.copy(characters[0]))
            character.append(deepcopy(characters[1]))
            character.append(deepcopy(characters[2]))
            if character[1].top+90 < 720 :
                if deplacementValide(int((character[1].top+90)/90),int((character[1].left)/90),myMap,feuille[me],feuille[you],character[2].getTypeMove()):
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
                if deplacementValide(int((character[1].top-90)/90),int((character[1].left)/90),myMap,feuille[me],feuille[you],character[2].getTypeMove()):
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
                if deplacementValide(int((character[1].top)/90),int((character[1].left+90)/90),myMap,feuille[me],feuille[you],character[2].getTypeMove()):
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
                if deplacementValide(int((character[1].top)/90),int((character[1].left-90)/90),myMap,feuille[me],feuille[you],character[2].getTypeMove()):
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
    for item in playerListAtPos:
        item[2].moves=mouvementDepart
    return playerListAtPos

    
#leaf => mvt perso 1 => atk perso 1 => mvt perso 2 => atk perso 2 => mvt perso 3 => atk perso 3 => mvt perso 4 => atk perso 4

