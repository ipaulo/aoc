# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

from aocd import get_data

nog = get_data(day=3, year=2015)
# nog = "^v^v^v^v^v"
ans1 = 1
ans2 = 0
print(len(nog) / 2)
# north (^), south (v), east (>), or west (<)

loc = tuple([0, 0])
loc1 = loc2 = tuple([0, 0])
deliv = {loc1}

dirs = {"^": [0, 1], "v": [0, -1], ">": [1, 0], "<": [-1, 0]}

# PART 1

for s in nog:
    dir = dirs[s]
    x, y = loc1
    a = dir[0]
    b = dir[1]
    # print(loc, s, deliv)
    loc1 = tuple([x + a, y + b])
    deliv.add(loc1)

ans1 = len(deliv)
print("Part 1 Answer = ", ans1)

# PART 2


def move(start, d):
    x, y = start
    dir = dirs[d]
    a = dir[0]
    b = dir[1]
    new = tuple([x + a, y + b])
    deliv.add(new)
    return new


def part2():
    global loc1, loc2
    for i in range(0, int(len(nog)), 2):
        loc1 = move(loc1, nog[i])
        loc2 = move(loc2, nog[i + 1])
        # print(i, nog[i], nog[i + 1])


loc1 = loc2 = tuple([0, 0])
deliv = {loc1}
part2()

ans2 = len(deliv)
print("Part 2 Answer = ", ans2)
