def SquareRoot(x):
    Sonuç = 1
    Köklü = 1
    Minus = False
    Bölenler = []
    if x < 0:
        Minus = True
        x *= -1
    a = 1
    while x > 1:
        a += 1
        if x % a == 0:
            Pass = False
            for i in Bölenler:
                try:
                    if i[0] == a:
                        i[1] += 1
                        Pass =True
                except:
                    pass
            if Pass == False:
                Bölenler.append([a,1])
            x /= a
            a = 1
    for i in range(len(Bölenler)):
        if Bölenler[i][1] >= 2:
            Sonuç *= Bölenler[i][0] * ((Bölenler[i][1] - (Bölenler[i][1] % 2)) / 2)
            Bölenler[i][1] = Bölenler[i][1] % 2
    for i in range(len(Bölenler)):
        if Bölenler[i][1] >0:
            Köklü *= Bölenler[i][0]
    if Köklü == 1:
        return int(Sonuç)
    if Sonuç == 1 and Köklü != 1:
        if Minus:
            return "root {}".format(-Köklü)

        return "root {}".format(Köklü)
    if Sonuç == 1 and Köklü == 1:
        if Minus:
            return "i{}".format(1)
        return 1
    if Minus:
        return "i times {} root {}".format(int(Sonuç), Köklü)
    return "{} root {}".format(int(Sonuç),Köklü)


print(SquareRoot(164))











