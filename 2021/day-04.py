# --- Day 4: Giant Squid ---

from aocd import get_data

boards = []
winners = []

file = get_data(day=4, year=2021).splitlines()

call_string = file[0]
calls = list(map(int, call_string.split(",")))


for x in range(2, 600, 6):
    lines = file[x : x + 5]
    for x, s in enumerate(lines):
        lines[x] = list(map(int, s.split()))
    boards.append(lines)


def happy(card, row, colnum):

    if sum(row) == -5:
        return True
    else:
        t = 0
        for x in range(0, len(card)):
            t += card[x][colnum]
        if t == -5:
            return True

    return False


def mark(card, call):
    global boards
    for x, row in enumerate(card):
        for s, spot in enumerate(row):
            if spot == call:
                card[x][s] = -1

                if happy(card, row, s):
                    return True
    return False


def unmarked_sum(t):
    board_sum = 0
    for sublist in t:
        for item in sublist:
            if item > 0:
                board_sum += item
    return board_sum


def calc_score(card, lastcall):

    return unmarked_sum(card) * lastcall


def mark_all(my_boards, call):
    global winners, boards

    for x, board in enumerate(my_boards):
        if mark(board, call):

            score = calc_score(board, call)
            if score not in winners:
                winners.append(score)
                boards.pop(x)


for call in calls:
    mark_all(boards, call)

ans1 = winners[0]
ans2 = winners[-1]

print("Part 1 Answer = ", ans1)
print("Part 2 Answer = ", ans2)
