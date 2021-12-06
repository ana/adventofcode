
days = 256

def create_new_dicc(d):
    ndic = {}
    for i in d:
        if (i==0):
            if(6 in ndic and 8 in ndic):
                ndic[6] += d[i]
                ndic[8] += d[i]
            elif(6 in ndic and 8 not in ndic):
                ndic[6] += d[i]
                ndic[8] = d[i]
            elif(6 not in ndic and 8 in ndic):
                ndic[6] = d[i]
                ndic[8] += d[i]
            elif(6 not in ndic and 8 not in ndic):
                ndic[6] = d[i]
                ndic[8] = d[i]
        else:
            if(i-1 in ndic):
                ndic[i-1] += d[i]
            else:
                ndic[i-1] = d[i]
    return ndic


with open("input.txt") as f:
    data = f.readline().strip()
line =[int(d) for d in data.split(",")]

d = {}
for i in line:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

for i in range(days):
    d = create_new_dicc(d)

print("Result for ", days, "days is: ", sum(d.values()))


