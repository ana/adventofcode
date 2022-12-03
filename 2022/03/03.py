

with open("03.txt") as f:
    lines = [str(x) for x in f.read().splitlines()]

prio = {}

s = "abcdefghijklmnopqrstuvwxyz"
l = 1
for e in s+s.upper():
    prio[e] = l
    l = l +1

####

total = 0
for e in lines:
    a = e[0:len(e)//2]
    b = e[len(e)//2 if len(e)%2 == 0 else ((len(e)//2)+1):]
    v = list(set(a).intersection(b))
    total = total + prio[v[0]] 
    
print(total)

####
total = 0
for e in range(0, len(lines), 3):
    a = lines[e]
    b = lines[e+1]
    c = lines[e+2]

    d = set(a).intersection(b)
    e = set(b).intersection(c)
    v = list(set(d).intersection(e))
    
    total = total + prio[v[0]] 
   
print(total)

