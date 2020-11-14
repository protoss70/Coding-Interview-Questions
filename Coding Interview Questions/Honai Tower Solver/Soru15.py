def HonaiTowerSolver(n):
    Odd = True
    if n % 2 == 0:
        Odd = False
    peg_one = []
    peg_two = []
    peg_three = []
    Sonuç = []
    for i in range(1,n+1):
        peg_one.append(i)
    while peg_three.__len__() < n:

        if peg_one != sorted(peg_one) or peg_two != sorted(peg_two) or peg_three != sorted(peg_three):

            return False
        try:
            if Odd:

                if len(peg_one) != 0 and (len(peg_three) == 0 or peg_one[0] < peg_three[0]):
                    peg_three.insert(0, peg_one[0])
                    peg_one.pop(0)
                    Sonuç.append([1, 3])
                elif len(peg_three) != 0 and (len(peg_one) == 0 or peg_one[0] > peg_three[0]):
                    peg_one.insert(0, peg_three[0])
                    peg_three.pop(0)
                    Sonuç.append([3, 1])

                if len(peg_one) != 0 and (len(peg_two) == 0 or peg_one[0] < peg_two[0]):
                    peg_two.insert(0, peg_one[0])
                    peg_one.pop(0)
                    Sonuç.append([1, 2])
                elif len(peg_one) == 0 or peg_one[0] > peg_two[0]:
                    peg_one.insert(0, peg_two[0])
                    peg_two.pop(0)
                    Sonuç.append([2, 1])

                if len(peg_three) != 0 and (len(peg_two) == 0 or peg_three[0] < peg_two[0]):
                    peg_two.insert(0, peg_three[0])
                    peg_three.pop(0)
                    Sonuç.append([3, 2])
                elif len(peg_three) == 0 or peg_three[0] > peg_two[0]:
                    peg_three.insert(0, peg_two[0])
                    peg_two.pop(0)
                    Sonuç.append([2, 3])
            else:
                if len(peg_one) != 0 and (len(peg_two) == 0 or peg_one[0] < peg_two[0]):
                    peg_two.insert(0, peg_one[0])
                    peg_one.pop(0)
                    Sonuç.append([1, 2])
                elif len(peg_one) == 0 or peg_one[0] > peg_two[0]:
                    peg_one.insert(0, peg_two[0])
                    peg_two.pop(0)
                    Sonuç.append([2, 1])

                if len(peg_one) != 0 and (len(peg_three) == 0 or peg_one[0] < peg_three[0]):
                    peg_three.insert(0, peg_one[0])
                    peg_one.pop(0)
                    Sonuç.append([1, 3])
                elif len(peg_one) == 0 or peg_one[0] > peg_three[0]:
                    peg_one.insert(0, peg_three[0])
                    peg_three.pop(0)
                    Sonuç.append([3, 1])

                if len(peg_two) != 0 and (len(peg_two) == 0 or peg_three[0] < peg_two[0]):
                    peg_two.insert(0, peg_three[0])
                    peg_three.pop(0)
                    Sonuç.append([3, 2])
                elif len(peg_three) == 0 or peg_three[0] > peg_two[0]:
                    peg_three.insert(0, peg_two[0])
                    peg_two.pop(0)
                    Sonuç.append([2, 3])
        except:
            pass


    return Sonuç



print(HonaiTowerSolver(5))