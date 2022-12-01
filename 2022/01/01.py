
e = []

with open("01.txt") as f:
    l = [x for x in f.read().splitlines()]

sum = 0

for i in range(0, len(l)):
    if l[i] == '':
        e.append(sum)
        sum = 0
    else:
        sum = sum + int(l[i])

print(max(e))

ordered = sorted(e, reverse=True)
print(ordered[0] + ordered[1] + ordered[2])
