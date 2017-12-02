
class Caracter:
    #Classe de personne

    def __init__(self, identity, name, typeMove, hp, atk, vit, defs, res,
                 porte, typeAtk, color, image):
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
        self.porte = porte
        tabMoves = {"Infanterie":2, "Flier":2, "Cavalier":3, "Tank":1}
        self.moves = tabMoves[self.typeMove]
        self.typeAtk = typeAtk
        
    
    def display(self):
        print("id: ", self.identity, "\nName: ", self.name, "\nhp: ", self.hp, "\natk: ",
              self.atk,"\ndef: ", self.defs,"\nres: ", self.res, "\nvit: ",
              self.vit, "\nMove type: ", self.typeMove,"\ncolor: ", self.color, "\nimage: ",
              self.image, "\nporte: ", self.porte, "\nmoves: ", self.moves)

    def getUrl(self):
        return self.image

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getAtk(self):
        return self.atk

    def getDef(self):
        return self.defs

    def getRes(self):
        return self.res
    
    def getVit(self):
        return self.vit
    
    def getMove(self):
        return self.moves
    
    def getColor(self):
        return self.color
    
    def getPorte(self):
        return self.porte
    
    def getMoves(self):
        return self.moves
    
    def getTypeAtk(self):
        return self.typeAtk

    def getTypeMove(self):
        return self.typeMove
