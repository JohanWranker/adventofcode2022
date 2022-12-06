data = [l.rstrip() for l in open("day6/in.txt")]
import re

data =  open("day6/in.txt").readline()

count = 0
for index in range(0,len(data)):
    ok = True
    tokens = []
    for j in range (0,14):
        d = data[index+j]
        if d in tokens:
            ok = False
            break
        tokens.append(d)
    if ok:
        print(index+14)
        break

    