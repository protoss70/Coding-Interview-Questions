StockPrices = [200, 9, 18, 8, 5, 7, 2]


def BestPrice1(a):

    LowestPrices = sorted(a)

    profits = []
    for i in LowestPrices:
        index = 0
        liste = []

        for b in range(0, len(a)):
            if i == a[b]:
                index = b
        for b in range(index, len(a)):
            liste.append(a[b])
        try:
            profits.append(sorted(liste, reverse=True)[0] - i)
        except:
            pass
    for i in sorted(profits, reverse=True):

        for b in range(0, len(profits)):
            if i == profits[b]:
                return LowestPrices[b]


print(BestPrice1(StockPrices))