data = [l.rstrip() for l in open("day7/in.txt")]
import re

cwd_split = ["/"]
cwd = "/"
sizes = {"/": 0}


def store_filesize(cmd_split, file_size):

    path = "/".join(cmd_split)
    print(path)
    sizes[path] += file_size
    a = cmd_split[0:-1]
    if len(a) > 0:
        store_filesize(a, file_size)


for line in data:
    if line[0] == "$":
        # command
        if "$ ls" in line:
            pass
        elif "$ cd .." in line:
            sub_size = sizes[cwd]
            cwd_split.pop()
            # cwd = "/".join(cwd_split)
            # if cwd == "//":
            #    cwd = "/"
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
            store_filesize(cwd_split, int(size))
#            sizes[cwd] = sizes[cwd] + int(size)
#
#            sub_size = sizes[cwd]
#            cwd_split.pop()
#            cwd = "/".join(cwd_split)
#            if cwd == "//":
#                cwd = "/"


print(sizes)
sum = 0
unused = 70000000 - sizes["/"]
needed = 30000000 - unused
close_match = 70000000
for i in sizes:
    if sizes[i] >= needed and sizes[i] < close_match:
        close_match = sizes[i]

print(sum)

needed = 70000000 - 30000000
print(needed)
print(close_match)
