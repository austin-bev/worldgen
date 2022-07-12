'''
from ..models.kingdom import generateKingdoms
from ..models.relationships import Relationships
from ..models.religion import generateReligions

def relationshipTest(): 
    religions = generateReligions(5)
    kingdoms = generateKingdoms(5, religions) #Remove 
    rel = Relationships(kingdoms)
    for i in kingdoms: print(i)
'''

def relationshipTest():
    pass