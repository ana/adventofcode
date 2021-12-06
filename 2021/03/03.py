
data=[]
longitud=0
gamma=[]
epsilon=[]
total=[]

with open('input.txt') as f:
    first_line = f.readline()

for i in range(0,len(first_line)-1):
    total.append(0)

with open("input.txt") as f:
    data = f.readlines()
    longitud=len(data)

for l in data:
    for c in range(0, len(l)-1):
        if l[c] == '1':
            total[c] = total[c] + 1

for n in range(0,len(total)):
    if (total[n] > longitud/2):
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

g=int("".join(gamma),2)
e=int("".join(epsilon),2)

print("Solution part one:", g*e)
