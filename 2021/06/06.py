import numpy

days = 80

def laternfish_update(group):

    size = len(group)
    new = []
    for i in range(0, size):
        if group[i] > 0:
            group[i] = group[i] -1
        elif group[i] == 0:
            group[i] = 6
            new.append(8)

    if new == []:
        return group
    else:
        n = numpy.array(new, dtype=int)
        return numpy.concatenate([group, n])


with open("input.txt") as f:
    data = f.readline().strip()
start =[int(d) for d in data.split(",")]

#group=numpy.array(start, dtype=int)

total = 0
for d in start:
    dd = numpy.array([d], dtype=int)
    for day in range(1,days+1):
        dd = laternfish_update(dd)
        if day == days:
            total += len(dd)

print("Part one result is: ", total)


