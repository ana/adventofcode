
# Part one
def calculate_distances(cs, mp):
    dicc = {}

    for i in range(0, mp+1):
        if i > cs:
            dicc[i] = i-cs
        else:
            dicc[i] = cs-i
    return dicc

# Part two
def calculate_distances2(cs, mp):
    dicc = {}

    for i in range(0, mp+1):
        if i > cs:
            diff = i-cs
        else:
            diff = cs-i
        
        dicc[i] =(diff*(diff+1))/2

    return dicc


with open("input.txt") as f:
    data = f.readline().strip()
start =[int(d) for d in data.split(",")]

max_position=max(start)
costes={}

for i in range(0, max_position+1):
    if i in start:
        costes[i] = calculate_distances2(i, max_position)

tcost = {}
for pos in range(0, max_position+1):
    tcost[pos] = sum([costes[i][pos] for i in start])

position=0
value=tcost[0]
for p, v in tcost.items():
    if v < value:
        value = v
        position = p

print("Position ", position, "is the one using less fuel: ", value)
