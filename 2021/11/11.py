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


def flashes(done, total, fls):
    to_visit = numpy.array(numpy.where(m>9)).T

    while len(to_visit) > 0:
        i,j = to_visit[-1]

        if len(to_visit) > 0:
            to_visit = to_visit[:-1]

        if [i,j] in done:
            continue

        done.append([i,j])
        fls += 1
        for ii,jj in [(i-1,j-1), (i-1,j), (i-1, j+1), (i,j-1), (i, j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]:
            if not (ii < 0 or jj < 0 or ii >= alto or jj >= ancho):
                m[ii,jj] += 1

    return done, (m > 9).sum(), fls


steps = 300
fls = 0
print("Before any steps:\n", m)
for i in range(steps):

    # 1 the energy level of each octopus increases by 1
    m = m+1

    # 2 flashes for everything with a 9
    nines=(m > 9).sum()
    done = []
    while True:
        done, r, fls = flashes(done, nines, fls)
        if r == nines:
            break
        else:
            nines = r

    # 3 any octopus that flashed during this step has its energy level set to 0
    m[m>9] = 0

    print("After step ", i+1, "flashes", fls, "total sum: ", numpy.sum(m), ":\n", m)
    # Step two
    if numpy.sum(m) == 0:
        break
