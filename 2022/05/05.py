from collections import deque


with open("input.txt") as f:
    lines = [str(x) for x in f.read().splitlines()]

moves = lines[10:]
piles = [None,
         deque(["T", "P", "Z", "C", "S", "L", "Q", "N"]),
         deque(["L", "P", "T", "V", "H", "C", "G"]),
         deque(["D", "C", "Z", "F"]),
         deque(["G", "W", "T", "D", "L", "M", "V", "C"]),
         deque(["P", "W", "C"]),
         deque(["P", "F", "J", "D", "C", "T", "S", "Z"]),
         deque(["V", "W", "G", "B", "D"]),
         deque(["N", "J", "S", "Q", "H", "W"]),
         deque(["R", "C", "Q", "F", "S", "L", "V"])]


def one(moves, piles):
    for l in moves:
        m = l.split(" ")
        times = int(m[1])
        frm = int(m[3])
        to = int(m[5])

        for i in range(0, times):
            pile_from = piles[frm]
            pile_to = piles[to]

            elem = pile_from.pop()
            pile_to.append(elem)

            piles[frm] = pile_from
            piles[to] = pile_to

    for e in piles:
        print(e, "\n")


def two(moves, piles):
    for l in moves:
        print(l, "\n")
        m = l.split(" ")
        times = int(m[1])
        frm = int(m[3])
        to = int(m[5])

        bffr = []
        pile_from = piles[frm]
        piles_to = piles[to]

        for i in range(0, times):
            elem = pile_from.pop()
            bffr.append(elem)

        piles[frm] = pile_from

        bffr = reversed(bffr)
        piles_to.extend(bffr)
        piles[to] = piles_to

    for e in piles:
        print(e, "\n")


two(moves, piles)
