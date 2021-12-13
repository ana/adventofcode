
with open("input.txt") as f:
    data = f.read().splitlines()

dots = []
folds = []
xs = []
ys=[]
for e in data:
    if e.startswith("fold"):
        r = e.split(" ")
        s, t= r[2].split("=")
        folds.append([s, int(t)])
    else:
        x,y = e.strip().split(",")
        dots.append([int(x), int(y)])
        xs.append(int(x))
        ys.append(int(y))


ancho = max(xs)+1
alto = max(ys)+1
print(ancho, "x", alto)
###

def dots_counter(mmm):
    counter = 0
    for linea in mmm:
        for e in linea:
            if e == '#':
                counter += 1
    return counter

def foldy(number, alto):
    # horizontal fold
    new = []
    for y,yy in zip(range(0,number,1), range(alto-1,number,-1)):
        l1, l2 = m[y], m[yy]
        newlist=[]
        for i in range(0,len(l1)):
            if l1[i] == '#' or  l2[i] == '#':
                newlist.append('#')
            else:
                newlist.append('.')
        new.append(newlist)

    dc = dots_counter(new)
    print("Total dots:", dc)
    for l in new:
        print(l)
    # return new value for alto
    return new, len(new)

def foldx(number, ancho):
    newancho = int((ancho-1)/2)
    # vertical fold
    new = []
    for linea in m:
        m1 = linea[0:newancho]
        m2 = linea[newancho+1:ancho]
        m2.reverse()
        newlist=[]
        for i in range(newancho):
            if m1[i] == '#' or  m2[i] == '#':
                newlist.append('#')
            else:
                newlist.append('.')
        new.append(newlist)

    dc = dots_counter(new)
    print("Total dots:", dc)
    for l in new:
        print(l)
    # return new value for ancho
    return new,newancho

m = []
for y in range(alto):
    l = []
    for x in range(ancho):
        l.append('.')
    m.append(l)

for c in dots:
    x, y = c
    m[y][x] = '#'

#for l in m:
#    print(l)
print("-------------------------------------------------------")


for f in folds:
    # if axis y -> fold is horizontal
    if f[0] == 'y':
        m,alto = foldy(f[1], alto)
    else:
        m,ancho = foldx(f[1], ancho)
    print("-------------------------------------------------------")

