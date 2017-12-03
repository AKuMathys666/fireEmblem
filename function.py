import pygame
from pygame.locals import *
from random import *
from caracter import *
import pymysql
from copy import *

db= pymysql.connect(host="localhost",user="root",  
    password="",db="fire_emblem_db")

def getCaracterFromDb(id):
        cur = db.cursor()
        sql = "select * from personnage where id = %s"
        try:  
            cur.execute(sql, id)      
          
            results = cur.fetchall()
            features = []
            for row in results :
                for i in range(len(row)):
                    features.append(row[i])
            person = Caracter(features[0],features[1],features[2],features[3],
                              features[4],features[5],features[6],features[7],
                              features[8],features[9],features[10],features[11])
            #person.display()
            return person
        except Exception as e:  
            raise e

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
                                if item[2].getHp()!=0:
                                        valReturn = False #Joueur sur la case ciblé
        for item in opponent :
                if item[1].top/90== x:
                        if item[1].left/90== y:
                                if item[2].getHp()!=0:
                                        valReturn = False # Enemie sur la case ciblé
        return valReturn
        
def deplacementValide(x,y,map,player,opponent,type_deplacement):
        
        if type_deplacement=="Infanterie":
                if map[x][y] in (0,3,6,7):
                        return samePos(x,y,player,opponent)
        elif type_deplacement=="Cavalier":
                if map[x][y] in (0,6,7):
                        return samePos(x,y,player,opponent)
        elif type_deplacement=="Flier":
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
        cur = db.cursor()
        sql = "select count(*) from personnage"  
        try:  
                count=cur.execute(sql)
                result=cur.fetchone()
        except Exception as e:  
                raise e
		
        listePerso=[]
        #Ajouter la liste des personnages
        #Dans cet exemple seul 2 personnages sont disponible 4 fois chacun mais réelement il faut au oins 8 personnages différents.
        for i in range(result[0]):
                listePerso.append(i+1)
        listePersoAvailable = listePerso[:]

        aleatoire=choice(listePersoAvailable)

        c1 = getCaracterFromDb(aleatoire)
        C1 = pygame.image.load(c1.getUrl()).convert()
        C1.set_colorkey((255,255,255))
        position_C1 = C1.get_rect()
        position_C1 = position_C1.move(positionPlayer[0][1],positionPlayer[0][0])
        listePersoAvailable.remove(aleatoire)

        aleatoire=choice(listePersoAvailable)

        c2 = getCaracterFromDb(aleatoire)
        C2 = pygame.image.load(c2.getUrl()).convert()
        C2.set_colorkey((255,255,255))
        position_C2 = C2.get_rect()
        position_C2 = position_C2.move(positionPlayer[1][1],positionPlayer[1][0])
        listePersoAvailable.remove(aleatoire)

        aleatoire=choice(listePersoAvailable)

        c3 = getCaracterFromDb(aleatoire)
        C3 = pygame.image.load(c3.getUrl()).convert()
        C3.set_colorkey((255,255,255))
        position_C3 = C3.get_rect()
        position_C3 = position_C3.move(positionPlayer[2][1],positionPlayer[2][0])
        listePersoAvailable.remove(aleatoire)

        aleatoire=choice(listePersoAvailable)

        c4 = getCaracterFromDb(aleatoire)
        C4 = pygame.image.load(c4.getUrl()).convert()
        C4.set_colorkey((255,255,255))
        position_C4 = C4.get_rect()
        position_C4 = position_C4.move(positionPlayer[3][1],positionPlayer[3][0])
        listePersoAvailable.remove(aleatoire)
        
        aleatoire=choice(listePersoAvailable)

        player = []
        #img, pos, déplace, typeDéplace, vie, atk,speed,def,res,distance_attaque,type_attaque
        #0=infanterie, 1=cavalier, 2=flier, 3=tank
        """
        player.append([C1,position_C1,1,3,44,40,28,27,18,2,1])
        player.append([C2,position_C2,2,2,38,41,40,20,30,2,0])
        player.append([C3,position_C3,2,0,41,43,30,29,20,1,0])
        player.append([C4,position_C4,2,0,37,35,25,25,40,1,0])
        """
        player.append([C1,position_C1,c1])
        player.append([C2,position_C2,c2])
        player.append([C3,position_C3,c3])
        player.append([C4,position_C4,c4])

        d1 = getCaracterFromDb(aleatoire)
        D1 = pygame.image.load(d1.getUrl()).convert()
        D1.set_colorkey((255,255,255))
        position_D1 = D1.get_rect()
        position_D1 = position_D1.move(positionOpponent[0][1],positionOpponent[0][0])
        listePersoAvailable.remove(aleatoire)
        
        aleatoire=choice(listePersoAvailable)

        d2 = getCaracterFromDb(aleatoire)
        D2 = pygame.image.load(d2.getUrl()).convert()
        D2.set_colorkey((255,255,255))
        position_D2 = D2.get_rect()
        position_D2 = position_D2.move(positionOpponent[1][1],positionOpponent[1][0])
        listePersoAvailable.remove(aleatoire)
        
        aleatoire=choice(listePersoAvailable)

        d3 = getCaracterFromDb(aleatoire)
        D3 = pygame.image.load(d3.getUrl()).convert()
        D3.set_colorkey((255,255,255))
        position_D3 = D3.get_rect()
        position_D3 = position_D3.move(positionOpponent[2][1],positionOpponent[2][0])
        listePersoAvailable.remove(aleatoire)
        
        aleatoire=choice(listePersoAvailable)

        d4 = getCaracterFromDb(aleatoire)
        D4 = pygame.image.load(d4.getUrl()).convert()
        D4.set_colorkey((255,255,255))
        position_D4 = D4.get_rect()
        position_D4 = position_D4.move(positionOpponent[3][1],positionOpponent[3][0])
        listePersoAvailable.remove(aleatoire)

        opponent = []
        #opponent.append([image,position,deplacement(1 à 3 selon le type_deplacement),type_deplacement(0=infanterie, 1=cavalier, 2=flier, 3=tank)],vie,atk,speed,def,res,distance_attaque(1 = cac, 2 = distance), type_attaque(0 = magie, 1=physique))
        opponent.append([D1,position_D1,d1])
        opponent.append([D2,position_D2,d2])
        opponent.append([D3,position_D3,d3])
        opponent.append([D4,position_D4,d4])
        
        return (player,opponent)
        
