import random
from namegen import *
from relationships import Relationships
from religion import Religion
from traits_people import somePeopleTraits, splitPeopleTraits
from traits_world import WorldTraits, someWorldTraits
from traits_kingdom import KingdomTraits, someKingdomTraits

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
    def __init__(self, name : str, year_created : int , religion : Religion, traits : list[KingdomTraits]):
        self.name : str = name
        self.created : int = year_created 
        self.religion : Religion = religion
        self.culture : Culture = "" #TODO
        self.kingdom_traits : list[KingdomTraits] = traits
        self.slogan : str = "" #Generated from existing traits. TODO

    def __str__(self):
        return f"Kingdom: {self.name}. Religion: {self.religion.name}, Kingdom Traits: {self.kingdom_traits}"

class Culture:
    def __init__(self):
        self.likes = []
        self.dislikes = []

if __name__ == "__main__":
    starter_kingdoms = 5
    print("Simulating 1000 years of history")
    #Generate all names
    kingdomnames = kingdomNames(starter_kingdoms)
    religionnames = religionNames(starter_kingdoms)

    #Create religion objects

    religions = [Religion(i, splitPeopleTraits(somePeopleTraits(4))) for i in religionnames]

    #Create kingdom objects
    kingdoms = [Kingdom(i, 0, random.choice(religions), someKingdomTraits(2)) for i in kingdomnames]

    #Generate world object and traits
    world_traits = someWorldTraits(3)
    world = World(worldName(), kingdoms, religions, world_traits)

    print(world,'\n')
    for i in kingdoms:
        print(i)
    print()
    for i in religions:
        print(i)

    relationships = Relationships(starter_kingdoms)
    
    
