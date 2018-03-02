import uuid
import random
random.seed()

def coinflip():
	return random.randint(0, 1)
	
class Human():
	id = None
	father = None
	mother = None
	generation = None
	genes = None
	children = None

	def __init__(self, father=None, mother=None):
		self.id = uuid.uuid4()
		self.genes = [None] * 23
		self.children = []
		if father is None and mother is None:
			for pair in range(0, 22):
				self.genes[pair] = (uuid.uuid4(), uuid.uuid4())
			self.generation = 0
		else:
			if mother.generation > father.generation:
				self.generation = mother.generation + 1
			else:
				self.generation = father.generation + 1
			for pair in range(0, 22):
				self.genes[pair] = (father.genes[pair][coinflip()], mother.genes[pair][coinflip()])
			self.father = father.id
			self.mother = mother.id
			father.children.append(self.id)
			mother.children.append(self.id)
