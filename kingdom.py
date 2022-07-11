import random
import people
from namegen import kingdomNames
from religion import Religion
from traits_kingdom import KingdomTraits, someKingdomTraits
import worldgen


class Kingdom:
    def __init__(self, name : str, year_created : int , religion : Religion, traits : list[KingdomTraits]):
        self.name : str = name
        self.created : int = year_created 
        self.religion : Religion = religion
        self.culture : worldgen.Culture = "" #TODO
        self.leader : people.Person = ""
        self.kingdom_traits : list[KingdomTraits] = traits
        self.slogan : str = "" #Generated from existing traits. TODO

    def setLeader(self, leader):
        self.leader = leader

    def __str__(self):
        return f"Kingdom: {self.name}. Religion: {self.religion.name}, Kingdom Traits: {self.kingdom_traits}"

#Generates kingdoms and religions
def generateKingdoms(num_kingdoms, religions):
    #Generate all names
    kingdomnames = kingdomNames(num_kingdoms)

    #Create kingdom objects
    kingdoms = [Kingdom(i, 0, random.choice(religions), someKingdomTraits(2)) for i in kingdomnames]
    return kingdoms