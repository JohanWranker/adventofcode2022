data = [l.rstrip() for l in open("day7/in.txt")]
import re

tree = {"/": [0]}
cwd_split = [""]
cwd = "/"
line_in_file = 1
file_length = len(data)


def ls():
    total_size = 0
    global line_in_file
    global file_length
    while line_in_file < file_length and "$" not in data[line_in_file]:
        if "dir " in data[line_in_file]:
            (_, dir) = data[line_in_file].split(" ")
            if cwd == "/":
                p = "/" + dir
            else:
                p = cwd + "/" + dir

            tree[p] = [0]
            tree[cwd].append(dir)
        else:
            (size, _) = data[line_in_file].split(" ")
            total_size += int(size)
            tree[cwd][0] = total_size
        line_in_file += 1


while line_in_file < file_length:
    line = data[line_in_file]
    if line[0] == "$":
        # command
        if "$ ls" in line:

            line_in_file += 1
            ls()
        elif "cd .." in line:
            cwd_split.pop()
            line_in_file += 1
        elif "cd " in line:
            (_, _, dir) = data[line_in_file].split(" ")
            cwd_split.append(dir)
            cwd = "/".join(cwd_split)
            line_in_file += 1


print(tree)
go = "/"


def calc_len(path):
    t = tree[path]
    total_length = t[0]
    for index in range(1, len(t)):
        if path == "/":
            p = "/" + t[index]
        else:
            p = path + "/" + t[index]
        l = calc_len(p)
        total_length += l

    print(path, total_length)


calc_len("")
