giriş = ")(()) )))((((("

def Finder():
    ToRemove = 0
    AçıkParantez = 0
    for i in range(len(giriş)):
        if giriş[i] == "(":
            AçıkParantez += 1
        elif giriş[i] == ")" and AçıkParantez == 0:
            ToRemove += 1
        elif giriş[i] == ")":
            AçıkParantez -= 1
    return ToRemove + AçıkParantez

print(Finder())
