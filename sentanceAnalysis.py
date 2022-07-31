class token:
    def __init__(self, wordD, arbD, typeD):
        self.word = wordD   
        self.typeArb = arbD
        self.typeComplex = typeD
        self.pointer = None
        self.pointerWord = None
        self.strength = 0
        self.relType = None
        self.coRefNum = None

    def setPointer(self, pointer):
        self.pointer = pointer

    def setPointerWord(self, pointerWord):
        self.pointerWord = pointerWord
    
    def setWord(self, word):
        self.word = word

    def setRelationshipType(self, relTypeD):
        self.relType = relTypeD

    def setStrength(self, strength):
        self.strength = strength

    def getStrength(self):
        return self.strength
    
    def setCoRefNum(self,num):
        if self.coRefNum == None:
            self.coRefNum = num
        else:
            raise Exception("Error: CoRefNum already set")
    