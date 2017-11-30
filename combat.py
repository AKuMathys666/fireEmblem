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
    
t_map=deplacement(aleatoire)
print(t_map)

fenetre.blit(fond,(0,0))

positionPlayer=getArrayPos(t_map,6)
positionOpponent=getArrayPos(t_map,7)

C1 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C1.set_colorkey((255,255,255))
position_C1 = C1.get_rect()
position_C1 = position_C1.move(positionPlayer[0][1],positionPlayer[0][0])
print(position_C1)

C2 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C2.set_colorkey((255,255,255))
position_C2 = C2.get_rect()
position_C2 = position_C2.move(positionPlayer[1][1],positionPlayer[1][0])
print(position_C2)

C3 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C3.set_colorkey((255,255,255))
position_C3 = C3.get_rect()
position_C3 = position_C3.move(positionPlayer[2][1],positionPlayer[2][0])
print(position_C3)

C4 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C4.set_colorkey((255,255,255))
position_C4 = C4.get_rect()
position_C4 = position_C4.move(positionPlayer[3][1],positionPlayer[3][0])
print(position_C4)

player = []
player.append([C1,position_C1,1,3,44,40,28,27,18])
player.append([C2,position_C2,2,2,38,41,40,20,30])
player.append([C3,position_C3,2,0,41,43,30,29,20])
player.append([C4,position_C4,2,0,37,35,25,25,40])

D1 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D1.set_colorkey((255,255,255))
position_D1 = D1.get_rect()
position_D1 = position_D1.move(positionOpponent[0][1],positionOpponent[0][0])
print(position_D1)

D2 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D2.set_colorkey((255,255,255))
position_D2 = D2.get_rect()
position_D2 = position_D2.move(positionOpponent[1][1],positionOpponent[1][0])
print(position_D2)

D3 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D3.set_colorkey((255,255,255))
position_D3 = D3.get_rect()
position_D3 = position_D3.move(positionOpponent[2][1],positionOpponent[2][0])
print(position_D3)

D4 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D4.set_colorkey((255,255,255))
position_D4 = D4.get_rect()
position_D4 = position_D4.move(positionOpponent[3][1],positionOpponent[3][0])
print(position_D4)

opponent = []
#opponent.append([image,position,deplacement(1 à 3 selon le type_deplacement),type_deplacement(0=infanterie, 1=cavalier, 2=flier, 3=tank)],vie,atk,speed,def,res)
opponent.append([D1,position_D1,2,0,50,45,32,18,22])
opponent.append([D2,position_D2,3,1,36,38,36,25,28])
opponent.append([D3,position_D3,3,1,47,36,25,23,30])
opponent.append([D4,position_D4,2,2,42,52,18,38,17])

#menu droite
C1_info = pygame.Surface.copy(C1)
C1_info.set_colorkey((255,255,255))
position_C1_info = C1_info.get_rect()
position_C1_info = position_C1_info.move(540,0)

C2_info = pygame.Surface.copy(C2)
C2_info.set_colorkey((255,255,255))
position_C2_info = C2_info.get_rect()
position_C2_info = position_C2_info.move(540,90)

C3_info = pygame.Surface.copy(C3)
C3_info.set_colorkey((255,255,255))
position_C3_info = C3_info.get_rect()
position_C3_info = position_C3_info.move(540,180)

C4_info = pygame.Surface.copy(C4)
C4_info.set_colorkey((255,255,255))
position_C4_info = C4_info.get_rect()
position_C4_info = position_C4_info.move(540,270)

D1_info = pygame.Surface.copy(D1)
D1_info.set_colorkey((255,255,255))
position_D1_info = D1_info.get_rect()
position_D1_info = position_D1_info.move(540,360)

D2_info = pygame.Surface.copy(D2)
D2_info.set_colorkey((255,255,255))
position_D2_info = D2_info.get_rect()
position_D2_info = position_D2_info.move(540,450)

D3_info = pygame.Surface.copy(D3)
D3_info.set_colorkey((255,255,255))
position_D3_info = D3_info.get_rect()
position_D3_info = position_D3_info.move(540,540)

