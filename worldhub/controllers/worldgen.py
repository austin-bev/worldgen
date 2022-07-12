import random
from ..models.kingdom import Kingdom, generateKingdoms
from ..models.people import generateLeader
from ..models.relationships import Relationships
from ..controllers.namegen import *
from ..models.religion import Religion, generateReligions
from ..models.traits_world import WorldTraits, someWorldTraits

class World:
    def __init__(self, name, kingdoms, religions, world_traits):
        self.name : str = name
        self.kingdoms : list[Kingdom] = kingdoms
        self.capital : Kingdom = random.choice(kingdoms)
        self.religions : list[Religion] = religions
        self.world_traits : list[WorldTraits] = world_traits
    
    def __str__(self):
        return f"{self.name}. Capital: {self.capital.name}, World Traits: {self.world_traits}"

class Culture:
    def __init__(self):
        self.likes = []
        self.dislikes = []

def generateWorld():
    starter_kingdoms = 5
    print("Simulating 1000 years of history")
    religions = generateReligions(starter_kingdoms)
    kingdoms = generateKingdoms(starter_kingdoms, religions)
    for i in kingdoms: i.setLeader(generateLeader(i))
    #Generate world object and traits
    world_traits = someWorldTraits(3)
    world = World(worldName(), kingdoms, religions, world_traits)
    return world

if __name__ == "__main__":
    world = generateWorld()
    religions = world.religions
    kingdoms = world.kingdoms

    print(world,'\n')
    for i in kingdoms: 
        print(i)
        print('\t',"Leader",i.leader)
    print()
    for i in religions: print(i)

    relationships = Relationships(kingdoms)
    
    
