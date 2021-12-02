# --- Day 2: Dive! ---

from aocd import get_data

key = get_data(day=2, year=2021).splitlines()

f = depth = 0

for i in key:
    x, y = i.split()

    if x == "forward":
        f += int(y)
    else:
        if x == "down":
            depth += int(y)
        else:
            depth -= int(y)

ans1 = f * depth
print("Part 1 Answer = ", ans1)

f = depth = aim = 0

for i in key:
    x, y = i.split()

    if x == "forward":
        f += int(y)
        depth = depth + int(y) * aim
    else:
        if x == "down":
            aim += int(y)
        else:
            aim -= int(y)
ans2 = f * depth

print("Part 2 Answer = ", ans2)
