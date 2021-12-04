# -*- coding: utf-8 -*-

# --- Day 4: The Ideal Stocking Stuffer ---

from aocd import get_data
from hashlib import md5

import itertools

key = get_data(day=4, year=2015)


def hunt(key, start, goal):
    i = itertools.count(start)
    slice = len(goal)
    for x in i:
        s = (key + str(x)).encode("utf8")
        n = md5(s).hexdigest()
        v = str(n)[:slice]

        if v == goal:
            break
    ans = x

    return ans


ans1 = hunt(key, 1, "00000")

print("Part 1 Answer = ", ans1)

ans2 = hunt(key, ans1, "000000")

print("Part 2 Answer = ", ans2)
