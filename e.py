import math as m

p = float(input())

pn = m.floor(p)

l = pn // 10

print("[", end="")

for i in range(l):
    print("+", end="")
for i in range(10-l):
    print(".", end="")

print("] {}%".format(pn))
