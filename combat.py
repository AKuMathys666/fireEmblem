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
mouvement=copy(turnPlayer[ChoixPerso][2])

#Boucle infinie
while continuer :
    pygame.display.flip()
    while len(turnPlayer)!=0 :
        fenetre=displayFight(fenetre,fond,player,opponent)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT :
                continuer=0
            if event.type == KEYUP :
                eventOccur=False
                if event.key == K_DOWN :
                    if turnPlayer[ChoixPerso][1].top+90 < 720 :
                        if deplacementValide(int((turnPlayer[ChoixPerso][1].top+90)/90),int((turnPlayer[ChoixPerso][1].left)/90),t_map,player,opponent,turnPlayer[ChoixPerso][3]):
                            if t_map[int((turnPlayer[ChoixPerso][1].top+90)/90)][int((turnPlayer[ChoixPerso][1].left)/90)]==3 and turnPlayer[ChoixPerso][3]==0:
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
                        if deplacementValide(int((turnPlayer[ChoixPerso][1].top-90)/90),int((turnPlayer[ChoixPerso][1].left)/90),t_map,player,opponent,turnPlayer[ChoixPerso][3]):
                            if t_map[int((turnPlayer[ChoixPerso][1].top-90)/90)][int((turnPlayer[ChoixPerso][1].left)/90)]==3 and turnPlayer[ChoixPerso][3]==0:
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
                        if deplacementValide(int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left-90)/90),t_map,player,opponent,turnPlayer[ChoixPerso][3]):
                            if t_map[int((turnPlayer[ChoixPerso][1].top)/90)][int((turnPlayer[ChoixPerso][1].left-90)/90)]==3 and turnPlayer[ChoixPerso][3]==0:
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
                        if deplacementValide(int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left+90)/90),t_map,player,opponent,turnPlayer[ChoixPerso][3]):
                            if t_map[int((turnPlayer[ChoixPerso][1].top)/90)][int((turnPlayer[ChoixPerso][1].left+90)/90)]==3 and turnPlayer[ChoixPerso][3]==0:
                                if mouvement-2 >=0:
                                    turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(90,0)
                                    mouvement-=2
                                    eventOccur = True
                            else:
                                mouvement-=1
                                turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(90,0)
                                eventOccur = True
                if event.key == K_TAB :
                    if mouvement!=copy(turnPlayer[ChoixPerso][2]):
                        turnPlayer.remove(turnPlayer[ChoixPerso])
                    if ChoixPerso < len(turnPlayer)-1 :
                        ChoixPerso+=1
                    else:
                        ChoixPerso=0
                    if len(turnPlayer)!=0: 
                            mouvement=copy(turnPlayer[ChoixPerso][2])
                if eventOccur:
                    if turnPlayer[ChoixPerso][3] == 0:
                        print("Infanterie ",int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left)/90))
                    if turnPlayer[ChoixPerso][3] == 1:
                        print("Cavalier ",int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left)/90))
                    if turnPlayer[ChoixPerso][3] == 2:
                        print("Flier ",int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left)/90))
                    if turnPlayer[ChoixPerso][3] == 3:
                        print("Tank ",int((turnPlayer[ChoixPerso][1].top)/90),int((turnPlayer[ChoixPerso][1].left)/90))
                    pygame.display.flip()
                    if mouvement==0:
                        turnPlayer.remove(turnPlayer[ChoixPerso])
                        if ChoixPerso < len(turnPlayer)-1 :
                            ChoixPerso+=1
                        else:
                            ChoixPerso=0
                        if len(turnPlayer)!=0: 
                            mouvement=copy(turnPlayer[ChoixPerso][2])
    if turn==0 :
        turn=1
        turnPlayer = opponent[:]
        mouvement=copy(turnPlayer[ChoixPerso][2])
    else :
        turn=0
        turnPlayer = player[:]
        mouvement=copy(turnPlayer[ChoixPerso][2])
