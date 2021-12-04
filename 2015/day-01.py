from aocd import get_data

santa = get_data(day=1, year=2015)

# santa = "(())"
# santa = "(()(()("
# ( up
# ) down
total = len(santa)

plus = len(santa.replace(")", ""))
floor = plus - (total - plus)


print("Part 1 Answer = ", floor)

floor = 0

for idx, value in enumerate(santa):
    if value == ")":
        floor = floor - 1
        if floor == -1:
            print("Part 2 Answer = ", idx + 1)
            break
    else:
        floor = floor + 1
