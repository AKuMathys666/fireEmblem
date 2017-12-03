
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
        #print("id: ", self.identity, ", Name: ", self.name, ", hp: ", self.hp, ", atk: ",
        #      self.atk,", def: ", self.defs,", res: ", self.res, ", vit: ",
        #      self.vit, ", Move type: ", self.typeMove,", color: ", self.color, ", image: ",
        #      self.image, ", porte: ", self.porte, ", moves: ", self.moves)
        print(self.name)
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
