giriş = [[0, 3, 1, 1, 1],
         [2, 0, 100, 1, 1],
         [1, 20, 3, 1, 1],
         [10, 0, 0, 0, 1]]


def Pathfinder():
    x = 0
    y = 0

    DeğerlerListesi = []
    for i in range(len(giriş)):
        DeğerlerListesi.append([])
    for b in range(len(giriş)):
        for i in range(len(giriş[0])):
            DeğerlerListesi[b].append(0)

    x = len(giriş[0])-1
    y = len(giriş)-1
    Kök = [len(giriş[0])-1,len(giriş)-1]
    DeğerlerListesi[y][x] = giriş[y][x]
    while True:

        #X İN way
        Pass = True
        while Pass:
            x-=1
            if x+1 != len(giriş[0]) and y+1 != len(giriş):
                if giriş[y][x+1] >= giriş[y+1][x]:
                    DeğerlerListesi[y][x] = DeğerlerListesi[y][x+1] + giriş[y][x]
                elif giriş[y][x+1] < giriş[y+1][x]:
                    DeğerlerListesi[y][x] = DeğerlerListesi[y+1][x] + giriş[y][x]
            elif x+1 == len(giriş[0]) and y+1 != len(giriş):
                DeğerlerListesi[y][x] = giriş[y][x] + DeğerlerListesi[y+1][x]
            elif x+1 != len(giriş[0]) and y+1 == len(giriş):

                DeğerlerListesi[y][x] = giriş[y][x] + DeğerlerListesi[y][x+1]
            if x == 0 and y == 0:
                if DeğerlerListesi[y + 1][x] > DeğerlerListesi[y][x + 1]:
                    return DeğerlerListesi[y + 1][x] + giriş[0][0]
                else:
                    return DeğerlerListesi[y][x + 1] + giriş[0][0]
            if x <= 0:
                Pass = False


        #Y in way
        x = Kök[0]

        Pass = True

        while Pass:

            y-=1
            if x+1 != len(giriş[0]) and y+1 != len(giriş):
                if giriş[y][x+1] >= giriş[y+1][x]:
                    DeğerlerListesi[y][x] = DeğerlerListesi[y][x+1] + giriş[y][x]
                elif giriş[y][x+1] < giriş[y+1][x]:
                    DeğerlerListesi[y][x] = DeğerlerListesi[y+1][x] + giriş[y][x]
            elif x+1 == len(giriş[0]) and y+1 != len(giriş):
                DeğerlerListesi[y][x] = giriş[y][x] + DeğerlerListesi[y+1][x]
            elif x+1 != len(giriş[0]) and y+1 == len(giriş):
                DeğerlerListesi[y][x] = giriş[y][x] + DeğerlerListesi[y][x+1]
            if x == 0 and y == 0:
                if DeğerlerListesi[y + 1][x] > DeğerlerListesi[y][x + 1]:
                    return DeğerlerListesi[y + 1][x] + giriş[0][0]

                else:
                    return DeğerlerListesi[y][x + 1] + giriş[0][0]

            if y == 0:
                Pass = False

        Kök = [Kök[0]-1,Kök[1]-1]
        x,y = Kök[0]+1,Kök[1]




print(Pathfinder())