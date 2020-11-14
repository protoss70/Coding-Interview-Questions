Giriş = "Lets go out right now"

def ReverseSentence():
    Sonuç = ""
    FirsIndex = 0

    for i in range(0,len(Giriş)):

        if Giriş[i] == " ":

            if len(Sonuç) == 0:
                Sonuç = Giriş[0:i]
                FirsIndex = i +1

            elif Giriş[i] == " ":
                Eklenecek = Giriş[FirsIndex:i]
                Eklenecek = Eklenecek+ " "
                Sonuç = Eklenecek + Sonuç
                FirsIndex = i + 1

        elif i == len(Giriş) - 1:
            Eklenecek = Giriş[FirsIndex:i+1]
            Eklenecek = Eklenecek + " "
            Sonuç = Eklenecek + Sonuç
            print(Sonuç)
            break

ReverseSentence()