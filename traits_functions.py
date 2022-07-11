import random

def someTraits(all_traits, num_traits = 1, weights = None): 
    traits = []
    conflicting_all = set()
    seen = set()
    for i in range(num_traits):
        chosen_trait = random.choices(all_traits, weights)[0] if weights else random.choice(all_traits)
        while chosen_trait in conflicting_all or chosen_trait in seen:
            chosen_trait = random.choices(all_traits, weights)[0] if weights else random.choice(all_traits)
        seen.add(chosen_trait)
        chosen_trait = chosen_trait() #Make the class reference an object
        conflicting_all.update(chosen_trait.conflicting) #Add the objects's conflicting references to the list
        traits.append(chosen_trait)
    return traits

def getWeightedTraits(kingdom):
    traits = set()
    for i in kingdom.kingdom_traits:
        for j in i.people_traits:
            traits.add(j)
    return traits

#Not specific to people
def createWeights(weighted_traits, all_traits):
    l = len(all_traits)
    weights = [10 for i in range(l)]
    for i in range(l):
        if all_traits[i] in weighted_traits: #Weighted traits should be hash table/set for O(1) search
            weights[i]=weights[i]*10
    return weights

#This is dumb
def splitTraits(allTraits):
    l = len(allTraits)
    if l % 2 == 0:
        h = int(l / 2)
        return allTraits[0:h], allTraits[h:l]
    #Nothing done if odd number of traits at the moment. Plan to change this anyway

if __name__ == '__main__':
    pass
