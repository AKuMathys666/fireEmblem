import pygame
from pygame.locals import *
pygame.init()

#crée une fenêtre 540*720 qui affiche l'image choisis
fenetre = pygame.display.set_mode((540,720),RESIZABLE)
fond = pygame.image.load("img/Maps/S0102.png").convert()
#fenetre.blit(fond,(0,0))
#pygame.display.flip()


C1 = pygame.image.load("img\Characters\Azura - Dancer/BtlFace - Copie.png").convert()
C1.set_colorkey((255,255,255))
#fenetre.blit(C1,(180,0))
position_C1 = C1.get_rect()
print(position_C1)
fenetre.blit(C1,position_C1)
#pygame.display.flip()


C2 = pygame.image.load("img\Characters\Athena\BtlFace - Copie.png").convert()
C2.set_colorkey((255,255,255))
#fenetre.blit(C2,(120,0))
position_C2 = C2.get_rect()
print(position_C2)
fenetre.blit(C2,position_C2)
#pygame.display.flip()

ChoixPerso = 1
continuer=1

#Boucle infinie
while continuer:
    fenetre.blit(fond,(0,0))
    fenetre.blit(C1,position_C1)
    fenetre.blit(C2,position_C2)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer=0
        if ChoixPerso == 1:
            if event.type == KEYUP:
                print(ChoixPerso)
                print(position_C1)
                if event.key == K_DOWN:
                    if position_C1.top+90 < 720 :
                        position_C1 = position_C1.move(0,90)
                        pygame.display.flip()
                if event.key == K_UP:
                    if position_C1.top-90 >= 0:
                        position_C1 = position_C1.move(0,-90)
                        pygame.display.flip()
                if event.key == K_LEFT:
                    if position_C1.left-90 >= 0:
                        position_C1 = position_C1.move(-90,0)
                        pygame.display.flip()
                if event.key == K_RIGHT:
                    if position_C1.left+90 < 540:
                        position_C1 = position_C1.move(90,0)
                        pygame.display.flip()
                if event.key == K_TAB:
                    ChoixPerso=2
        
                
        elif ChoixPerso == 2:
            if event.type == KEYUP:
                print(ChoixPerso)
                print(position_C2)
                if event.key == K_DOWN:
                    if position_C2.top+90 < 720 :
                        position_C2 = position_C2.move(0,90)
                        pygame.display.flip()
                if event.key == K_UP:
                    if position_C2.top-90 >= 0:
                        position_C2 = position_C2.move(0,-90)
                        pygame.display.flip()
                if event.key == K_LEFT:
                    if position_C2.left-90 >= 0:
                        position_C2 = position_C2.move(-90,0)
                        pygame.display.flip()
                if event.key == K_RIGHT:
                    if position_C2.left+90 < 540:
                        position_C2 = position_C2.move(90,0)
                        pygame.display.flip()
                if event.key == K_TAB:
                    ChoixPerso=1
                          


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
