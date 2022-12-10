data = [l.rstrip() for l in open("day10/in.txt")]
import re
from numpy import *
import numpy

tick = 0
x = []
X = 1

for line in data:
    x.append(X)
    if "noop" in line:
        continue
    (cmd, value_str) = line.split(" ")
    x.append(X)
    X += int(value_str)

print(x)
print(x[20])
print(x[40])
print(x[60])
#assert x[20] == 21
#assert x[60] == 19
#assert x[100] == 18
#assert x[140] == 21
#assert x[180] == 16
#assert x[220] == 18
sum = 0
for index in [20,60,100,140,180,220]:
    sum += index*x[index]
print(sum)

screen = [] 
for row in range (6):
    screen.append([])
    for p in range(40):
        screen[-1].append(' ')

for pos in range(len(x)):
    (loop,pos_in_loop) = divmod(pos,6*40)
    (row,col) = divmod(pos_in_loop, 40)
    if abs(x[pos]-col) < 2:
        screen[row][col] = 'x'

print(screen)

str =""
for row in range (6):
    print(str)
    str = ""
    for p in range(40):
        str += screen[row][p]
print(str)