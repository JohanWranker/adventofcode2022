data = [l.rstrip() for l in open("day7/in.txt")]
import re

tree = {"/": [0]}
cwd_split = [""]
cwd = "/"
line_in_file = 1
file_length = len(data)
sizes = {"/": 0}

while line_in_file < file_length:
    line = data[line_in_file]
    if line[0] == "$":
        # command
        if "$ ls" in line:
            pass
        elif "cd .." in line:
            sub_size = sizes[cwd]
            cwd_split.pop()
            cwd = "/".join(cwd_split)
            if cwd == "//":
                cwd = "/"
        elif "cd " in line:
            dd = data[line_in_file].split(" ")
            cwd_split.append(dd[-1])
            cwd = "/".join(cwd_split)
            assert cwd not in sizes
            sizes[cwd] = 0
        else:
            assert False
    else:
        if "dir " in data[line_in_file]:
            (_, dir) = data[line_in_file].split(" ")
        else:
            (size, _) = data[line_in_file].split(" ")
            sizes[cwd] = sizes[cwd] + int(size)
    line_in_file += 1


print(sizes)
sum = 0
for i in sizes:
    if sizes[i] <= 100000:
        sum += sizes[i]
    else:
        print(i, sizes[i])

print(sum)
