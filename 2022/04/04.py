

with open("04.txt") as f:
    lines = [str(x) for x in f.read().splitlines()]

total1 = 0
total2 = 0

for l in lines:
    x, y = l.split(",")
    xa, xb = x.split("-")
    ya, yb = y.split("-")

    xx = set()
    yy = set()

    for i in range(int(xa), int(xb)+1):
        xx.add(i)
    for i in range(int(ya), int(yb)+1):
        yy.add(i)

    if xx.issubset(yy) or yy.issubset(xx):
        total1 = total1 +1

    for i in xx:
        if i in yy:
            total2 = total2 +1
            break
        else:
            continue
print(total1)
print(total2)
