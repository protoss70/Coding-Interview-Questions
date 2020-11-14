def Factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def Posibility(n = 10, k = [1,3,5]):
    k = sorted(k)
    if len(k) < 0 or n <= 0:
        raise NameError("k cannot be empty")
    for i in k:
        if i <= 0:
            raise NameError("pick numbers that are higher than 0")
    a = 0
    b = 1
    c = 2
    Durum = 0
    olasılıklar = []
    liste = []
    for i in range(len(k)):
        liste.append(0)
    while a < len(k):
        Durum += k[a]
        liste[a] += k[a]

        if Durum < n and a != len(k)-1:
            for b in range(a+1,len(k)):
                Durum = liste[a]
                while Durum < n:
                    #print("b: {}, \t Liste: {}".format(b, liste))
                    Durum += k[b]
                    liste[b] += k[b]
                    if Durum < n and b != len(k) - 1:
                        c = b + 1
                        while c < len(k):
                            liste[c] += k[c]
                            Durum += k[c]
                            #print("c: {}, \t Liste: {} \tDurum: {}".format(c, liste, Durum))
                            if Durum < n and c != len(k)-1:
                                c += 1
                            elif Durum > n:
                                Durum -= liste[c]
                                liste[c] = 0
                                if c - 1 == b:
                                    break
                                else:

                                    c -= 1
                            elif Durum == n:
                                break

                    if Durum == n:
                        olasılıklar.append([])
                        for i in liste:
                            olasılıklar[-1].append(i)
                        for i in range(b, len(liste)):
                            liste[i] = 0
                    elif Durum > n:
                        for i in range(b, len(liste)):
                            liste[i] = 0
                    #print("e",olasılıklar)
            Durum = liste[a]
        elif Durum > n:
            Durum = 0
            liste[a] = 0
            a+=1
        elif Durum == n:

            olasılıklar.append([])
            for i in liste:
                olasılıklar[-1].append(i)
            for i in range(a, len(liste)):
                liste[i] = 0
    Sayı = 0
    for i in olasılıklar:
        s = 0
        d = 0
        for b in range(len(i)):
            s += i[b] / k[b]
            s = int(s)
        d = Factorial(s)
        for b in range(len(i)):
            d /= Factorial(int(i[b] / k[b]))
        Sayı += d
    print(olasılıklar)
    return Sayı






print(Posibility(300,[1,3,5,7,10]))





