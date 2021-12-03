# --- Day 3: Binary Diagnostic ---

from aocd import get_data
import numpy as np

# diag = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 20000
# 12001
# 00010
# 01010""".splitlines()

diag = get_data(day=3, year=2021).splitlines()

for x, line in enumerate(diag):
    s = []
    for char in line:
        s.append(int(char))
    diag[x] = s

data = np.array(diag)

x, y = data.shape
gamma = eps = "0b"

for column in range(0, y):
    a = np.flatnonzero(data[:, column]).size

    if a > (x / 2):
        gamma = gamma + "1"
        eps = eps + "0"
    else:
        gamma = gamma + "0"
        eps = eps + "1"

ans1 = int(gamma, 2) * int(eps, 2)
print(ans1)
