data = []
ds = open("day3/in.txt").readlines()


sum = 0
for l2 in ds:
    # print(l2)
    data = l2.strip()
    l = int(len(data) / 2)
    left = data[0:l]
    right = data[l:]
    for item in left:
        if item in right:
            # print(item)
            if item.islower():
                val = ord(item) - ord("a") + 1
            else:
                val = ord(item) - ord("A") + 27
            # print(f"item {item} v = {val}")
            sum += val
            break

print(sum)


sum = 0
index = 2
while index < len(ds):
    for item in ds[index].strip():
        if item in ds[index - 1] and item in ds[index - 2]:
            # print(item)
            if item.islower():
                val = ord(item) - ord("a") + 1
            else:
                val = ord(item) - ord("A") + 27
            # print(f"item {item} v = {val}")
            sum += val
            break

    index += 3

print(sum)
