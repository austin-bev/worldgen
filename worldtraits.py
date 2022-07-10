import inspect
import sys
import random
from typing import Type

class WorldTraits:
    def __init__(self):
        self.name = "World Trait Placeholder"
        self.conflicting = []
        #World Generation biases
        #Islands, mountains, volcanoes, ect...
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

#Government styles
class World_Militarist(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Militarist'

class World_Dictatorship(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Dictatorship'
        self.conflicting = [World_Democracy, World_Libertarian]

class World_Democracy(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Democracy'
        self.conflicting = [World_Dictatorship]

class World_Corrupt(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Corrupt'

class World_Libertarian(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Libertarian'
        self.conflicting = [World_Dictatorship]

class World_Communist(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Communist'
        self.conflicting = [World_Libertarian, World_Democracy]

#World features / geography
class World_Mountainous(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Mountainous'

class World_Volcanic(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Volcanic'

class World_Skyward(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Skyward'
        self.conflicting = [World_Underwater]

class World_Flooded(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Flooded'
        self.conflicting = [World_Underwater, World_Archipelago]

class World_Underwater(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Underwater'
        self.conflicting = [World_Skyward, World_Flooded, World_Archipelago]

class World_Archipelago(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Archipelago'
        self.conflicting = [World_Flooded, World_Underwater, World_Pangea]

class World_Pangea(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Pangea'
        self.conflicting = [World_Archipelago]

#World weather
class World_Snowy(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Snowy'
        self.conflicting = []

class World_Desert(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Desert'
        self.conflicting = [World_Rainy]

class World_Rainy(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Rainy'
        self.conflicting = [World_Desert]

class World_Foggy(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Foggy'
        self.conflicting = []

class World_Thunderous(WorldTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Thunderous'
        self.conflicting = []

#Return pointers to all above classes in a big list
def allWorldTraits():
    all_traits = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj != WorldTraits:
            all_traits.append(obj)
    return all_traits

#Conplexity of this isn't great to be honest
def someWorldTraits(num_traits = 1) -> Type[WorldTraits]:
    all_traits = allWorldTraits()
    traits = [] #These could all be sets...
    conflicting_all = []
    seen = []
    for i in range(num_traits):
        chosen_trait = random.choice(all_traits)
        while chosen_trait in conflicting_all or chosen_trait in seen:
            chosen_trait = random.choice(all_traits)
        seen.append(chosen_trait)
        chosen_trait : WorldTraits = chosen_trait() #Make the class reference an object
        conflicting_all += chosen_trait.conflicting #Add the objects's conflicting references to the list
        traits.append(chosen_trait)
    return traits

if __name__ == '__main__':
    trait = someWorldTraits(num_traits = 2)
    for i in trait:
        print(i)
