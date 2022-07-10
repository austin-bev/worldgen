import inspect
import sys
import random
from typing import Type

class KingdomTraits:
    def __init__(self):
        self.name = "Kingdom Trait Placeholder"
        self.conflicting = []
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class World_Militarist(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Militarist'

#Return pointers to all above classes in a big list
def allKingdomTraits():
    all_traits = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj != KingdomTraits:
            all_traits.append(obj)
    return all_traits

#Conplexity of this isn't great to be honest
def someKingdomTraits(num_traits = 1) -> Type[KingdomTraits]:
    all_traits = allKingdomTraits()
    traits = [] #These could all be sets...
    conflicting_all = []
    seen = []
    for i in range(num_traits):
        chosen_trait = random.choice(all_traits)
        while chosen_trait in conflicting_all or chosen_trait in seen:
            chosen_trait = random.choice(all_traits)
        seen.append(chosen_trait)
        chosen_trait : KingdomTraits = chosen_trait() #Make the class reference an object
        conflicting_all += chosen_trait.conflicting #Add the objects's conflicting references to the list
        traits.append(chosen_trait)
    return traits

if __name__ == '__main__':
    trait = someKingdomTraits(num_traits = 2)
    for i in trait:
        print(i)
