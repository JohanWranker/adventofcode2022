data = []
ds = open("day3/in.txt").readlines()
for d in ds:
    data = d.strip()


sum = 0
for l2 in ds:
    print(l2)
    data = l2.strip()
    l = int(len(data) / 2)
    left = data[0:l]
    right = data[l:]
    for item in left:
        if item in right:
            print(item)
            if item.islower():
                val = ord(item) - ord("a") + 1
            else:
                val = ord(item) - ord("A") + 27
            print(f"item {item} v = {val}")
            sum += val
            break

print(sum)
