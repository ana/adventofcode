
total = []
data=[]
longitud=0

with open('input.txt') as f:
    first_line = f.readline()

for i in range(0,len(first_line)-1):
    total.append(0)

with open("input.txt") as f:
    data = f.read().splitlines()
    longitud=len(data)

ncol = len(first_line)
listas=data

def bit_mas_comun_reduce (listas, indice):
    uno = 0
    cero = 0
    bit = ''
    for l in listas:
        if l[indice] == '1':
            uno += 1
        else:
            cero += 1

    if (uno >= cero):
        bit='1'
    else:
        bit='0'

    nlista = []
    for l in listas:
        if l[indice] == bit:
            nlista.append(l)
    return nlista

for i in range(0, longitud):
    listas = bit_mas_comun_reduce(listas, i)
    if len(listas)==1:
        break

oxy = listas[0]

listas=data

def bit_menos_comun_reduce (listas, indice):
    uno = 0
    cero = 0
    bit = ''
    for l in listas:
        if l[indice] == '1':
            uno += 1
        else:
            cero += 1

    if (cero <= uno):
        bit='0'
    else:
        bit='1'

    nlista = []
    for l in listas:
        if l[indice] == bit:
            nlista.append(l)
    return nlista

for i in range(0, longitud):
    listas = bit_menos_comun_reduce(listas, i)
    if len(listas)==1:
        break

co2 = listas[0]

i_co2 = int("".join(co2),2)
i_oxy = int("".join(oxy),2)

print("solution part two: ", i_co2*i_oxy)
