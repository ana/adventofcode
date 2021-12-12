import pprint

def check_paths(grafo):
    paths = []
    ongoing = [['start']]

    while ongoing:
        p = ongoing.pop(0)
        ultimo = p[-1]

        if ultimo == 'end':
            paths.append(p)
            continue

        for e in grafo[ultimo]:
            if e != 'start':
                if e in p and e.islower():
                    continue
                else:
                    new = p.copy()
                    new.append(e)
                    ongoing.append(new)

    return paths

def one_small_cave(pp):
    if pp is None:
        return False
    elif len(set(pp)) == len(pp):
        return False
    else:
        for e in pp:
            if pp.count(e) > 1 and e.islower():
                    return True

    return False

def check_paths2(grafo):
    paths = []
    ongoing = [['start']]

    while ongoing:
        p = ongoing.pop(0)
        ultimo = p[-1]

        if ultimo == 'end':
            paths.append(p)
            continue

        for e in grafo[ultimo]:
            if e != 'start':
                if e in p and e.islower() and one_small_cave(p.copy()):
                    continue
                else:
                    new = p.copy()
                    new.append(e)
                    ongoing.append(new)

    return paths

####
with open("input.txt") as f:
    data = f.read().splitlines()

data = [e.split("-") for e in data]
elements = set([e for x in data for e in x])

grafo = {}
for key in elements:
    grafo[key] = []

for e in data:
    a,b = e
    grafo[a].append(b)
    grafo[b].append(a)

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(grafo)

caminos = check_paths(grafo)
#pp.pprint(caminos)
print("part one: paths: ", len(caminos))

caminos = check_paths2(grafo)
print("part two: paths: ", len(caminos))


