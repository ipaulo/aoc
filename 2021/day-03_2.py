# --- Day 3: Binary Diagnostic ---

# https://note.nkmk.me/en/python-numpy-where/

from aocd import get_data
import numpy as np

# diag = get_data(day=3, year=2021).splitlines()

diag = """00100
11110
10110
10111
10101
01111
00111
11100
20000
12001
00010
01010""".splitlines()

for x, line in enumerate(diag):
    s = []
    for char in line:
        s.append(int(char))
    diag[x] = s

d = np.array(diag)

x, y = d.shape
gamma = eps = "0b"


def signif(myarr, column):
    """Return true if 1 is more significant in the column"""

    x, y = myarr.shape
    a = np.flatnonzero(myarr[:, column]).size
    return a >= x / 2


for column in range(0, y):
    # hi = np.zero(d[:,0])
    # hi = np.delete(d,z,axis=0)
    # low = np.nonzero(d[:,0])
    # low = np.delete(d,z,axis=0)
    # a = np.flatnonzero(data[:,column]).size

    if signif(d, column):
        print(d, "---------")
        new = np.delete(d, np.where(d > 1)[1], axis=0)
        print(new)
        break
    else:
        gamma = gamma + "0"
        eps = eps + "1"

# print(gamma, eps)
# ans1 = int(gamma, 2) * int(eps, 2)
# print(ans1)

# c = np.arange(12).reshape((3, 4))
# print(c)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]

# print(np.delete(c, np.where(c < 2)[1], axis=1))
# # [[ 2  3]
# #  [ 6  7]
# #  [10 11]]

# print("Part 2 Answer = ", ans2)


# >>> diag = '''00100
# ... 11110
# ... 10110
# ... 10111
# ... 10101
# ... 01111
# ... 00111
# ... 11100
# ... 10000
# ... 11001
# ... 00010
# ... 01010'''.splitlines()
# >>>
# >>> for x, line in enumerate(diag):
# ...     s=[]
# ...     for char in line:
# ...         s.append(int(char))
# ...     diag[x] = s
# ...
# >>> data = np.array(diag)
# >>> print(data)
# [[0 0 1 0 0]
#  [1 1 1 1 0]
#  [1 0 1 1 0]
#  [1 0 1 1 1]
#  [1 0 1 0 1]
#  [0 1 1 1 1]
#  [0 0 1 1 1]
#  [1 1 1 0 0]
#  [1 0 0 0 0]
#  [1 1 0 0 1]
#  [0 0 0 1 0]
#  [0 1 0 1 0]]
# >>> d= np.array(diag)

# >>> np.nonzero(d[:,0])
# (array([1, 2, 3, 4, 7, 8, 9], dtype=int64),)

# >>> np.reduce(d,axis=(0,0),where=True)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "d:\anaconda3\envs\aoc\lib\site-packages\numpy\__init__.py", line 313, in __getattr__
#     raise AttributeError("module {!r} has no attribute "
# AttributeError: module 'numpy' has no attribute 'reduce'


# >>> print(d[np.all(d, axis=1)])
# []
# >>> print(d[np.all(d>0, axis=1)])
# []
# >>> d
# array([[0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 0],
#        [1, 0, 1, 1, 0],
#        [1, 0, 1, 1, 1],
#        [1, 0, 1, 0, 1],
#        [0, 1, 1, 1, 1],
#        [0, 0, 1, 1, 1],
#        [1, 1, 1, 0, 0],
#        [1, 0, 0, 0, 0],
#        [1, 1, 0, 0, 1],
#        [0, 0, 0, 1, 0],
#        [0, 1, 0, 1, 0]])

# >>> np.nonzero(d[:,0])
# (array([1, 2, 3, 4, 7, 8, 9], dtype=int64),)
# >>> z = np.nonzero(d[:,0])np.nonzero(d[:,0])
# KeyboardInterrupt
# >>> np.nonzero(d[:,0])
# KeyboardInterrupt
# >>> z = np.nonzero(d[:,0])
# >>> np.delete(d,z,axis=0)
# array([[0, 0, 1, 0, 0],
#        [0, 1, 1, 1, 1],
#        [0, 0, 1, 1, 1],
#        [0, 0, 0, 1, 0],
#        [0, 1, 0, 1, 0]])
# >>> d = np.array(diag)
# >>> z = np.nonzero(d[:,0])
# >>> np.where(d,z,axis=0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<__array_function__ internals>", line 4, in where
# TypeError: where() got an unexpected keyword argument 'axis'
# >>> np.where(d,z)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<__array_function__ internals>", line 5, in where
# ValueError: either both or neither of x and y should be given
# >>> np.delete(d,~z,axis=0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: bad operand type for unary ~: 'tuple'
# >>>
