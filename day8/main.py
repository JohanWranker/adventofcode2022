data = [l.rstrip() for l in open("day8/in.txt")]
import re


# row then col

tree = []
seen = []
max_row = len(data)
for line in data:
    max_col = len(line)
    tree.append([])
    seen.append([])
    for index in range(0, max_col):
        tree[-1].append(int(line[index]))
        seen[-1].append(0)

print(tree)

if True:
    for row in range(max_row):
        for high in range(9, -1, -1):
            for col in range(max_col):
                if tree[row][col] >= high:
                    seen[row][col] += 1
                    break

if True:
    for row in range(max_row):
        for high in range(9, -1, -1):
            for col in range(max_col - 1, -1, -1):
                if tree[row][col] >= high:
                    seen[row][col] += 1
                    break

if True:
    for col in range(max_col):
        for high in range(9, -1, -1):
            for row in range(max_row):
                if tree[row][col] >= high:
                    seen[row][col] += 1
                    break

if True:
    for col in range(max_col):
        for high in range(9, -1, -1):
            for row in range(max_row - 1, -1, -1):
                if tree[row][col] >= high:
                    seen[row][col] += 1
                    break

sum = 0
for row in range(max_row):
    for col in range(max_col):
        if seen[row][col] > 0:
            sum += 1


print(seen)
print(sum)


def look_up(r, c):
    hight = tree[r][c]
    sum = 0
    while True:
        r -= 1
        if r < 0:
            break
        sum += 1
        if tree[r][c] >= hight:
            break
    return sum


def look_down(r, c):
    hight = tree[r][c]
    sum = 0
    while True:
        r += 1
        if r >= max_row:
            break
        sum += 1
        if tree[r][c] >= hight:
            break
    return sum


def look_left(r, c):
    hight = tree[r][c]
    sum = 0
    while True:
        c -= 1
        if c < 0:
            break
        sum += 1
        if tree[r][c] >= hight:
            break
    return sum


def look_right(r, c):
    hight = tree[r][c]
    sum = 0
    while True:
        c += 1
        if c >= max_col:
            break
        sum += 1
        if tree[r][c] >= hight:
            break
    return sum


val = []
max = 0
for row in range(max_row):
    val.append([])
    for col in range(max_col):
        a = look_right(row, col)
        b = look_left(row, col)
        c = look_down(row, col)
        d = look_up(row, col)
        mul = a * b * c * d
        if mul > max:
            max = mul
        val[-1].append(mul)

print(val)
print(max)
