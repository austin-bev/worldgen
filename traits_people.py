import inspect
import sys
import random
from typing import Type

class PeopleTraits:
    def __init__(self):
        self.name = "People Trait Placeholder"
        self.conflicting = []
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

#Personality Traits - Thanks CK2
class People_Stressed(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Stressed'
        self.conflicting = []
        
class People_Depressed(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Depressed'
        self.conflicting = []

class People_Lunatic(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Lunatic'
        self.conflicting = []

class People_Possessed(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Possessed'
        self.conflicting = []

class People_Alcoholic(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Alcoholic'
        self.conflicting = []

class People_DrugAddicted(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Drug-Addicted'
        self.conflicting = []

class People_Homosexual(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Homosexual'
        self.conflicting = []

class People_Genius(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Genius'
        self.conflicting = [People_Slow, People_Quick, People_Imbecile]

class People_Quick(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Quick'
        self.conflicting = [People_Slow, People_Genius, People_Imbecile]

class People_Slow(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Slow'
        self.conflicting = [People_Genius, People_Quick, People_Imbecile]    

class People_Imbecile(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Imbecile'
        self.conflicting = [People_Slow, People_Genius, People_Quick]   

class People_Strong(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Strong'
        self.conflicting = [People_Weak]   

class People_Weak(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Weak'
        self.conflicting = [People_Strong] 

class People_Lustful(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Lustful'
        self.conflicting = []     

class People_Gluttonous(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Gluttonous'
        self.conflicting = [] 

class People_Greedy(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Greedy'
        self.conflicting = [People_Charitable, People_Kind, People_Honest]  

class People_Charitable(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Charitable'
        self.conflicting = [People_Greedy]     

class People_Lazy(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Lazy'
        self.conflicting = []    

class People_Kind(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Kind'
        self.conflicting = [People_Greedy]  

class People_Honest(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Honest'
        self.conflicting = [People_Greedy]

class People_Brave(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Brave'
        self.conflicting = [People_Cowardly]   

class People_Cowardly(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Cowardly'
        self.conflicting = [People_Brave] 

class People_Ambitious(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Ambitious'
        self.conflicting = [People_Content]         

class People_Content(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Content'
        self.conflicting = [People_Ambitious] 
          
class People_Artsy(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Artsy'
        self.conflicting = []  

# Physical Traits
class People_Attractive(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Attractive'
        self.conflicting = [People_Ugly]

class People_Ugly(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Ugly'
        self.conflicting = [People_Attractive]

class People_Dwarf(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Dwarf'
        self.conflicting = [People_Tall]

class People_Tall(PeopleTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Tall'
        self.conflicting = [People_Dwarf]

#Interests TODO

#Return pointers to all above classes in a big list
def allPeopleTraits():
    all_traits = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj != PeopleTraits:
            all_traits.append(obj)
    return all_traits

#Conplexity of this isn't great to be honest
def somePeopleTraits(num_traits = 1) -> Type[PeopleTraits]:
    all_traits = allPeopleTraits()
    traits = []
    conflicting_all = set()
    seen = set()
    for i in range(num_traits):
        chosen_trait = random.choice(all_traits)
        while chosen_trait in conflicting_all or chosen_trait in seen:
            chosen_trait = random.choice(all_traits)
        seen.add(chosen_trait)
        chosen_trait : PeopleTraits = chosen_trait() #Make the class reference an object
        conflicting_all.update(chosen_trait.conflicting) #Add the objects's conflicting references to the list
        traits.append(chosen_trait)
    return traits

def splitPeopleTraits(allTraits):
    l = len(allTraits)
    if l % 2 == 0:
        h = int(l / 2)
        return allTraits[0:h], allTraits[h:l]

if __name__ == '__main__':
    trait = somePeopleTraits(num_traits = 2)
    for i in trait:
        print(i)
