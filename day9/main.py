data = [l.rstrip() for l in open("day9/in.txt")]
import re
from numpy import *
import numpy


# row, col
true_table = [
    [1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0],
]
head = [0, 0]
tail = [0, 0]
visit = {"0x0": 1}
one_of_table = {"R": [0, 1], "L": [0, -1], "D": [-1, 0], "U": [1, 0]}

for line in data:
    direction = line[0]
    steps = int(line[2])
    vector = one_of_table[direction]

    if line in "L 3":
        print("here")
    for loop in range(steps):

        # move
        head[0] += vector[0]
        head[1] += vector[1]

        diff = [head[0] - tail[0], head[1] - tail[1]]
        if abs(diff[0]) < 2 and abs(diff[1]) < 2:
            continue
        step = [0, 0]
        step[0] = int(diff[0] / abs(diff[0])) if diff[0] != 0 else 0
        step[1] = int(diff[1] / abs(diff[1])) if diff[1] != 0 else 0

        tail[0] += step[0]
        tail[1] += step[1]

        #if true_table[tail[0]][tail[1]] == 0:
        #    assert False

        pos_array = f"{tail[0]}x{tail[1]}"
        if pos_array not in visit:
            visit[pos_array] = 1
        else:
            visit[pos_array] += 1

print(len(visit))
