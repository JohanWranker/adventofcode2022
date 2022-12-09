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

visit = {"0x0": 1}
one_of_table = {"R": [0, 1], "L": [0, -1], "D": [-1, 0], "U": [1, 0]}


class Knot:
    def __init__(self):
        # self.head = [0, 0]
        self.tail = [0, 0]

    def move_pos(self, row, col):
        self.tail[0] += row
        self.tail[1] += col

    def follow(self, row, col):
        diff = [row - self.tail[0], col - self.tail[1]]
        if abs(diff[0]) < 2 and abs(diff[1]) < 2:
            pass
        else:
            step = [0, 0]
            step[0] = int(diff[0] / abs(diff[0])) if diff[0] != 0 else 0
            step[1] = int(diff[1] / abs(diff[1])) if diff[1] != 0 else 0

            self.tail[0] += step[0]
            self.tail[1] += step[1]

            diff2 = [row - self.tail[0], col - self.tail[1]]
            if abs(diff2[0]) > 2 or abs(diff2[1]) > 2:
                assert False

            # if true_table[tail[0]][tail[1]] == 0:
            #    assert False


length = 9
list = []
for index in range(length + 1):
    list.append(Knot())

for line in data:
    l = line.split(" ")
    direction = l[0]
    steps = int(l[1])
    vector = one_of_table[direction]

    if line in "L 3":
        print("here")
    for loop in range(steps):

        list[0].move_pos(vector[0], vector[1])
        for index in range(1, length + 1):
            list[index].follow(list[index - 1].tail[0], list[index - 1].tail[1])
        # move

        pos_array = f"{list[-1].tail[0]}x{list[-1].tail[1]}"
        visit[pos_array] = "x"

print(len(visit))
