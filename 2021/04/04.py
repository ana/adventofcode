def winner(carton):
    ss = 0
    for linea in carton:
        s = 0
        ss += linea[2][1]
        for l in linea:
            s += l[1]
        if s == 5:
            return True
    if ss == 5:
        return True

    return False

def rellena_carton(carton, bolas):
    steps = 0

    for b in range(0, len(bolas)):
        for linea in carton:
            for n in linea:
                if bolas[b] == n[0]:
                    n[1] = 1
        if winner(carton):
            steps = b
            break

    suma0 = 0
    for linea in carton:
        for n in linea:
            if n[1] == 0:
                print(n)
                suma0 += n[0]
    suma0 = suma0* bolas[steps]

    return {steps:suma0}

with open("tinput.txt") as f:
    data = f.read().splitlines()

bolas = [int(x) for x in data[0].split(",")]
resultados = []

for l in range(2, len(data[2:]), 6):
    carton = []
    for i in range(0,5):
        # carton es una lista de 5 listas donde cada numero es la clave de un diccionario
        carton.append([[int(xx),0] for xx in data[l+i].split(" ")  if xx !='' ])
    resultados.append(rellena_carton(carton, bolas))

print("Part 1 result:", min(resultados, key=lambda x: x[0])[1])
print("Part 2 result:", max(resultados, key=lambda x: x[0])[1])
~

