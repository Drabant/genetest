import object
import random
random.seed()

gens = 100

men = [object.Human(gender=object.MALE) for i in range(0, 50)]
women = [object.Human(gender=object.FEMALE) for i in range(0, 50)]

def sortdict(dictionary):
    return {i: dictionary[i] for i in sorted(dictionary)}

generation = 0
while generation < gens:
    generation += 1
    boys = []
    girls = []
    for mother in women:
        father = men[random.randint(0, len(men)-1)]
        if father.father == mother.father:
            father = men[random.randint(0, len(men)-1)]
        if father.mother == mother.mother:
            father = men[random.randint(0, len(men)-1)]
        for i in range(0, random.randint(2, 3)):
            child = object.Human(mother, father)
            if child.gender == object.MALE:
                boys += [child]
            else:
                girls += [child]
    men = boys
    women = girls
    inbred = 0
    for i in women + men:
        if i.inbred():
            inbred += 1
    print("Generation", generation, ": there are", len(men), "men and", len(women), "women.", str(int(inbred * 100 / len(men + women))) + "% inbred.")

#inbreeding = {}
#for i in men + women:
#    inbred = i.inbred()
#    if inbred in inbreeding:
#        inbreeding[inbred] += 1
#    else:
#        inbreeding[inbred] = 1
#inbreeding = sortdict(inbreeding)
#for i in inbreeding:
#    print(i, ":", inbreeding[i])
