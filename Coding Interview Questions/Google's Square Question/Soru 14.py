giriş = [-9, -2, 0, 2, 3]

def Squarer():
    for i in range(len(giriş)):
        if giriş[i] < 0:
            giriş[i] *= -1
    newList = sorted(giriş)
    print(giriş)
    print(newList)
    for i in range(len(newList)):
        newList[i] *= newList[i]
    return newList


print(Squarer())