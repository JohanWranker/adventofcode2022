data = [l.rstrip() for l in open("day5/in.txt")]
import re


end_of_crates = 0
no_of_stacks_float = 0
for line in data:
    stacks_count = line.split(" ")
    if stacks_count[1] == "1":
        no_of_stacks = int(stacks_count[-1])
        break
    end_of_crates += 1

print(end_of_crates)
print(no_of_stacks)

stacks = []
for i in range(0, no_of_stacks):
    stacks.append([])

for row in range(end_of_crates - 1, -1, -1):
    line = data[row]
    for index in range(0, no_of_stacks):
        location = index * 4 + 1
        if len(line) < location:
            continue
        a = stacks[index]
        b = line[location]
        if b != " ":
            a.append(line[location])
            stacks[index] = a

for index in range(end_of_crates + 2, len(data)):
    m = re.match(r"move (\d+) from (\d+) to (\d+)", data[index])
    print(m.groups())
    for count in range(0, int(m.group(1))):
        x = stacks[int(m.group(2)) - 1].pop()
        stacks[int(m.group(3)) - 1].append(x)

        a = ""
for s in stacks:
    a += s[-1]


print(a)
