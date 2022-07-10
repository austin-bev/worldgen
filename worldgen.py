import random
from namegen import *
from relationships import Relationships
from religion import Religion
from worldtraits import WorldTraits, someWorldTraits
from kingdomtraits import KingdomTraits, someKingdomTraits

class World:
    def __init__(self, name, kingdoms, religions, world_traits):
        self.name : str = name
        self.kingdoms : list[Kingdom] = kingdoms
        self.capital : Kingdom = random.choice(kingdoms)
        self.religions : list[Religion] = religions
        self.world_traits : list[WorldTraits] = world_traits
    
    def __str__(self):
        return f"World: {self.name}. Capital: {self.capital.name}, World Traits: {self.world_traits}"

class Kingdom:
    def __init__(self, name : str, year_created : int, religion : Religion, traits : list[KingdomTraits]):
        self.name : str = name
        self.created : int = year_created 
        self.religion : Religion = religion
        self.culture : Culture = ""
        self.kingdom_traits : list[KingdomTraits] = traits
        self.slogan : str = "" #Generated from existing traits. 

    def __str__(self):
        return f"Kingdom: {self.name}. Created: {self.created}, Religion: {self.religion}, Kingdom Traits: {self.kingdom_traits}"

class Culture:
    def __init__(self):
        self.likes = []
        self.dislikes = []

if __name__ == "__main__":
    starter_kingdoms = 5
    print("Simulating 1000 years of history")
    kingdomnames = kingdomNames(starter_kingdoms)
    religionnames = religionNames(starter_kingdoms)
    religions = [Religion(i) for i in religionnames]
    kingdoms = [Kingdom(i, 0, random.choice(religions), someKingdomTraits(2)) for i in kingdomnames]
    world_traits = someWorldTraits(3)
    world = World(worldName(), kingdoms, religions, world_traits)

    print(world)
    for i in kingdoms:
        print(i)

    relationships = Relationships(starter_kingdoms)
    
    
