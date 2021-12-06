
inc = 0

with open("input.txt") as f:
    numbers = [int(x) for x in f.read().splitlines()]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        inc += 1

print("Part one: ", inc, "measurements are larger than the previous measurement.")


inc = 0
numbers3 = []

for i in range(0, len(numbers)-2):
    numbers3.append(numbers[i] + numbers[i+1] + numbers[i+2])

for i in range(1, len(numbers3)):
    if numbers3[i] > numbers3[i-1]:
        inc = inc+1

print("Part two: ", inc, "sums are larger than the previous sum.")

