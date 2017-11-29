import pygame
from pygame.locals import *
from random import *
pygame.init()
from map import deplacement

#crée une fenêtre 540*720 qui affiche l'image choisis
fenetre = pygame.display.set_mode((540,720),RESIZABLE)
terrain_disponible=9
aleatoire=choice(range(terrain_disponible))
if aleatoire==0:
    fond = pygame.image.load("img/Maps/S0102.png").convert()
if aleatoire==1:
    fond = pygame.image.load("img/Maps/S0305.png").convert()
if aleatoire==2:
    fond = pygame.image.load("img/Maps/S0405.png").convert()
if aleatoire==3:
    fond = pygame.image.load("img/Maps/S0504.png").convert()
if aleatoire==4:
    fond = pygame.image.load("img/Maps/S1401.png").convert()
if aleatoire==5:
    fond = pygame.image.load("img/Maps/X0022.png").convert()
if aleatoire==6:
    fond = pygame.image.load("img/Maps/X0081.png").convert()
if aleatoire==7:
    fond = pygame.image.load("img/Maps/S0202.png").convert()
if aleatoire==8:
    fond = pygame.image.load("img/Maps/S0502.png").convert()
    
t_map=deplacement(aleatoire)
print(t_map)

fenetre.blit(fond,(0,0))

C1 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C1.set_colorkey((255,255,255))
position_C1 = C1.get_rect()
print(position_C1)

C2 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C2.set_colorkey((255,255,255))
position_C2 = C2.get_rect()
print(position_C2)

C3 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C3.set_colorkey((255,255,255))
position_C3 = C3.get_rect()
print(position_C3)

C4 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C4.set_colorkey((255,255,255))
position_C4 = C4.get_rect()
print(position_C4)

player = []
player.append([C1,position_C1,2])
player.append([C2,position_C2,2])
player.append([C3,position_C3,2])
player.append([C4,position_C4,2])

D1 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D1.set_colorkey((255,255,255))
position_D1 = D1.get_rect()
print(position_D1)

D2 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D2.set_colorkey((255,255,255))
position_D2 = D2.get_rect()
print(position_D2)

D3 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D3.set_colorkey((255,255,255))
position_D3 = D3.get_rect()
print(position_D3)

D4 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
D4.set_colorkey((255,255,255))
position_D4 = D4.get_rect()
print(position_D4)

opponent = []
opponent.append([D1,position_D1,2])
opponent.append([D2,position_D2,2])
opponent.append([D3,position_D3,2])
opponent.append([D4,position_D4,2])

ChoixPerso = 0
continuer=1
turn = 0 # 0 = player, 1 = opponent
print(C1)

for item in player :
    print(item[0])
    fenetre.blit(item[0],item[1])
for item in opponent :
    fenetre.blit(item[0],item[1])

turnPlayer = player[:]
#Boucle infinie
while continuer :
    pygame.display.flip()
    while not turnPlayer is None :
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
                if event.key == K_DOWN :
                    if turnPlayer[ChoixPerso][1].top+90 < 720 :
                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(0,90)
                        pygame.display.flip()
                if event.key == K_UP :
                    if turnPlayer[ChoixPerso][1].top-90 >= 0 :
                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(0,-90)
                        pygame.display.flip()
                if event.key == K_LEFT :
                    if turnPlayer[ChoixPerso][1].left-90 >= 0 :
                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(-90,0)
                        pygame.display.flip()
                if event.key == K_RIGHT :
                    if turnPlayer[ChoixPerso][1].left+90 < 540 :
                        turnPlayer[ChoixPerso][1] = turnPlayer[ChoixPerso][1].move(90,0)
                        pygame.display.flip()
                if event.key == K_TAB :
                    if ChoixPerso < len(turnPlayer)-1 :
                        ChoixPerso+=1
                    else:
                        ChoixPerso=0
    if turn==0 :
        turn=1
        turnPlayer = opponent[:]
    else :
        turn=0
        turnPlayer = player[:]

"""
    #for C1
    fenetre.blit(fond,(0,0))
    fenetre.blit(C1,position_C1)
    pygame.display.flip()
    #for C2
    fenetre.blit(fond,(0,0))
    fenetre.blit(C2,position_C2)
    pygame.display.flip()
"""
