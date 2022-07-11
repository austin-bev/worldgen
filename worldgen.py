import random
import kingdom
import people
import relationships
from namegen import *
from religion import Religion, generateReligions
from traits_world import WorldTraits, someWorldTraits

class World:
    def __init__(self, name, kingdoms, religions, world_traits):
        self.name : str = name
        self.kingdoms : list[kingdom.Kingdom] = kingdoms
        self.capital : kingdom.Kingdom = random.choice(kingdoms)
        self.religions : list[Religion] = religions
        self.world_traits : list[WorldTraits] = world_traits
    
    def __str__(self):
        return f"World: {self.name}. Capital: {self.capital.name}, World Traits: {self.world_traits}"

class Culture:
    def __init__(self):
        self.likes = []
        self.dislikes = []

if __name__ == "__main__":
    starter_kingdoms = 5
    print("Simulating 1000 years of history")
    religions = generateReligions(starter_kingdoms)
    kingdoms = kingdom.generateKingdoms(starter_kingdoms, religions)
    for i in kingdoms: i.setLeader(people.generateLeader(i))
    #Generate world object and traits
    world_traits = someWorldTraits(3)
    world = World(worldName(), kingdoms, religions, world_traits)

    print(world,'\n')
    for i in kingdoms: 
        print(i)
        print('\t',"Leader",i.leader)
    print()
    for i in religions: print(i)

    relationships = relationships.Relationships(starter_kingdoms)
    
    
