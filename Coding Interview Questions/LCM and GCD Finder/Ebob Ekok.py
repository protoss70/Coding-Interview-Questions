def Ebob(A,B):

    Bölenler = []
    x = 1
    Sonuç = 1

    while True:
        x += 1
        if A % x == 0 and B % x == 0 and x != 1:
            Bölenler.append(x)
            A /= x
            B /= x
            x = 1
        elif A % x == 0 and x != 1:
            A /= x
            x = 1
        elif B % x == 0 and x != 1:
            B /= x
            x = 1

        if A == 1 and B == 1:
            for i in Bölenler:
                Sonuç *= i
            print(Sonuç)
            break






def Ekok(A,B):
    Bölenler = []
    x = 1
    Sonuç = 1

    while True:
        x += 1
        if A % x == 0 and B % x == 0 and x != 1:
            Bölenler.append(x)
            A /= x
            B /= x
            x = 1
        elif A % x == 0 and x != 1:
            A /= x
            Bölenler.append(x)
            x = 1
        elif B % x == 0 and x != 1:
            B /= x
            Bölenler.append(x)
            x = 1

        if A == 1 and B == 1:
            for i in Bölenler:
                Sonuç *= i
            print(Sonuç)
            break

Ekok(4 , 6)