from dnd import Character

def calcer(foo):
    return sum([foo.getgene(i, 16, 16) for i in range(0,3)]) % 100 + 1

def tester(num):
    thing = {}
    for i in range(0, num):
        result = calcer(Character())
        if result in thing:
            thing[result] += 1
        else:
            thing[result] = 1
    return thing

def tester2(num):
    thing = {}
    for i in range(0, num):
        result = Character().a_str
        if result in thing:
            thing[result] += 1
        else:
            thing[result] = 1
    return thing
