
with open("input.txt") as f:
    data = f.read().splitlines()

output1 = [l.split("|")[1] for l in data]
output = [l.strip().split(" ") for l in output1]

counter = 0
for array in output:
    for a in array:
        if len(a) in [2,3,4,7]:
            counter += 1

print("easy digits 1,4,7 and 8 appear ", counter, "times")

