data = []
ds = open("day4/in.txt").readlines()


def sp(data):
    f = []
    left_start, left_end = data.split("-")
    for hh in range(int(left_start), int(left_end) + 1):
        f.append(int(hh))

    return f


sum = 0
full = 0
for d in ds:
    found = 0
    left, right = d.strip().split(",")
    ll = sp(left)
    rl = sp(right)
    for i in ll:
        if i in rl:
            found = 1
            continue
    for i in rl:
        if i in ll:
            found = 1
            continue
    if found:
        sum += 1

print(sum)

for d in ds:
    l = left.split("-")
    left_start = int(l[0])
    left_end = int(l[1])
    # left_start, left_end = [left.split("-")]
    l = right.split("-")
    right_start = int(l[0])
    right_end = int(l[1])
    # right_start, right_end = [right.split("-")]
    if (
        (left_start <= right_start)
        and (right_start <= left_end)
        and (left_start <= right_end)
        and (right_end <= left_end)
    ):
        sum += 1
        found = 1

    elif (
        (right_start <= left_start)
        and (left_start <= right_end)
        and (right_start <= left_end)
        and (left_end <= right_end)
    ):
        sum += 1
        found = 2

    left_in = left_start >= right_start
    left_in = left_in and left_end <= right_end
    if left_in:
        full += 1
        if found == 0:
            print("")
        continue

    right_in = right_start >= left_start
    right_in = right_in and right_end <= left_end
    if right_in:
        full += 1
        if found == 0:
            print("")


print(sum)
print(full)
