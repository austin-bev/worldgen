import random
from fileio import *

def worldName():
    return nameGeneration('names_town.csv')[0]

def kingdomNames(kingdoms = 5):
    return nameGeneration('names_town.csv', noise = 2, size = kingdoms)

def religionNames(religions = 5):
    return nameGeneration('names_religion.csv', size = religions)

def nameGeneration(filename, noise = 1, size = 1):
    s0, s1 = parseCsv(filename)
    namelist=[]
    for i in range(size):
        if random.randint(1,10) <= noise:
            name = s1[random.randint(0,len(s1)-1)]
            name = name.strip().title()
        else:
            name = s0[random.randint(0,len(s0)-1)]
        for i in range(noise):
            name += s1[random.randint(0,len(s1)-1)]
        namelist.append(name)
    return namelist