D4_info = pygame.Surface.copy(D4)
D4_info.set_colorkey((255,255,255))
position_D4_info = D4_info.get_rect()
position_D4_info = position_D4_info.move(540,630)

info = []
info.append([C1_info,position_C1_info])
info.append([C2_info,position_C2_info])
info.append([C3_info,position_C3_info])
info.append([C4_info,position_C4_info])
info.append([D1_info,position_D1_info])
info.append([D2_info,position_D2_info])
info.append([D3_info,position_D3_info])
info.append([D4_info,position_D4_info])

info_fond=[]
for i in range(8):
    current_background=pygame.image.load("img\character_stats.png").convert()
    info_fond.append([current_background,current_background.get_rect().move(540,90*i)])

for item in info_fond :
    fenetre.blit(item[0],item[1])
for item in info :
    fenetre.blit(item[0],item[1])
    
ChoixPerso = 0

continuer=True
turn = 0 # 0 = player, 1 = opponent
#vie,atk,speed,def,res 4 5 6 7 8
i=0
for item in player :
    fenetre.blit(item[0],item[1])
    
    current_hp=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_hp.render(str(item[4]),True, (255,255,255)),(720,33+(i*90)))
    
    current_atk=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_atk.render(str(item[5]),True, (255,255,255)),(720,63+(i*90)))
    
    current_vit=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_vit.render(str(item[6]),True, (255,255,255)),(840,3+(i*90)))
    
    current_def=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_def.render(str(item[7]),True, (255,255,255)),(840,33+(i*90)))
    
    current_res=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_res.render(str(item[8]),True, (255,255,255)),(840,63+(i*90)))
    
    i+=1
for item in opponent:
    fenetre.blit(item[0],item[1])

    current_hp=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_hp.render(str(item[4]),True, (255,255,255)),(720,33+(i*90)))
    
    current_atk=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_atk.render(str(item[5]),True, (255,255,255)),(720,63+(i*90)))
    
    current_vit=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_vit.render(str(item[6]),True, (255,255,255)),(840,3+(i*90)))
    
    current_def=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_def.render(str(item[7]),True, (255,255,255)),(840,33+(i*90)))
    
    current_res=pygame.font.SysFont('Arial',23)
    fenetre.blit(current_res.render(str(item[8]),True, (255,255,255)),(840,63+(i*90)))
    
    i+=1

turnPlayer = player[:]
mouvement=copy(turnPlayer[ChoixPerso][2])

#Boucle infinie
while continuer :
    pygame.display.flip()
    while len(turnPlayer)!=0 :
        fenetre.blit(fond,(0,0))
        for item in player :
            fenetre.blit(item[0],item[1])
        for item in opponent :
            fenetre.blit(item[0],item[1])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT :
                continuer=0
            if event.type == KEYUP :
                eventOccur=False
                if event.key == K_DOWN :
                    if turnPlayer[ChoixPerso][1].top+90 < 720 :
                        if deplacementValide(int((turnPlayer[ChoixPerso][1].top+90)/90),int((turnPlayer[ChoixPerso][1].left)/90),t_map,player,opponent,turnPlayer[ChoixPerso][3]):
                            if t_map[int((turnPlayer[ChoixPerso][1].top+90)/90)][int((turnPlayer[ChoixPerso][1].left)/90)]==3 and turnPlayer[ChoixPerso][2]==0:
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
                            if t_map[int((turnPlayer[ChoixPerso][1].top-90)/90)][int((turnPlayer[ChoixPerso][1].left)/90)]==3 and turnPlayer[ChoixPerso][2]==0:
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
                            if t_map[int((turnPlayer[ChoixPerso][1].top)/90)][int((turnPlayer[ChoixPerso][1].left-90)/90)]==3 and turnPlayer[ChoixPerso][2]==0:
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
                            if t_map[int((turnPlayer[ChoixPerso][1].top)/90)][int((turnPlayer[ChoixPerso][1].left+90)/90)]==3 and turnPlayer[ChoixPerso][2]==0:
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
