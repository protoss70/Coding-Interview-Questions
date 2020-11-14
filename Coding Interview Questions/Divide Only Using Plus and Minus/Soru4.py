

def Divison(a,b):
    if b == 0:
        return False
    Bölüm = 0
    Sonuç = 0
    while a > Bölüm:
        if Bölüm + b < a:
            Bölüm += b
            Sonuç +=1
        elif Bölüm + b > a:
            print(a - Bölüm, " <--Remaining")
            return Sonuç
        elif Bölüm + b == a:
            print(a - Bölüm," <--Remaining")
            return Sonuç+1



print(Divison(71,5))