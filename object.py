import uuid
import random
random.seed()

FEMALE = 0
MALE = 1

def coinflip():
    return random.randint(0, 1)

def makechromo():
    return random.getrandbits(64)

class Human():
    id = None
    father = None
    mother = None
    generation = None
    genes = None
    children = None
    gender = None

    def __init__(self, mother=None, father=None, gender=None):
        self.id = uuid.uuid4()
        self.genes = [None] * 23
        self.children = []
        if father is None and mother is None:
            for pair in range(0, 23):
                self.genes[pair] = [makechromo(), makechromo()]
            self.genes[22][0] &= (~0 << 1)
            self.generation = 0
            if gender is not None:
                self.genes[22][1] = (self.genes[22][1] & (~0 << 1)) | gender
        else:
            if mother.generation > father.generation:
                self.generation = mother.generation + 1
            else:
                self.generation = father.generation + 1
            for pair in range(0, 23):
                self.genes[pair] = [mother.genes[pair][coinflip()], father.genes[pair][coinflip()]]
            if gender is not None:
                self.genes[22][1] = father.genes[22][gender]
            self.father = father.id
            self.mother = mother.id
            father.children.append(self.id)
            mother.children.append(self.id)
        self.setgender()

    def splice(self):
        for i in self.genes:
            yield i[coinflip()]
            
    def die(self):
        del self.genes

    def setgender(self):
        if self.genes[22][0] & 1:
            raise RuntimeError("Extraenous Y chromosome found.")
        if self.genes[22][1] & 1:
            self.gender = MALE
        else:
            self.gender = FEMALE

    def inbred(self):
        inbred = 0
        for i in self.genes:
            if i[0] == i[1]:
                inbred += 1
        return inbred
