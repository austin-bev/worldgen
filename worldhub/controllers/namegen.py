import random
from ..controllers.fileio import *

#All FileIO is done in one go at the start. Files need not be accessed again after thiws
PEOPLENAMES_ALL = parseCsv('names_people.csv')
RELIGIONNAMES_ALL = parseCsv('names_religion.csv')
PLACENAMES_ALL = parseCsv('names_town.csv')

def worldName():
    return nameGeneration(PLACENAMES_ALL)[0]

def kingdomNames(kingdoms = 5):
    return nameGeneration(PLACENAMES_ALL, noise = 2, size = kingdoms)

def religionNames(religions = 5):
    return nameGeneration(RELIGIONNAMES_ALL, size = religions)

def nameGeneration(parsed_names, noise = 1, size = 1):
    s0, s1, s2 = parsed_names
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

def personNameGeneration(size):
    firstname_all, lastname_all, gender_all = PEOPLENAMES_ALL
    namelist=[]
    for i in range(size):
        rand = random.randint(0,len(firstname_all))
        firstname = firstname_all[rand]
        gender = gender_all[rand]
        lastname = random.choice(lastname_all)
        namelist.append((firstname, lastname, gender))
    return namelist