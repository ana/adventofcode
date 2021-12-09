import numpy

with open("input.txt") as f:
    data = f.read().splitlines()

ancho = len(data[0].strip())
alto = len(data)

m=numpy.zeros(shape=(alto,ancho), dtype=int)
for x in range(alto):
    linea = data[x]
    for y in range(ancho):
        num = linea[y]
        m[x][y] = num

def check_element(x,y):
    l = []
    for i,j in [(x,y-1), (x, y+1), (x-1,y), (x+1,y)]:
            if (0 <= j < ancho) and (0 <= i < alto):
                l.append(m[i,j])
    return ( m[x,y] < min(l) )

def hoyos():
    lows = []
    value = 0
    for x in range(alto):
        for y in range(ancho):
            if check_element(x,y):
                lows.append([x,y])
                value += 1 + m[x,y]
    return value, lows

def check_basin(estado, inicio):
    size = 0
    to_visit = [inicio]

    while to_visit:
        [i, j] = to_visit.pop(0)

        if estado[i,j]:
            continue

        estado[i,j] = True # Marco que ya pertenece a un "basin"
        size += 1

        for ii,jj in [(i,j-1), (i, j+1), (i-1,j), (i+1,j)]:
            if (ii < 0 or jj < 0 or ii >= alto or jj >= ancho) \
                    or m[i,j] >= m[ii,jj]:
                continue

            to_visit.append([ii, jj])

    return size

value, lhoyos = hoyos()
print("Part one result: ", value)

lbasins = []
estado = numpy.array(m, copy=True)
for x in range(ancho):
    for y in range(ancho):
        if(m[x,y] == 9):
            estado[x,y] = True
        else:
            estado[x,y] = False

for p in lhoyos:
    lbasins.append(check_basin(estado, p))

r = sorted(lbasins)
print("Part two result: ", r[-1]*r[-2]*r[-3])

