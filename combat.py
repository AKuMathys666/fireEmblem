import pygame
from pygame.locals import *
from random import *
pygame.init()
from map import *
from function import *
from copy import *
from alphaBeta import *
import sys
import time

#crée une fenêtre 540*720 qui affiche l'image choisis
fenetre = pygame.display.set_mode((900,720),RESIZABLE)
terrain_disponible=9
aleatoire=choice(range(terrain_disponible))
fond=getFond(aleatoire)
    
fenetre.blit(fond,(0,0))

t_map=deplacement(aleatoire)
for map in t_map:
    print(map)

print("PRESENTATION DU JEU:")
print("------------------------------------------------------")
print("Ce jeu se compose d'une partie en versus avec 2 joueurs.")
print("Chaque joueur possède 4 personnages tirés aléatoirement sans doublons.")
print("L'objectif est de vaincre les 4 personnages adverses.")
print("Le jeu se déroule en tour par tour, vous jouez avec vos 4 personnages puis l'adversaire joue avec ses 4 personnages.")
print("Triangle advantage: des bonus malus de 20 % sont accordés selon la couleurs des personnages qui s'attaquent:")
print("Bleu > Rouge, Rouge > Vert, Vert > Bleu, le Gris étant l'element neutre")
print("Lorsque vous attaquer un adversaire si vous avez au moins 5 de vitesse de plus que lui, vous l'attaquez 2 fois")
print("Lorsque vous attaquez un adversaire, il ripostera s'il en est capable.")
print("De plus, certains personnages possèdes des armes spéciales dites 'brave weapons' leurs permettant d'attaquer 2 fois")
print("Selon le type de déplacement de vos personnages vous pourez vous déplacer plus ou moins librement d'une a trois cases.")
print("Le terrain est donc a prendre en compte (il est lui même choisit aléatoirement)")
print("Le type d'attaque,également dépendant du personnage est a considérer, magique ou physique il se heurtera respectivement aux resistances ou défenses adverse")
print("Pour se déplacer utilisez les fleches directionnelles.")
print("Pour confirner un deplacement entrez 'y' pour l'annuler et retourner a votre position de début de tour faites 'n'.")
print("Puisque vous pouvez jouer sur n'importe lequelle de vos personnages dans l'ordre que vous souhaitez, entrez la touche de tabulation afin de passer au personnages suivant.")
print("Attention, faire tabulation ne consome pas le tour du personnage!")
print("Si des enemie sont a porté d'attaque une fois votre deplacement effectué, il vous sera proposé de confirmer lequel vous voulez attaquer.")
print("Bonne chance!")
print("------------------------------------------------------")
print("Personnages du joueur 1 :")

positionPlayer=getArrayPos(t_map,6)
positionOpponent=getArrayPos(t_map,7)
player,opponent=initCharacters(positionPlayer,positionOpponent)

for chara in player:
    chara[2].display()

print("------------------------------------------------------")
print("Personnages du joueur 2 :")
for chara in opponent:
    chara[2].display()
fenetre=displayInfoBackground(fenetre,player,opponent)
fenetre=displayInfoStats(fenetre,player,opponent)
    
ChoixPerso = 0

continuer=True
turn = 0 # 0 = player, 1 = opponent


#turn=1
#makeTree(player,opponent,turn)

turnPlayer = player[:]
mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])

numTour=1

print("------------------------------------------------------")
print("--------------------- TOUR",numTour,"-------------------------")
print("-------------------- Joueur 1 ------------------------")
print("Tour de ",turnPlayer[ChoixPerso][2].getName())