#def displayUpdate(fenetre):
        
def displayFight(fenetre,fond,player,opponent):
        fenetre.blit(fond,(0,0))
        for item in player :
                if item[2].getHp()!=0:
                        fenetre.blit(item[0],item[1])
        for item in opponent :
                if item[2].getHp()!=0:
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
                current_name=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_name.render(str(item[2].getName()),True, (255,255,255)),(650,3+(i*90)))
                
                current_hp=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_hp.render(str(item[2].getHp()),True, (255,255,255)),(720,33+(i*90)))
                
                current_atk=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_atk.render(str(item[2].getAtk()),True, (255,255,255)),(720,63+(i*90)))
                
                current_vit=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_vit.render(str(item[2].getVit()),True, (255,255,255)),(840,3+(i*90)))
                
                current_def=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_def.render(str(item[2].getDef()),True, (255,255,255)),(840,33+(i*90)))
                
                current_res=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_res.render(str(item[2].getRes()),True, (255,255,255)),(840,63+(i*90)))
                
                i+=1
        for item in opponent:
                #display character
                fenetre.blit(item[0],item[1])

                #display info stats
                current_name=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_name.render(str(item[2].getName()),True, (255,255,255)),(650,3+(i*90)))
                
                current_hp=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_hp.render(str(item[2].getHp()),True, (255,255,255)),(720,33+(i*90)))
                
                current_atk=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_atk.render(str(item[2].getAtk()),True, (255,255,255)),(720,63+(i*90)))
                
                current_vit=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_vit.render(str(item[2].getVit()),True, (255,255,255)),(840,3+(i*90)))
                
                current_def=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_def.render(str(item[2].getDef()),True, (255,255,255)),(840,33+(i*90)))
                
                current_res=pygame.font.SysFont('Arial',23)
                fenetre.blit(current_res.render(str(item[2].getRes()),True, (255,255,255)),(840,63+(i*90)))
                
                i+=1
        return fenetre

def getEnemieToAttack(opponent,me):
        charToAttack=[]
        #print(me[1].top,me[1].left)
        for character in opponent:
                if character[2].getHp()!=0:
                        #print(character[1].top,character[1].left)
                        if me[2].getPorte()==1:
                                # tous les cas ou un adversaire est a une case de moi
                                if character[1].top+90 == me[1].top and character[1].left == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top-90 == me[1].top and character[1].left == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top == me[1].top and character[1].left+90 == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top == me[1].top and character[1].left-90 == me[1].left:
                                        charToAttack.append(character)
                        else:
                                # tous les cas ou un adversaire est a deux cases de moi
                                if character[1].top+180 == me[1].top and character[1].left == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top-180 == me[1].top and character[1].left == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top == me[1].top and character[1].left+180 == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top == me[1].top and character[1].left-180 == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top+90 == me[1].top and character[1].left+90 == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top-90 == me[1].top and character[1].left-90 == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top+90 == me[1].top and character[1].left-90 == me[1].left:
                                        charToAttack.append(character)
                                if character[1].top-90 == me[1].top and character[1].left+90 == me[1].left:
                                        charToAttack.append(character)
        return charToAttack
        
#ne prend pas en compte les faiblesses/resistances pour le moment
def attack(opponent,me):
        if me[2].getTypeAtk()==0:                # attaque magique
                meDamage=me[2].getAtk()-opponent[2].getRes()
                himDamage=opponent[2].getAtk()-me[2].getRes()
        else:                                # attaque physique
                meDamage=me[2].getAtk()-opponent[2].getDef()
                himDamage=opponent[2].getAtk()-me[2].getDef()
        if meDamage < 0:
                meDamage=0
        if himDamage < 0:
                himDamage=0
        opponent[2].hp-= meDamage
        print(me[2].getName()," inflige ",meDamage," dégat à ",opponent[2].getName())
        if opponent[2].getHp() >0:
                me[2].hp-= himDamage
                print(opponent[2].getName()," inflige ",himDamage," dégat à ",me[2].getName())
                if me[2].getVit() >= opponent[2].getVit()+5:        #my speed >= opponent speed + 5
                        if me[2].getHp() >0:
                                opponent[2].hp-= meDamage
                                print(me[2].getName()," inflige ",meDamage," dégat à ",opponent[2].getName())
        if opponent[2].getHp() < 0:
                opponent[2].hp=0
                print(opponent[2].getName()," est hors combat.")
        if me[2].getHp() < 0:
                me[2].hp=0
                print(me[2].getName()," est hors combat.")
        return (opponent,me)

def getCharName(listChara,name):
        i=0
        for pers in listChara:
                if pers[2].getName()==name:
                        return i
                i+=1
