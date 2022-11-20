def sortedFunc(numList):
    flag = True
    for i in range(1, len(numList)):
        if num_list[i-1] > num_list[i]:
            flag = False
            break
    return flag


def sortedFunc2(numList):
    if num_list == sorted(num_list):
        return True
    else:
        return False


n = input()

num_list = [int(num) for num in input().split(" ")]

if sortedFunc2(num_list):
    print("Yes")
else:
    print("No")