#Boucle infinie
while continuer :
    pygame.display.flip()
    while len(turnPlayer)!=0 :
        fenetre=displayFight(fenetre,fond,player,opponent)
        pygame.display.flip()
        if turn == 1: #tour de l'IA
            stackLeaf=list()
            stackLeaf = evaluationIA(player,opponent,t_map)
            for item in stackLeaf:
                time.sleep(0.5)
                player,opponent=item[0],item[1]
                fenetre=displayFight(fenetre,fond,player,opponent)
                fenetre=displayInfoBackground(fenetre,player,opponent)
                fenetre=displayInfoStats(fenetre,player,opponent)
                pygame.display.flip()
            turnPlayer=[]
        else:
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
                            if ChoixPerso < len(turnPlayer)-1 :
                                ChoixPerso+=1
                            else:
                                ChoixPerso=0
                            if len(turnPlayer)!=0: 
                                    mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                                    print("Tour de ",turnPlayer[ChoixPerso][2].getName())
                            characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
                            pygame.display.flip()
                        if eventOccur:
                            pygame.display.flip()
                            if mouvement==0:
                                print("Voulez vous confirmer le déplacement de ",turnPlayer[ChoixPerso][2].getName(),"? y/n")
                        if event.key == K_y :
                            if turn==0:
                                cible=getEnemieToAttack(opponent,turnPlayer[ChoixPerso])
                            else:
                                cible=getEnemieToAttack(player,turnPlayer[ChoixPerso])
                            if not cible:
                                print("Pas de cible a proximité, fin de tour pour ",turnPlayer[ChoixPerso][2].getName())
                            else:
                                print("Un ou plusieurs enemies sont a porté d'attaque. Entrez le numero correspondant afin d'attaquer le personnage ciblé:")
                                i=1
                                print("0 pour ne pas attaquer")
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
                                                        opponent[getCharName(opponent,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                        player[getCharName(player,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                        answer=False
                                                    else:
                                                        player[getCharName(player,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                        opponent[getCharName(opponent,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                        answer=False
                                                if event2.key == K_0:
                                                    answer=False
                                                i+=1
                                        
                                fenetre=displayInfoBackground(fenetre,player,opponent)
                                fenetre=displayInfoStats(fenetre,player,opponent)
                            turnPlayer.remove(turnPlayer[ChoixPerso])
                            if ChoixPerso < len(turnPlayer)-1 :
                                ChoixPerso+=1
                            else:
                                ChoixPerso=0
                            if turn==0:
                                alive = []
                                for chara in opponent:
                                    if chara[2].getHp()!=0:
                                        alive.append(chara)
                                if not alive:
                                    continuer=False
                            else:
                                alive = []
                                for chara in player:
                                    if chara[2].getHp()!=0:
                                        alive.append(chara)
                                if not alive:
                                    continuer=False
                            if len(turnPlayer)!=0:
                                mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                                characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
                                print("Tour de ",turnPlayer[ChoixPerso][2].getName())
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
                                print("Pas de cible a proximité, fin de tour pour ",turnPlayer[ChoixPerso][2].getName())
                            else:
                                print("Un ou plusieurs enemies sont a porté d'attaque. Entrez le numero correspondant afin d'attaquer le personnage ciblé:")
                                i=1
                                print("0 pour ne pas attaquer")
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
                                                if event2.key == keyname and i<= len(cible):
                                                    if turn ==0:
                                                        opponent[getCharName(opponent,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                        player[getCharName(player,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                        answer=False
                                                    else:
                                                        player[getCharName(player,cible[i][2].getName())],turnPlayer[ChoixPerso]=attack(cible[i],turnPlayer[ChoixPerso])
                                                        opponent[getCharName(opponent,turnPlayer[ChoixPerso][2].getName())][2].hp=turnPlayer[ChoixPerso][2].getHp()
                                                        answer=False
                                                if event2.key == K_0:
                                                    answer=False
                                                i+=1
                                fenetre=displayInfoBackground(fenetre,player,opponent)
                                fenetre=displayInfoStats(fenetre,player,opponent)
                            turnPlayer.remove(turnPlayer[ChoixPerso])
                            if ChoixPerso < len(turnPlayer)-1 :
                                ChoixPerso+=1
                            else:
                                ChoixPerso=0
                            if turn==0:
                                alive = []
                                for chara in opponent:
                                    if chara[2].getHp()!=0:
                                        alive.append(chara)
                                if not alive:
                                    continuer=False
                            else:
                                alive = []
                                for chara in player:
                                    if chara[2].getHp()!=0:
                                        alive.append(chara)
                                if not alive:
                                    continuer=False
                            if len(turnPlayer)!=0:
                                mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                                characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
                                print("Tour de ",turnPlayer[ChoixPerso][2].getName())
                        if event.key == K_n:
                            turnPlayer[ChoixPerso][1]=copy(characterPosBeforeTurn)
                            mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
                            pygame.display.flip()
    if turn==0 :
        turn=1
        turnPlayer = []
        for item in opponent:
            if item[2].getHp()!=0:
                turnPlayer.append(item)
        if turnPlayer:
            mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
            characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
        else:
            continuer=False
        if turnPlayer :
            print("--------------------- TOUR",numTour,"-------------------------")
            print("-------------------- Joueur 2 ------------------------")
            numTour+=1
            print("Tour de ",turnPlayer[ChoixPerso][2].getName())
    else :
        turn=0
        for item in player:
            if item[2].getHp()!=0:
                turnPlayer.append(item)
        if turnPlayer:
            mouvement=copy(turnPlayer[ChoixPerso][2].getMove())
            characterPosBeforeTurn=copy(turnPlayer[ChoixPerso][1])
        else:
            continuer=False
        if turnPlayer :
            print("--------------------- TOUR",numTour,"-------------------------")
            print("-------------------- Joueur 1 ------------------------")
            numTour+=1
            print("Tour de ",turnPlayer[ChoixPerso][2].getName())

fenetre=displayInfoBackground(fenetre,player,opponent)
fenetre=displayInfoStats(fenetre,player,opponent)
fenetre=displayFight(fenetre,fond,player,opponent)
pygame.display.flip()

if turn==0:
    print("Joueur 1 est vainqueur")
else:
    print("Joueur 2 est vainqueur")
