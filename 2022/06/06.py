with open("input.txt") as f:
    st = f.read().strip()


for i in range(0, len(st)):
    if len(set(st[i:i+4])) == 4:
      print("value:", i+4)
      break

for i in range(0, len(st)):
    if len(set(st[i:i+14])) == 14:
      print("value2:", i+14)
      break
