from object import Human, MALE, FEMALE
import sys
import time

runs = 10000

inbred = {}

g00 = Human(gender=MALE)
g01 = Human(gender=FEMALE)
for i in range(runs):
    sys.stdout.write("Running simulation... %d%%\r" % ((i+1) * 100 / runs))
    sys.stdout.flush()
    g10 = Human(g01, g00, gender=FEMALE)
    g11 = Human(g01, g00, gender=FEMALE)
    g20 = Human(g10, Human(gender=MALE), gender=FEMALE)
    g21 = Human(g11, Human(gender=MALE), gender=FEMALE)
    g30 = Human(g20, Human(gender=MALE), gender=FEMALE)
    g31 = Human(g21, Human(gender=MALE), gender=FEMALE)
    g40 = Human(g30, Human(gender=MALE), gender=MALE)
    g41 = Human(g31, Human(gender=MALE), gender=FEMALE)
    g50 = Human(g41, g40)
    coff = g50.inbred()
    if coff in inbred:
    	inbred[coff] += 1
    else:
        inbred[coff] = 1
print("\n")
inbred = {i: inbred[i] for i in sorted(inbred)}
for i in inbred:
	print(i, ":", inbred[i])
