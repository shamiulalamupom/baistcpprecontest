def pal1(s):
    l = len(s)
    flag = True

    for i in range(l):
        if s[i] != s[l-i-1]:
            flag = False
            break
    return flag


def pal2(s):
    if s == s[::-1]:
        return True
    else:
        return False


s = input()

if pal2(s):
    print("Yes")
else:
    print("No")
