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

class Kingdom_Peaceful(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Peaceful'
        self.conflicting = [Kingdom_Agressive, Kingdom_Militarist]

class Kingdom_Agressive(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Agressive'
        self.conflicting = [Kingdom_Peaceful] 

class Kingdom_Militarist(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Militarist'
        self.conflicting = [Kingdom_WellLiked, Kingdom_Peaceful]  

class Kingdom_Fishing(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Fishing Culture'
        self.conflicting = []

class Kingdom_Farming(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Farming Culture'
        self.conflicting = []

class Kingdom_Hunting(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Hunting Culture'
        self.conflicting = [Kingdom_Vegetarian]

class Kingdom_Vegetarian(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Vegetarian'
        self.conflicting = [Kingdom_Hunting]
        
class Kingdom_Artsy(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Artsy'
        self.conflicting = []   

class Kingdom_Cultured(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Cultured'
        self.conflicting = []    

class Kingdom_Wealthy(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Wealthy'
        self.conflicting = [Kingdom_Poor]   

class Kingdom_Poor(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Poor'
        self.conflicting = [Kingdom_Wealthy] 

class Kingdom_Religious(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Religious'
        self.conflicting = [Kingdom_Athiest] 

class Kingdom_Athiest(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Athiest'
        self.conflicting = [Kingdom_Religious] 

class Kingdom_FreeTrade(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Free trade'
        self.conflicting = [Kingdom_RestrictedTrade] 

class Kingdom_RestrictedTrade(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Restricted trade'
        self.conflicting = [Kingdom_FreeTrade] 

class Kingdom_Sciene(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Scientifically Adept'
        self.conflicting = [] 

class Kingdom_WellLiked(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Well-liked'
        self.conflicting = [Kingdom_Disliked]   

class Kingdom_Disliked(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Disliked'
        self.conflicting = [Kingdom_WellLiked]  

class Kingdom_Gentrified(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Class Divide'
        self.conflicting = []  

class Kingdom_Alcohol(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Alcohol-fueled'
        self.conflicting = []  

class Kingdom_Drugs(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Drug-fueled'
        self.conflicting = []      

class Kingdom_Amphibious(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Amphibious'
        self.conflicting = [] 
          
class Kingdom_Wizards(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Wizards'
        self.conflicting = [] 

class Kingdom_Conflict(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Internal Conflict'
        self.conflicting = []  

class Kingdom_Schizophrenic(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Schizophrenic'
        self.conflicting = []  

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
