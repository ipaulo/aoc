from aocd import get_data

real_data = get_data(day=1).splitlines()

test = """199
200
208
210
200
207
240
269
260
263""".splitlines()

santa_sonar = real_data

santa_sonar = [int(i) for i in santa_sonar]
deeper = 0

a = santa_sonar[0]
for b in santa_sonar:
    if b > a:
        deeper += 1
        # print(b, "(increased)", deeper)
    else:
        # print(b, "no change", deeper)
        pass
    a = b

print("Part 1 answer:", deeper)

deeper = 0
prev = 0

for i in range(0, len(santa_sonar) - 2):
    r1 = santa_sonar[i]
    r2 = santa_sonar[i + 1]
    r3 = santa_sonar[i + 2]
    sum = r1 + r2 + r3
    if prev == 0:
        prev = sum
    if sum > prev:
        deeper += 1
        # print(sum, "(increased)", deeper)
    else:
        # print(sum, "no change")
        pass
    prev = sum

print("Part 2 answer:", deeper)
