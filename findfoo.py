done = False
bitnum = 3

while not done:
    print("bits:", bitnum)
    if not ((2 ** bitnum) % 3):
        done = True
    bitnum += 1
