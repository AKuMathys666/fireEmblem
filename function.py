import pygame
from pygame.locals import *
from random import *

def getArrayPos(anyArray,number):
	arrayreturn = []
	for i,line in enumerate(anyArray):
		for j,val in enumerate(line):
			if val == number:
				arrayreturn.append([i*90,j*90])
	return arrayreturn

def samePos(x,y,player,opponent):
	valReturn = True
	for item in player :
		if item[1].top/90== x:
			if item[1].left/90== y:
				valReturn = False #Joueur sur la case ciblé
	for item in opponent :
		if item[1].top/90== x:
			if item[1].left/90== y:
				valReturn = False # Enemie sur la case ciblé
	return valReturn
	
def deplacementValide(x,y,map,player,opponent,type_deplacement):
	
	if type_deplacement==0:#Infanterie
		if map[x][y] in (0,3,6,7):
			return samePos(x,y,player,opponent)
	elif type_deplacement==1:#Cavalier
		if map[x][y] in (0,6,7):
			return samePos(x,y,player,opponent)
	elif type_deplacement==2:#Flier
		if map[x][y] in (0,2,3,6,7):
			return samePos(x,y,player,opponent)
	else:#Tank
		if map[x][y] in (0,3,6,7):
			return samePos(x,y,player,opponent)
	return False
	
def getFond(aleatoire):
	if aleatoire==0:
		fond = pygame.image.load("img/Maps/S0102.png").convert()
		print("S0102")
	if aleatoire==1:
		fond = pygame.image.load("img/Maps/S0305.png").convert()
		print("S0305")
	if aleatoire==2:
		fond = pygame.image.load("img/Maps/S0405.png").convert()
		print("S0405")
	if aleatoire==3:
		fond = pygame.image.load("img/Maps/S0504.png").convert()
		print("S0504")
	if aleatoire==4:
		fond = pygame.image.load("img/Maps/S1401.png").convert()
		print("S1401")
	if aleatoire==5:
		fond = pygame.image.load("img/Maps/X0022.png").convert()
		print("X0022")
	if aleatoire==6:
		fond = pygame.image.load("img/Maps/X0081.png").convert()
		print("X0081")
	if aleatoire==7:
		fond = pygame.image.load("img/Maps/S0202.png").convert()
		print("S0202")
	if aleatoire==8:
		fond = pygame.image.load("img/Maps/S0502.png").convert()
		print("S0502")
	return fond
	
