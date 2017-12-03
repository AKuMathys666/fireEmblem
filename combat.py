import pygame
from pygame.locals import *
from random import *
pygame.init()
from map import *
from function import *
from copy import *

#crée une fenêtre 540*720 qui affiche l'image choisis
fenetre = pygame.display.set_mode((900,720),RESIZABLE)
terrain_disponible=9
aleatoire=choice(range(terrain_disponible))
fond=getFond(aleatoire)
    
fenetre.blit(fond,(0,0))

t_map=deplacement(aleatoire)
for map in t_map:
    print(map)

positionPlayer=getArrayPos(t_map,6)
positionOpponent=getArrayPos(t_map,7)
player,opponent=initCharacters(positionPlayer,positionOpponent)

fenetre=displayInfoBackground(fenetre,player,opponent)
fenetre=displayInfoStats(fenetre,player,opponent)
    
ChoixPerso = 0

continuer=True
turn = 0 # 0 = player, 1 = opponent

turnPlayer = player[:]
mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])

#Boucle infinie
while continuer :
    pygame.display.flip()
    while len(turnPlayer)!=0 :
        fenetre=displayFight(fenetre,fond,player,opponent)
        pygame.display.flip()
        for event in pygame.event.get():
            if mouvement != 0:
                if event.type == QUIT :
                    continuer=0
                if event.type == KEYUP :
                    eventOccur=False
                    if event.key == K_DOWN :
                        if turnPlayer[ChoixPerso][1].top+90 < 720 :
                            if deplacementValide(int((turnPlayer[ChoixPerso][1].top+90)/90),int((turnPlayer[ChoixPerso][1].left)/90),t_map,player,opponent,turnPlayer[ChoixPerso][2].getTypeMove()):
                                if t_map[int((turnPlayer[ChoixPerso][1].top+90)/90)][int((turnPlayer[ChoixPerso][1].left)/90)]==3 and turnPlayer[ChoixPerso][2].getTypeMove()=="Infanterie":
                                    if mouvement-2 >=0:
                                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(0,90)
                                        mouvement-=2
                                        eventOccur = True
                                else:
                                    mouvement-=1
                                    turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(0,90)
                                    eventOccur = True
                    if event.key == K_UP :
                        if turnPlayer[ChoixPerso][1].top-90 >= 0 :
                            if deplacementValide(int((turnPlayer[ChoixPerso][1].top-90)/90),int((turnPlayer[ChoixPerso][1].left)/90),t_map,player,opponent,turnPlayer[ChoixPerso][2].getTypeMove()):
                                if t_map[int((turnPlayer[ChoixPerso][1].top-90)/90)][int((turnPlayer[ChoixPerso][1].left)/90)]==3 and turnPlayer[ChoixPerso][2].getTypeMove()=="Infanterie":
                                    if mouvement-2 >=0:
                                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(0,-90)
                                        mouvement-=2
                                        eventOccur = True
                                else:
                                    mouvement-=1
                                    turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(0,-90)
                                    eventOccur = True
                    if event.key == K_LEFT :
                        if turnPlayer[ChoixPerso][1].left-90 >= 0 :
                            if deplacementValide(int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left-90)/90),t_map,player,opponent,turnPlayer[ChoixPerso][2].getTypeMove()):
                                if t_map[int((turnPlayer[ChoixPerso][1].top)/90)][int((turnPlayer[ChoixPerso][1].left-90)/90)]==3 and turnPlayer[ChoixPerso][2].getTypeMove()=="Infanterie":
                                    if mouvement-2 >=0:
                                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(-90,0)
                                        mouvement-=2
                                        eventOccur = True
                                else:
                                    mouvement-=1
                                    turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(-90,0)
                                    eventOccur = True
                    if event.key == K_RIGHT :
                        if turnPlayer[ChoixPerso][1].left+90 < 540 :
                            if deplacementValide(int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left+90)/90),t_map,player,opponent,turnPlayer[ChoixPerso][2].getTypeMove()):
                                if t_map[int((turnPlayer[ChoixPerso][1].top)/90)][int((turnPlayer[ChoixPerso][1].left+90)/90)]==3 and turnPlayer[ChoixPerso][2].getTypeMove()=="Infanterie":
                                    if mouvement-2 >=0:
                                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(90,0)
                                        mouvement-=2
                                        eventOccur = True
                                else:
                                    mouvement-=1
                                    turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(90,0)
                                    eventOccur = True
                    if event.key == K_TAB :
                        turnPlayer[ChoixPerso][1]=copy(characterPosBeforeTurn)
                        mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                        characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
                        pygame.display.flip()
                        if ChoixPerso < len(turnPlayer)-1 :
                            ChoixPerso+=1
                        else:
                            ChoixPerso=0
                        if len(turnPlayer)!=0: 
                                mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                    if eventOccur:
                        print(turnPlayer[ChoixPerso][2].getName()," ",turnPlayer[ChoixPerso][2].getTypeMove()," ",int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left)/90))
                        pygame.display.flip()
                        if mouvement==0:
                            print("Voulez vous confirmer le déplacement? y/n")
                    if event.key == K_y :
                        if turn==0:
                            cible=getEnemieToAttack(opponent,turnPlayer[ChoixPerso])
                        else:
                            cible=getEnemieToAttack(player,turnPlayer[ChoixPerso])
                        if not cible:
                            print("Pas de cible a proximité")
                        else:
                            print("Un ou plusieurs enemies sont a porté d'attaque. Entrez le numero correspondant afin d'attaquer le personnage ciblé:")
                            i=1
                            for ciblePossible in cible:
                                print(i,ciblePossible[2].getName())
                                i+=1
                            answer=True
                            arrayKey=(K_1,K_2,K_3,K_4)
                            while answer:
                                for event2 in pygame.event.get():
                                    i=0
                                    for keyname in arrayKey:
                                        if event2.type == KEYUP :
                                            if event2.key == keyname :
                                                if turn ==0:
                                                    print(getCharName(opponent,cible[i][2].getName()))
                                                    print(attack(cible[i],turnPlayer[ChoixPerso]))
                                                    opponent[getCharName(opponent,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                    player[getCharName(player,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                    answer=False
                                                else:
                                                    print(getCharName(player,cible[i][2].getName()))
                                                    print(attack(cible[i],turnPlayer[ChoixPerso]))
                                                    player[getCharName(player,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                    opponent[getCharName(opponent,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                    answer=False
                                            i+=1
                            fenetre=displayInfoBackground(fenetre,player,opponent)
                            fenetre=displayInfoStats(fenetre,player,opponent)
                        turnPlayer.remove(turnPlayer[ChoixPerso])
                        if ChoixPerso < len(turnPlayer)-1 :
                            ChoixPerso+=1
                        else:
                            ChoixPerso=0
                        if len(turnPlayer)!=0:
                            mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                            characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
                    if event.key == K_n:
                        turnPlayer[ChoixPerso][1]=copy(characterPosBeforeTurn)
                        mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                        pygame.display.flip()
            else:
                if event.type == KEYUP :
                    eventOccur=False
                    if event.key == K_y :
                        if turn==0:
                            cible=getEnemieToAttack(opponent,turnPlayer[ChoixPerso])
                        else:
                            cible=getEnemieToAttack(player,turnPlayer[ChoixPerso])
                        if not cible:
                            print("Pas de cible a proximité")
                        else:
                            print("Un ou plusieurs enemies sont a porté d'attaque. Entrez le numero correspondant afin d'attaquer le personnage ciblé:")
                            i=1
                            for ciblePossible in cible:
                                print(i,ciblePossible[2].getName())
                                i+=1
                            answer=True
                            arrayKey=(K_1,K_2,K_3,K_4)
                            while answer:
                                for event2 in pygame.event.get():
                                    i=0
                                    for keyname in arrayKey:
                                        if event2.type == KEYUP :
                                            if event2.key == keyname :
                                                if turn ==0:
                                                    print(getCharName(opponent,cible[i][2].getName()))
                                                    print(attack(cible[i],turnPlayer[ChoixPerso]))
                                                    opponent[getCharName(opponent,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                    player[getCharName(player,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                    answer=False
                                                else:
                                                    print(getCharName(player,cible[i][2].getName()))
                                                    print(attack(cible[i],turnPlayer[ChoixPerso]))
                                                    player[getCharName(player,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                    opponent[getCharName(opponent,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                    answer=False
                                            i+=1
                            fenetre=displayInfoBackground(fenetre,player,opponent)
                            fenetre=displayInfoStats(fenetre,player,opponent)
                        turnPlayer.remove(turnPlayer[ChoixPerso])
                        if ChoixPerso < len(turnPlayer)-1 :
                            ChoixPerso+=1
                        else:
                            ChoixPerso=0
                        if len(turnPlayer)!=0:
                            mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                            characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
                    if event.key == K_n:
                        turnPlayer[ChoixPerso][1]=copy(characterPosBeforeTurn)
                        mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                        pygame.display.flip()
    if turn==0 :
        turn=1
        turnPlayer = opponent[:]
        mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
        characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
    else :
        turn=0
        turnPlayer = player[:]
        mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
        characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
