import inspect
import sys
import random
from typing import Type
from traits_people import *

class KingdomTraits:
    def __init__(self):
        self.name = "Kingdom Trait Placeholder"
        self.conflicting = []
        self.people_traits = []
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Kingdom_Peaceful(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Peaceful'
        self.conflicting = [Kingdom_Agressive, Kingdom_Militarist]
        self.people_traits = [People_Kind]

class Kingdom_Agressive(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Agressive'
        self.conflicting = [Kingdom_Peaceful] 
        self.people_traits = []

class Kingdom_Militarist(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Militarist'
        self.conflicting = [Kingdom_WellLiked, Kingdom_Peaceful]  
        self.people_traits = []   

class Kingdom_Vegetarian(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Vegetarian'
        self.conflicting = [Kingdom_Hunting]
        self.people_traits = []   

class Kingdom_Artsy(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Artsy'
        self.conflicting = []   
        self.people_traits = [People_Artsy]

class Kingdom_Cultured(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Cultured'
        self.conflicting = []    
        self.people_traits = [People_Artsy]

class Kingdom_Wealthy(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Wealthy'
        self.conflicting = [Kingdom_Poor]   
        self.people_traits = [People_Lazy, People_Cowardly, People_Content]   

class Kingdom_Poor(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Poor'
        self.conflicting = [Kingdom_Wealthy] 
        self.people_traits = [People_Stressed]

class Kingdom_Religious(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Religious'
        self.conflicting = [Kingdom_Athiest] 
        self.people_traits = []   #Amplifies the effect of the kingdom's religion

class Kingdom_Athiest(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Athiest'
        self.conflicting = [Kingdom_Religious] 
        self.people_traits = []   #Completely nullifies the effect of the kingdom's religion

class Kingdom_FreeTrade(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Free trade'
        self.conflicting = [Kingdom_RestrictedTrade] 
        self.people_traits = []   

class Kingdom_RestrictedTrade(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Restricted trade'
        self.conflicting = [Kingdom_FreeTrade] 
        self.people_traits = []   

class Kingdom_Sciene(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Scientifically Adept'
        self.conflicting = [] 
        self.people_traits = [People_Ambitious]   

class Kingdom_WellLiked(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Well-liked'
        self.conflicting = [Kingdom_Disliked]   
        self.people_traits = [People_Kind, People_Honest, People_Charitable]   

class Kingdom_Disliked(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Disliked'
        self.conflicting = [Kingdom_WellLiked]  
        self.people_traits = [People_Greedy]   

class Kingdom_Gentrified(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Class Divide'
        self.conflicting = []  
        self.people_traits = [] #Rich AND poor    

class Kingdom_Alcohol(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Alcohol-fueled'
        self.conflicting = []  
        self.people_traits = [People_Alcoholic] 

class Kingdom_Drugs(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Drug-fueled'
        self.conflicting = []      
        self.people_traits = [People_DrugAddicted] 

class Kingdom_Amphibious(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Amphibious'
        self.conflicting = [] 
        self.people_traits = []   #More interest in the water. Considering removing...        
          
class Kingdom_Wizards(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Wizards'
        self.conflicting = [] 
        self.people_traits = []   #Wizardry is it's own beast TODO

class Kingdom_Conflict(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Internal Conflict'
        self.conflicting = []  
        self.people_traits = [People_Stressed] 

class Kingdom_Schizophrenic(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Schizophrenic'
        self.conflicting = []  
        self.people_traits = [People_Genius, People_Imbecile, People_DrugAddicted, People_Alcoholic, People_Lunatic, People_Depressed, People_Greedy] #My favourite

class Kingdom_Charitable(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Charitable'
        self.conflicting = [Kingdom_Greedy]  
        self.people_traits = [People_Charitable]         

class Kingdom_Greedy(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Greedy'
        self.conflicting = [Kingdom_Charitable]  
        self.people_traits = [People_Greedy]    

#General Interests of the people
class Kingdom_Fishing(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Fishing Culture'
        self.conflicting = []
        self.people_traits = []   

class Kingdom_Farming(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Farming Culture'
        self.conflicting = []
        self.people_traits = []   

class Kingdom_Hunting(KingdomTraits):
    def __init__(self):
        super().__init__()
        self.name = 'Hunting Culture'
        self.conflicting = [Kingdom_Vegetarian]
        self.people_traits = []   

#Return pointers to all above classes in a big list
def allKingdomTraits():
    all_traits = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj.__module__ == __name__ and obj != KingdomTraits:
            all_traits.append(obj)
    return all_traits

#Conplexity of this isn't great to be honest
def someKingdomTraits(num_traits = 1) -> Type[KingdomTraits]:
    all_traits = allKingdomTraits()
    traits = [] #These could all be sets...
    conflicting_all = set()
    seen = set()
    for i in range(num_traits):
        chosen_trait = random.choice(all_traits)
        while chosen_trait in conflicting_all or chosen_trait in seen:
            chosen_trait = random.choice(all_traits)
        seen.add(chosen_trait)
        chosen_trait : KingdomTraits = chosen_trait() #Make the class reference an object
        conflicting_all.update(chosen_trait.conflicting) #Add the objects's conflicting references to the list
        traits.append(chosen_trait)
    return traits

if __name__ == '__main__':
    trait = someKingdomTraits(num_traits = 2)
    for i in trait:
        print(i)
