from namegen import kingdomNames, personNameGeneration, religionNames
from religion import Religion
from traits_kingdom import someKingdomTraits
from traits_people import *
from worldgen import Kingdom

class Person:
    def __init__(self, firstname, lastname, gender, traits, kingdom):
        self.firstname : str = firstname
        self.lastname : str = lastname
        self.gender : str = gender
        self.traits : list[PeopleTraits] = traits
        self.kingdom : Kingdom = kingdom
    
    def __str__(self):
        return f"Name: {self.firstname} {self.lastname} ({self.gender}). Traits: {self.traits}. Kingdom: {self.kingdom.name}"

def generatePeople(kingdom, number):
    all_people = []
    for i in range(number):
        firstname, lastname, gender = personNameGeneration(1)[0]
        traits = somePeopleTraits(3) #Doesn't take into account the bias from kingdoms TODO
        all_people.append(Person(firstname, lastname, gender, traits, kingdom))
    return all_people

if __name__ == '__main__':
    kingdom = Kingdom(kingdomNames(1)[0], 0, Religion(religionNames(1)[0], splitPeopleTraits(somePeopleTraits(4))), someKingdomTraits(2))
    people = generatePeople(kingdom, 3)
    print(kingdom)
    for i in people:
        print(i)