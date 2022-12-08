data = [l.rstrip() for l in open("day7/in.txt")]
import re

cwd_split = [""]
cwd = "/"
sizes = {"/": 0}

for line in data:
    if line[0] == "$":
        # command
        if "$ ls" in line:
            pass
        elif "$ cd .." in line:
            sub_size = sizes[cwd]
            cwd_split.pop()
            cwd = "/".join(cwd_split)
            if cwd == "//":
                cwd = "/"
        elif "$ cd " in line:
            dd = line.split(" ")
            cwd_split.append(dd[-1])
            cwd = "/".join(cwd_split)
            assert cwd not in sizes
            sizes[cwd] = 0
        else:
            assert False
    else:
        if "dir " in line[0:4]:
            (_, dir) = line.split(" ")
        else:
            (size, _) = line.split(" ")
            sizes[cwd] = sizes[cwd] + int(size)


print(sizes)
sum = 0
for i in sizes:
    if sizes[i] <= 100000:
        sum += sizes[i]
    else:
        print(i, sizes[i])

print(sum)
