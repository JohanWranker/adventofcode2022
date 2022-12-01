#!/usr/bin/python3
import os

print(f"hello")


fd = open("day1/input.txt")

data = fd.readlines()


elvs = [0]
for line in data:
    print(line)
    if len(line) == 0 or line== "\n":
        print("next elf")
        elvs.append(0)
        continue
    elvs[-1] += int(line)


sortedElvs = sorted(elvs,reverse = True)
print(sortedElvs[0])
print(sortedElvs[1])
print(sortedElvs[2])
sum = sortedElvs[0] + sortedElvs[1] + sortedElvs[2]
print(sum)
    
