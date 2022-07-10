class Relationships:
    def __init__(self, kingdoms):
        self.relationships = [[0 for i in range(kingdoms)] for j in range(kingdoms)]
        self.kingdoms = kingdoms
    
    def addKingdom(self):
        self.kingdoms += 1
        for i in self.relationships: #Kingdom is neutral to all existing kingdoms
            i.append(0) 
        self.relationships.append([0 for i in range(self.kingdoms)]) #New kingdom is neutral to all existing kingdoms
    
    def changeRelationship(self, kingdomOne, kingdomTwo, change):
        self.relationships[kingdomOne][kingdomTwo] += change
        self.relationships[kingdomTwo][kingdomOne] += change

    def setRelationship(self, kingdomOne, kingdomTwo, new):
        self.relationships[kingdomOne][kingdomTwo] = new
        self.relationships[kingdomTwo][kingdomOne] = new