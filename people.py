import kingdom
from namegen import kingdomNames, personNameGeneration, religionNames
from religion import Religion
from traits_functions import updateWeights, getWeightedTraits, splitTraits
from traits_kingdom import Kingdom_Athiest, Kingdom_Religious, someKingdomTraits
from traits_multipliers import *
from traits_people import PeopleTraits, allPeopleTraits, somePeopleTraits  
import worldgen

class Person:
    def __init__(self, firstname, lastname, gender, traits, kingdom):
        self.firstname : str = firstname
        self.lastname : str = lastname
        self.gender : str = gender
        self.traits : list[PeopleTraits] = traits
        self.kingdom : worldgen.Kingdom = kingdom
        self.religion : Religion = kingdom.religion
    
    def __str__(self):
        return f"Name: {self.firstname} {self.lastname} ({self.gender}). Traits: {self.traits}. Kingdom: {self.kingdom.name}"

def personWeights(kingdom, leader = False):
    #Kingdom Weights
    weighted_traits = getWeightedTraits(kingdom)
    all_traits = allPeopleTraits()
    weights = updateWeights(weighted_traits, all_traits, KINGDOM_MULTIPLIER*LEADER_MULTIPLIER) if leader else updateWeights(weighted_traits, all_traits, KINGDOM_MULTIPLIER)
    #Religion Weights
    religionBonus = 1
    if Kingdom_Religious in kingdom.kingdom_traits: 
        religionBonus = RELIGION_BONUS_MULTIPLIER
    elif Kingdom_Athiest in kingdom.kingdom_traits:
        religionBonus = NO_RELIGION_MULTIPLIER
    weights = updateWeights({type(i) for i in kingdom.religion.desirable}, all_traits, RELIGION_MULTIPLIER*religionBonus, existing_weights = weights)
    weights = updateWeights({type(i) for i in kingdom.religion.undesirable}, all_traits, RELIGION_NEGATIVE_MULTIPLIER*religionBonus, existing_weights = weights)
    return weights

def generateLeader(kingdom):
    weights = personWeights(kingdom, leader=True)
    firstname, lastname, gender = personNameGeneration(1)[0]
    traits = somePeopleTraits(3, weights) 
    return Person(firstname, lastname, gender, traits, kingdom)

def generatePeople(kingdom, number):
    all_people = []
    weights = personWeights(kingdom)
    for i in range(number):
        firstname, lastname, gender = personNameGeneration(1)[0]
        traits = somePeopleTraits(3, weights) 
        all_people.append(Person(firstname, lastname, gender, traits, kingdom))
    return all_people

if __name__ == '__main__':
    kingdom = kingdom.generateKingdoms(1)[0]
    people = generatePeople(kingdom, 3)
    print(kingdom)
    print(kingdom.religion)
    for i in people:
        print(i)