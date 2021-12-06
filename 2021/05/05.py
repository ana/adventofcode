import re
import numpy

with open("input.txt") as f:
    data = f.read().splitlines()

acciones = [re.split("\-\>|,", l) for l in data]
m=numpy.zeros(shape=(1000,1000), dtype=int)


for acc in acciones:
    a,b, r, s = [int(x) for x in acc]

    # Vertical (x)
    if a == r:
        if (b-s >= 0):
            for i in range(s,b+1):
                m[a,i] += 1
        else:
            for i in range(b,s+1):
                m[a,i] += 1

    # Horizontal (y)
    elif b == s:
        if (a-r>=0):
            for i in range(r,a+1):
                m[i,b] += 1
        else:
            for i in range(a,r+1):
                m[i,b] += 1

    # Diagonal ! (second part)
    else:
        # subo de (a,b) a (r,s)
        if a < r and b < s:
            i=a
            j=b
            while (i<r+1 and j<s+1):
                m[i,j] += 1
                i+=1
                j+=1

        elif r < a and s < b:
            i=r
            j=s
            while (i<a+1 and j<b+1):
                m[i,j] += 1
                i+=1
                j+=1
        # subo en a y bajo en b
        elif a < r and b > s:
            i=a
            j=b
            while (i<r+1 and j>s-1):
                m[i,j] += 1
                i+=1
                j-=1

        # bajo en a y subo en b
        elif a > r and b < s:
            i=a
            j=b
            while (i>r-1 and j<s+1):
                m[i,j] += 1
                i-=1
                j+=1

        else:
            print(" Problem: ", a,b, " ",r,s,"\n")

print(print("Result 2: ", len(m[m>=2])))
