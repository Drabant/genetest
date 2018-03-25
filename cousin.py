from object import Human, MALE, FEMALE
import sys
import time

runs = 1000

inbred = {}

for i in range(runs):
    sys.stdout.write("Running simulation... %d%%\r" % (i * 100 / runs))
    sys.stdout.flush()
    g00 = Human(gender=MALE)
    g01 = Human(gender=FEMALE)
    g10 = Human(g01, g00, gender=FEMALE)
    g11 = Human(g01, g00, gender=FEMALE)
    g12 = Human(gender=MALE)
    g13 = Human(gender=FEMALE)
    g21 = Human(g10, g12, gender=MALE)
    g22 = Human(g11, g13, gender=FEMALE)
    g30 = Human(g22, g21)
    coff = g30.inbred()
    if coff in inbred:
    	inbred[coff] += 1
    else:
        inbred[coff] = 1
print("\n")
inbred = {i: inbred[i] for i in sorted(inbred)}
for i in inbred:
	print(i, ":", inbred[i])
