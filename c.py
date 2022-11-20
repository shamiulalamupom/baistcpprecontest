n = int(input())

space = n-1

for i in range(n):
    for j in range(space):
        print(" ", end="")
    for k in range(i+1):
        if k != i:
            print("* ", end="")
        else:
            print("*")
    space -= 1
