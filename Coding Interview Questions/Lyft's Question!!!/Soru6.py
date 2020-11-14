k = 9
giriş = [1,2,3,4,5]

def Summer():
    sonuç = []
    for i in range(len(giriş)):
        firsIndex = i
        toplam = giriş[i]
        a = i+1
        while toplam < k:
            toplam += giriş[a]
            if toplam == k:
                for i in range(firsIndex,a+1):
                    sonuç.append(giriş[i])
                return sonuç
            if a == len(giriş)-1:
                return []
            a += 1


print(Summer())