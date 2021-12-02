# --- Day 2: Dive! ---

from aocd import get_data

key = get_data(day=2, year=2021).splitlines()

f = depth = 0

for i in key:
    x, y = i.split()
    y = int(y)
    if x == "forward":
        f += y
    else:
        if x == "down":
            depth += y
        else:
            depth -= y

ans1 = f * depth
print("Part 1 Answer = ", ans1)

f = depth = aim = 0

for i in key:
    x, y = i.split()
    y = int(y)

    if x == "forward":
        f += y
        depth = depth + y * aim
    else:
        if x == "down":
            aim += y
        else:
            aim -= y
ans2 = f * depth

print("Part 2 Answer = ", ans2)
