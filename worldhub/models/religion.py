from ..controllers.namegen import religionNames
from .traits_functions import splitTraits
from .traits_people import PeopleTraits, somePeopleTraits

class Religion:
    def __init__(self, name, traits):
        self.name = name
        self.desirable : list[PeopleTraits] = traits[0]
        self.undesirable : list[PeopleTraits] = traits[1]
    
    def __str__(self):
        return f"{self.name}. Desirable Traits: {self.desirable}, Undesirable Traits: {self.undesirable}"

def generateReligions(num_religions):
    religionnames = religionNames(num_religions)
    religions = [Religion(i, splitTraits(somePeopleTraits(4))) for i in religionnames]
    return religions