def initCharacters(positionPlayer, positionOpponent):
	listePerso=[]
	#Ajouter la liste des personnages
	#Dans cet exemple seul 2 personnages sont disponible 4 fois chacun mais réelement il faut au oins 8 personnages différents.
	listePerso.append("img\Characters\Azura - Dancer/BtlFace - Copie.png")
	listePerso.append("img\Characters\Azura - Dancer/BtlFace - Copie.png")
	listePerso.append("img\Characters\Azura - Dancer/BtlFace - Copie.png")
	listePerso.append("img\Characters\Azura - Dancer/BtlFace - Copie.png")
	listePerso.append("img\Characters\Athena\BtlFace - Copie.png")
	listePerso.append("img\Characters\Athena\BtlFace - Copie.png")
	listePerso.append("img\Characters\Athena\BtlFace - Copie.png")
	listePerso.append("img\Characters\Athena\BtlFace - Copie.png")
	listePersoAvailable = listePerso[:]
	
	aleatoire=choice(range(len(listePersoAvailable)))
	
	C1 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	C1.set_colorkey((255,255,255))
	position_C1 = C1.get_rect()
	position_C1 = position_C1.move(positionPlayer[0][1],positionPlayer[0][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])
	
	aleatoire=choice(range(len(listePersoAvailable)))

	C2 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	C2.set_colorkey((255,255,255))
	position_C2 = C2.get_rect()
	position_C2 = position_C2.move(positionPlayer[1][1],positionPlayer[1][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])
	
	aleatoire=choice(range(len(listePersoAvailable)))

	C3 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	C3.set_colorkey((255,255,255))
	position_C3 = C3.get_rect()
	position_C3 = position_C3.move(positionPlayer[2][1],positionPlayer[2][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])
	
	aleatoire=choice(range(len(listePersoAvailable)))

	C4 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	C4.set_colorkey((255,255,255))
	position_C4 = C4.get_rect()
	position_C4 = position_C4.move(positionPlayer[3][1],positionPlayer[3][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])
	
	aleatoire=choice(range(len(listePersoAvailable)))

	player = []
	player.append([C1,position_C1,1,3,44,40,28,27,18])
	player.append([C2,position_C2,2,2,38,41,40,20,30])
	player.append([C3,position_C3,2,0,41,43,30,29,20])
	player.append([C4,position_C4,2,0,37,35,25,25,40])

	D1 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	D1.set_colorkey((255,255,255))
	position_D1 = D1.get_rect()
	position_D1 = position_D1.move(positionOpponent[0][1],positionOpponent[0][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])
	
	aleatoire=choice(range(len(listePersoAvailable)))

	D2 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	D2.set_colorkey((255,255,255))
	position_D2 = D2.get_rect()
	position_D2 = position_D2.move(positionOpponent[1][1],positionOpponent[1][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])
	
	aleatoire=choice(range(len(listePersoAvailable)))

	D3 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	D3.set_colorkey((255,255,255))
	position_D3 = D3.get_rect()
	position_D3 = position_D3.move(positionOpponent[2][1],positionOpponent[2][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])
	
	aleatoire=choice(range(len(listePersoAvailable)))

	D4 = pygame.image.load(listePersoAvailable[aleatoire]).convert()
	D4.set_colorkey((255,255,255))
	position_D4 = D4.get_rect()
	position_D4 = position_D4.move(positionOpponent[3][1],positionOpponent[3][0])
	listePersoAvailable.remove(listePersoAvailable[aleatoire])

	opponent = []
	#opponent.append([image,position,deplacement(1 à 3 selon le type_deplacement),type_deplacement(0=infanterie, 1=cavalier, 2=flier, 3=tank)],vie,atk,speed,def,res)
	opponent.append([D1,position_D1,2,0,50,45,32,18,22])
	opponent.append([D2,position_D2,3,1,36,38,36,25,28])
	opponent.append([D3,position_D3,3,1,47,36,25,23,30])
	opponent.append([D4,position_D4,2,2,42,52,18,38,17])
	
	return (player,opponent)
	
#def displayUpdate(fenetre):
	
def displayFight(fenetre,fond,player,opponent):
	fenetre.blit(fond,(0,0))
	for item in player :
		fenetre.blit(item[0],item[1])
	for item in opponent :
		fenetre.blit(item[0],item[1])
	return fenetre
	
def displayInfoBackground(fenetre,player,opponent):
	#menu droite
	C1_info = pygame.Surface.copy(player[0][0])
	C1_info.set_colorkey((255,255,255))
	position_C1_info = C1_info.get_rect()
	position_C1_info = position_C1_info.move(540,0)

	C2_info = pygame.Surface.copy(player[1][0])
	C2_info.set_colorkey((255,255,255))
	position_C2_info = C2_info.get_rect()
	position_C2_info = position_C2_info.move(540,90)

	C3_info = pygame.Surface.copy(player[2][0])
	C3_info.set_colorkey((255,255,255))
	position_C3_info = C3_info.get_rect()
	position_C3_info = position_C3_info.move(540,180)

	C4_info = pygame.Surface.copy(player[3][0])
	C4_info.set_colorkey((255,255,255))
	position_C4_info = C4_info.get_rect()
	position_C4_info = position_C4_info.move(540,270)

	D1_info = pygame.Surface.copy(opponent[0][0])
	D1_info.set_colorkey((255,255,255))
	position_D1_info = D1_info.get_rect()
	position_D1_info = position_D1_info.move(540,360)

	D2_info = pygame.Surface.copy(opponent[1][0])
	D2_info.set_colorkey((255,255,255))
	position_D2_info = D2_info.get_rect()
	position_D2_info = position_D2_info.move(540,450)

	D3_info = pygame.Surface.copy(opponent[2][0])
	D3_info.set_colorkey((255,255,255))
	position_D3_info = D3_info.get_rect()
	position_D3_info = position_D3_info.move(540,540)

	D4_info = pygame.Surface.copy(opponent[3][0])
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
		
	return fenetre
	
def displayInfoStats(fenetre,player,opponent):
	i=0
	for item in player :
		#display character
		fenetre.blit(item[0],item[1])

		#display info stats
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
		#display character
		fenetre.blit(item[0],item[1])

		#display info stats
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
	return fenetre