from namegen import kingdomNames, religionNames
from religion import Religion, generateReligions
from traits_functions import splitTraits
from traits_kingdom import Kingdom_Disliked, Kingdom_FreeTrade, Kingdom_Militarist, Kingdom_Peaceful, Kingdom_RestrictedTrade, Kingdom_WellLiked, someKingdomTraits
from traits_people import somePeopleTraits
import worldgen
import kingdom

# Initial relationship depends on:
# Well liked ++
# {Same religion} +
# Free Trade +
# Peaceful + 
# Restricted trade -
# Disliked --
# Militarist -- 

RELATIONSHIP_KINGDOM_TRAITS = {
    Kingdom_WellLiked : 5,
    Kingdom_FreeTrade : 2,
    Kingdom_Peaceful : 2,
    Kingdom_RestrictedTrade : -2,
    Kingdom_Disliked : -5,
    Kingdom_Militarist : -5
}

class Relationships:
    def __init__(self, kingdoms):
        self.relationships = self.InitialRelationships(kingdoms)
    
    def addKingdom(self):
        for i in self.relationships: 
            i.append(0) 
        self.relationships.append([0 for i in range(self.kingdoms)]) #New kingdom is neutral to all existing kingdoms
    
    def changeRelationship(self, kingdomOne, kingdomTwo, change):
        self.relationships[kingdomOne][kingdomTwo] += change
        self.relationships[kingdomTwo][kingdomOne] += change

    def setRelationship(self, kingdomOne, kingdomTwo, new):
        self.relationships[kingdomOne][kingdomTwo] = new
        self.relationships[kingdomTwo][kingdomOne] = new

    def InitialRelationships(self, kingdoms):
        l = len(kingdoms)
        reputation = [0 for i in range(l)] #Initial reputation
        for i in range(l):
            reputation[i] += self.calculateReputation(kingdoms[i])
        relationships = [reputation[::] for i in range(l)]
        for i in range(l): relationships[i][i] = 0 #All kingdoms should not hate or like themselves.
        print(relationships)
        return relationships

    def calculateReputation(self, kingdom):
        rep = 0
        for trait in kingdom.kingdom_traits:
            if type(trait) in RELATIONSHIP_KINGDOM_TRAITS:
                rep += RELATIONSHIP_KINGDOM_TRAITS[type(trait)]
        return rep

if __name__ == "__main__":
    religions = generateReligions(5)
    kingdoms = kingdom.generateKingdoms(5, religions)
    rel = Relationships(kingdoms)
    for i in kingdoms: print(i)
        
