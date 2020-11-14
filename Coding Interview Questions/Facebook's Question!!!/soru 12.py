giriş = [1,2,3,4,5,6,7,12]


def Rotater(k):
    if k % len(giriş) == 0:
        return giriş
    else:
        for i in range(k):
            giriş.append(giriş[0])
            giriş.pop(0)
        return giriş


print(Rotater(2))