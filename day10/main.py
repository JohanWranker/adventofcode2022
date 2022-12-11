data = [l.rstrip() for l in open("day10/in.txt")]
import re
from numpy import *
import numpy

tick = 0
x = ['-']
X = 1
line_screen = []
sum2 = 0
def add_pos(pos):
    global line_screen, sum2
    line_screen += "x" if abs(pos - X) < 2 else " "
    index = pos+1
    if index in [20,60,100,140,180,220]:
        sum2 += index*X


for line in data:
    x.append(X)
    add_pos(len(x)-1)
    if "noop" in line:
        continue
    (cmd, value_str) = line.split(" ")
    x.append(X)
    add_pos(len(x)-1)
    X += int(value_str)

[print(v[1],end="\n" if (v[0]%40==0) else "") for v in enumerate(line_screen)]
sum = 0
for index in [20,60,100,140,180,220]:
    sum += index*x[index]
print(sum)
print(sum2)
exit()
screen = [] 
for row in range (6):
    screen.append([])
    for p in range(40):
        screen[-1].append(' ')

for pos in range(len(x)):
    (loop,pos_in_loop) = divmod(pos,6*40)
    (row,col) = divmod(pos_in_loop, 40)
    if abs(x[pos+1]-col) < 2:
        screen[row][col] = 'x'

print(screen)

str =""
for row in range (6):
    print(str)
    str = ""
    for p in range(40):
        str += screen[row][p]
print(str)