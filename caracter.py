
class Caracter:
    #Classe de personne

    def __init__(self, identity, name, hp, atk, defs, res, vit,
                 typeMove, color, image, arm, skill, assist, p1, p2, p3):
        self.identity = identity
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defs = defs
        self.res = res
        self.vit = vit
        self.typeMove = typeMove
        self.color = color
        self.image = image
        self.arm = arm
        self.skill = skill
        self.assist = assist
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def display(self):
        print("id: ", self.identity, "\nName: ", self.name, "\nhp: ", self.hp, "\natk: ",
              self.atk,"\ndef: ", self.defs,"\nres: ", self.res, "\nvit: ",
              self.vit, "\nMove type: ", self.typeMove,"\ncolor: ", self.color, "\nimage: ",
              self.image, "\narm: ", self.arm, "\nskill: ", self.skill, "\nassist: ", self.assist,
              "\nPassif 1: ",self.p1, "\nPassif 2: ", self.p2, "\nPassif 3: ", self.p3)
=======

class Caracter:
    #Classe de personne

    def __init__(self, identity, name, hp, atk, defs, res, vit,
                 typeMove, color, image, arm, skill, assist, p1, p2, p3):
        self.identity = identity
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defs = defs
        self.res = res
        self.vit = vit
        self.typeMove = typeMove
        self.color = color
        self.image = image
        self.arm = arm
        self.skill = skill
        self.assist = assist
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def display(self):
        print("id: ", self.identity, "\nName: ", self.name, "\nhp: ", self.hp, "\natk: ",
              self.atk,"\ndef: ", self.defs,"\nres: ", self.res, "\nvit: ",
              self.vit, "\nMove type: ", self.typeMove,"\ncolor: ", self.color, "\nimage: ",
              self.image, "\narm: ", self.arm, "\nskill: ", self.skill, "\nassist: ", self.assist,
              "\nPassif 1: ",self.p1, "\nPassif 2: ", self.p2, "\nPassif 3: ", self.p3)