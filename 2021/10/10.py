
with open("input.txt") as f:
    data = f.read().splitlines()

subs = ["<>", "{}", "()", "[]"]
openings = ['{', '[', '(', '<']
closings =['}', ']', ')', '>']

def rec(linea):
    if any([x in linea for x in subs]):
        if '<>' in linea:
            ll = linea.replace('<>','')
            return rec(ll)
        elif '()' in linea:
            ll = linea.replace('()','')
            return rec(ll)
        elif '[]' in linea:
            ll = linea.replace('[]','')
            return rec(ll)
        elif '{}' in linea:
            ll = linea.replace('{}','')
            return rec(ll)
    else:
        return linea

def process (results):

    points = 0
    for cadena in results:
        for c in range(len(cadena)-1):
            if cadena[c] in openings and cadena[c+1] in closings:
                if cadena[c+1] == ')':
                    points += 3
                elif cadena[c+1] == ']':
                    points += 57
                elif cadena[c+1] == '}':
                    points += 1197
                elif cadena[c+1] == '>':
                    points += 25137
                break

    return points

def remove_corrupt_lines(results):

    incomplete = []
    for cadena in results:
        corrupt = False
        for c in range(len(cadena)-1):
            if cadena[c] in openings and cadena[c+1] in closings:
                corrupt = True
                continue
        if not corrupt:
            incomplete.append(cadena)

    return incomplete


def process2 (results):

    points = []
    for cadena in results:
        p = 0
        for c in range(len(cadena)-1, -1, -1):
            p *= 5
            if cadena[c] == '(':
                p += 1
            elif cadena[c] == '[':
                p += 2
            elif cadena[c] == '{':
                p += 3
            elif cadena[c] == '<':
                p += 4
        points.append(p)

    return sorted(points)

results = []
for l in data:
    results.append(rec(l))

points = process(results)

print("Part one: ", points, "points")

incomplete_lines = remove_corrupt_lines(results)
list_points2 = process2(incomplete_lines)
l = int((len(list_points2) - 1)/2)
print("Part two: ", list_points2[l])
