# --- Day 2: I Was Told There Would Be No Math ---

from aocd import get_data

box = get_data(day=2, year=2015).splitlines()


def area(list):
    list = sorted(list)
    l = list[0]
    w = list[1]
    h = list[2]

    areas = (l * w, l * h, w * h)
    area = 2 * sum(areas) + min(areas)

    ribbon = 2 * (l + w) + (l * w * h)
    return area, ribbon


ans1 = 0
ans2 = 0

for line in box:
    sides = line.split("x")
    sides = list(map(int, sides))
    a, b = area(sides)
    ans1 += a
    ans2 += b

print("Part 1 Answer = ", ans1)

print("Part 2 Answer = ", ans2)
