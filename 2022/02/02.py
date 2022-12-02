
# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors.
# 1 for Rock, 2 for Paper, and 3 for Scissors


with open("02.txt") as f:
    l = [x for x in f.read().splitlines()]

total = 0

for p in l:
    t = 0

    if p == 'A X':
        t = 1 + 3
    elif p == 'A Y':
        t = 2 + 6
    elif p == 'A Z':
        t = 3

    elif p == 'B X':
        t = 1 
    elif p == 'B Y':
        t = 2 + 3
    elif p == 'B Z':
        t = 3 + 6

    elif p == 'C X':
        t = 1 + 6
    elif p == 'C Y':
        t = 2
    elif p == 'C Z':
        t = 3 + 3

    total = total + t

print(total)


# X lose, Y  draw, and Z win

total = 0

for p in l:
    t = 0


    if p == 'A X':
        t = 0 + 3
    elif p == 'A Y':
        t = 3 + 1
    elif p == 'A Z':
        t = 6 + 2

    elif p == 'B X':
        t = 0 + 1
    elif p == 'B Y':
        t = 3 + 2
    elif p == 'B Z':
        t = 6 + 3

    elif p == 'C X':
        t = 0 + 2
    elif p == 'C Y':
        t = 3 + 3
    elif p == 'C Z':
        t = 6 + 1

    total = total + t

print(total)
