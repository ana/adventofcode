

with open("input.txt") as f:
    data = [x.split() for x in f.read().splitlines()]

def part_one():
    horizontal = 0
    down = 0
    up = 0

    for d in data:
        word, number = d[0], int(d[1])

        if word == "forward":
            horizontal = horizontal + number
        elif word == "down":
            down = down + number
        elif word == "up":
            up = up + number
        else:
            print("Problem:", word, number)

    print("Solution part one:", horizontal*(down-up))



def part_two():
    horizontal = 0
    depth = 0
    aim = 0

    for d in data:
        word, number = d[0], int(d[1])

        if word == "forward":
            horizontal = horizontal + number
            depth = depth + number*aim
        elif word == "down":
            aim = aim + number
        elif word == "up":
            aim = aim - number
        else:
            print("Problem: ", word, number)

    print("Solution part two:", horizontal*depth)

part_one()
part_two()
