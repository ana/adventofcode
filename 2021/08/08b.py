import re, sys

def get_key(val, dicc):
    for key, value in dicc.items():
         if val == value:
             return key


def process_line(signals, aux, codigo):

    for e in signals:
        l = len(e)
        if l == 2:  # Possible 0
            codigo[e] = 1
        elif l == 3:
            codigo[e] = 7
        elif l == 4:
            codigo[e] = 4
        elif l == 7:
            codigo[e] = 8
        elif l == 5:
            aux[5].append(e)
        elif l == 6:
            aux[6].append(e)

    # Para calcular el 3 (5 p), uso el 1 (2 p)
    uno = get_key(1, codigo)
    for e in aux[5]:
        if uno[0] in e and uno[1] in e:
            codigo[e] = 3
            aux[5].remove(e)
            break

    # Para calcular el 9 (6p) uso el 3(5p)
    tres = get_key(3, codigo)
    for e in aux[6]:
        if (tres[0] in e and tres[1] in e and tres[2] in e and tres[3] in e and tres[4] in e):
            codigo[e] = 9
            aux[6].remove(e)
            break


    # Para calcular 0 (6p), uso el 7(3p)
    siete = get_key(7, codigo)
    for e in aux[6]:
        if (siete[0] in e and siete[1] in e and siete[2] in e):
            codigo[e] = 0
            aux[6].remove(e)
            break

    # Queda el 6 de 6p
    codigo[aux[6][0]] = 6

    # quedan 2 y 5 con con 5p

    # Para calcular 5 (5p), uso el 6 (6p)
    seis = aux[6][0]
    for e in aux[5]:
        if (e[0] in seis and e[1] in seis \
            and e[2] in seis and e[3] in seis \
            and e[4] in seis):
            codigo[e] = 5
            aux[5].remove(e)
            break

    # Queda el 2 de 5p
    codigo[aux[5][0]] = 2

    return codigo


def sort_string_lists(sl):
    final = []
    for s in sl:
        s = sorted(s)
        final.append("".join(s))

    return final


def calculate_output(output, codigo):
    r = []
    for e in output:
        r.append(codigo[e])

    return r


with open("input.txt") as f:
    data = f.read().splitlines()

results = []
for line in data:
    signals, output = line.split("|")
    signals = signals.strip(" ").split(" ")
    output = output.strip(" ").split(" ")
    signals = sort_string_lists(signals)
    output = sort_string_lists(output)
    aux = {5:[], 6:[]}
    codigo = {}
    codigo = process_line(signals, aux, codigo)
    r = calculate_output (output,codigo)
    results.append(r)

total = 0
for r in results:
    total += int("".join([str(x) for x in r]))

print("Part two:", total)

