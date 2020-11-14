Karakter = input('karakter adınızı giriniz:')
Karakter_hız = 4
Karakter_eşya_yeri = 0
çantadakiler = []
Çağrılar = []
print('oyun kuralları:\n1- sadece rakam girin')

print('''{} sanatına el konulmuş dindar bir ailede yaşayan bir müzisyen\n evden kaçmaya kalbini adamış ve bunun için ne gerekirse yapacak,'''.format(Karakter)



)

print('Gün 1\n***** SEÇİMLER *****')
while True:
    Gün_1_seçim_1 = input(
        'valizini seç \n1- sırt çantası (2 eşya yeri)\n2- dağcı çantası (3 eşya yeri, -1 hız)\n3- valiz (5 eşya yeri,-3 hız)')

    if (Gün_1_seçim_1 == '1'):
        Karakter_çanta = 'sırt çantası'
        Karakter_eşya_yeri += 2
        print('karakter hızı: {} \nkarakter çantası seçimi: {}\nkarakter eşya sınırı: {}'.format(Karakter_hız,
                                                                                                 Karakter_çanta,
                                                                                                 Karakter_eşya_yeri))
        break
    elif (Gün_1_seçim_1 == '2'):
        Karakter_çanta = 'dağcı çantası'
        Karakter_eşya_yeri += 3
        Karakter_hız -= 1
        print('karakter hızı: {} \nkarakter çantası seçimi: {}\nkarakter eşya sınırı: {}'.format(Karakter_hız,
                                                                                                 Karakter_çanta,
                                                                                                 Karakter_eşya_yeri))
        break
    elif (Gün_1_seçim_1 == '3'):
        Karakter_çanta = 'sırt çantası'
        Karakter_eşya_yeri += 5
        Karakter_hız -= 3
        print('karakter hızı: {} \nkarakter çantası seçimi: {}\nkarakter eşya sınırı: {}'.format(Karakter_hız,
                                                                                                 Karakter_çanta,
                                                                                                 Karakter_eşya_yeri))
        break
    else: print('*****\nhatalı giriş\n*****')
print('evden kaçmadan alacağın eşyaları seçmeyi unutma')

print('*\nöncelikle çok geç olmadan 2 oda gezebilirsin bu odaları dikkatli seç\n*')


Babanın_Yatak_Odası = ['100 para', 'kimlik kartın', 'tabanca']
Tuvalet = ['ilk yardım çantası','prezervatif']
Depo = [ '100 para', 'balta', 'kurşun']
Oda_giriş_sayısı = 0
Babanın_Yatak_Odası_Girişi = 0
Tuvalet_Girişi = 0
depo_girişi = 0

while True:

    print('odalar \n1- babanın odası\n2- tuvalet\n3- depo')
    oda = input('gireceğiniz odayı seçin:')


    if oda == '1' and Babanın_Yatak_Odası_Girişi != 1:
        Oda_giriş_sayısı += 1
        while True and len(Babanın_Yatak_Odası) != 0:
            print('alabileceğin eşyalar', Babanın_Yatak_Odası,'her eşyadan bir tane alabilirsin',sep='\n')


            alacak = input('alacağınız eşyaların sıralarını giriniz\n (ör: 1 ya da 123 gibi):')

            if alacak == '1'and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Babanın_Yatak_Odası[0])
                Babanın_Yatak_Odası_Girişi += 1
                print('çantadakiler:',çantadakiler)
                break

            elif alacak == '2'and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Babanın_Yatak_Odası[1])
                Babanın_Yatak_Odası_Girişi += 1
                print('çantadakiler:',çantadakiler)
                break

            elif alacak == '3'and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Babanın_Yatak_Odası[2])
                Babanın_Yatak_Odası_Girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '12'and len(çantadakiler) + 2 <= Karakter_eşya_yeri:
                çantadakiler.append(Babanın_Yatak_Odası[0])
                çantadakiler.append(Babanın_Yatak_Odası[1])
                Babanın_Yatak_Odası_Girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '13'and len(çantadakiler) + 2 <= Karakter_eşya_yeri:
                çantadakiler.append(Babanın_Yatak_Odası[0])
                çantadakiler.append(Babanın_Yatak_Odası[2])
                Babanın_Yatak_Odası_Girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '23' and len(çantadakiler) + 2 <= Karakter_eşya_yeri:
                çantadakiler.append(Babanın_Yatak_Odası[1])
                çantadakiler.append(Babanın_Yatak_Odası[2])
                Babanın_Yatak_Odası_Girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '123' and len(çantadakiler) + 3 <= Karakter_eşya_yeri:
                çantadakiler.append(Babanın_Yatak_Odası[0])
                çantadakiler.append(Babanın_Yatak_Odası[2])
                çantadakiler.append(Babanın_Yatak_Odası[1])
                Babanın_Yatak_Odası_Girişi += 1
                print('çantadakiler:',çantadakiler)
                break

            else: print('hatalı seçim',çantadakiler)

    elif oda == '1' and Babanın_Yatak_Odası_Girişi == 1:
        print('**********\nbu odaya 1 kez girdin bir daha giremezsin\n**********')
    if oda == '2' and Tuvalet_Girişi != 1:
        Oda_giriş_sayısı += 1

        while True:
            print('alabileceğin eşyalar', Tuvalet, 'her eşyadan bir tane alabilirsin', sep='\n')

            alacak = input('alacağınız eşyaların sıralarını giriniz\n (ör: 1 ya da 123 gibi):')

            if alacak == '1' and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Tuvalet[0])
                Tuvalet_Girişi += 1
                print('çantadakiler:', çantadakiler)
                break
            elif alacak == '2' and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Tuvalet[1])
                Tuvalet_Girişi += 1
                print('çantadakiler:', çantadakiler)
                break
            elif alacak == '12' and len(çantadakiler) + 2 <= Karakter_eşya_yeri:
                çantadakiler.append(Tuvalet[1])
                Tuvalet_Girişi += 1
                print('çantadakiler:', çantadakiler)
                break
            else:
                print('hatalı seçtiniz',çantadakiler)

    elif oda == '2' and Tuvalet_Girişi == 1:
        print('**********\nbu odaya 1 kez girdin bir daha giremezsin\n**********')
    if oda == '3' and depo_girişi != 1:
        Oda_giriş_sayısı += 1
        while True:
            print('alabileceğin eşyalar', Depo,'her eşyadan bir tane alabilirsin',sep='\n')


            alacak = input('alacağınız eşyaların sıralarını giriniz\n (ör: 1 ya da 123 gibi):')

            if alacak == '1'and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Depo[0])
                depo_girişi += 1
                print('çantadakiler:',çantadakiler)
                break

            elif alacak == '2'and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Depo[1])
                depo_girişi += 1
                print('çantadakiler:',çantadakiler)
                break

            elif alacak == '3'and len(çantadakiler) < Karakter_eşya_yeri:
                çantadakiler.append(Depo[2])
                depo_girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '12'and len(çantadakiler) + 2 <= Karakter_eşya_yeri:
                çantadakiler.append(Depo[0])
                çantadakiler.append(Depo[1])
                depo_girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '13'and len(çantadakiler) + 2 <= Karakter_eşya_yeri:
                çantadakiler.append(Depo[0])
                çantadakiler.append(Depo[2])
                depo_girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '23' and len(çantadakiler) + 2 <= Karakter_eşya_yeri:
                çantadakiler.append(Depo[1])
                çantadakiler.append(Depo[2])
                depo_girişi += 1
                print('çantadakiler:',çantadakiler)
                break
            elif alacak == '123' and len(çantadakiler) + 3 <= Karakter_eşya_yeri:
                çantadakiler.append(Depo[0])
                çantadakiler.append(Depo[2])
                çantadakiler.append(Depo[1])
                depo_girişi += 1
                print('çantadakiler:',çantadakiler)
                break

            else: print('hatalı seçim',çantadakiler)
    elif depo_girişi == 1:
        print('**********\nbu odaya 1 kez girdin bir daha giremezsin\n**********')
    if Oda_giriş_sayısı == 2:
        print('\nsabah olmak üzere\n')
        break
    if len(çantadakiler) == Karakter_eşya_yeri:
        print('yer dolu')
        break
print('******\nDİO: Tebrikler küçük adam.\nŞimdi git ve sanatını sonuna kadar icra et\n')
print('''envantere Dio'nun çağrısı eklendi ''')
Çağrılar.append('''Dio'nun çağrısı''')
print('****\n{}\n*****'.format(Çağrılar))
print('oyununuz kaydedildi')

print('********************\nGÜN 2\n********************')
print(
    'GELİŞMELER: 2. günün şafağında havada müzik kokusu çantada dolusu güfte\nartık bu lanet şehirden kaçma zamanı geldi...\n nereye mi\nmüziğin merkezine')
print('şey... DİO... müziğin merkezi neresi acaba\nDİO: müzik kalbinde çalıyor evlat.\nsadece sesi duyman lazım')
print('tabi ya müziğin sesi he... o zaman müziği dinleyelim')
print('********************\nSEÇİMLER \n********************')
while True:
    print('********************\nSEÇİMLER \n********************')

    Gün_2_seçim_1 = input('gideceğin yeri seç\n1- lokal bar\n2- Esenler otogar\n3- Burger King')

    if Gün_2_seçim_1 == '3':
        print('Kasiyer:siparişinizi alabilir miyiz')
        print('''DİO: seni vizyonsuz çocuk\nDİO'nun çağrısı envanterden eksildi''')
        print('müziğin sesi buradan duyulmuyor\n sanırım kaybettim')
        print('********************\noyunu kaybettiniz\n********************')
    elif Gün_2_seçim_1 =='2':
        print('ne biçim bir yer burası, bu ne böyle')
        print('tedirgin görünen yabancı:sen, çocuk.\n buraya yabancısın sanırım gel bak sana ne göstereceğim')
        print('...\n...\n...')
        print('*****3 AY SONRA*****')
        print('uyuşturucu bağımlısı oldunuz')
        print('********************\noyunu kaybettiniz\n********************')
    elif Gün_2_seçim_1 == '1':
        print('daha girişten müziğin kokusunu alabiliyorum\nişte orada...\nMÜZİK BABA.')
        print('MÜZİK BABA: ben de seni bekliyordum, DİO bana haber vermişti\nşimdi buradan uzayalım')
        break

print("********** SEÇİMLER **********\n1- Çin'e gitmek(gerekli eşyaler: kimlik kartın, 100 para, Gerekli hız: 4\n2- İstiklal Caddesi\n3- Genç Bi Şenlik (Gerekli Eşyalar: Prezertif, 100 para)")
Gün_2_seçim_2 = input('Seçiminiz:')

while True:

    if Gün_2_seçim_2 == '1' and Karakter_hız == 4 and (çantadakiler[0] == '100 para' or çantadakiler[1] == '100 para') and (çantadakiler[0] == 'kimlik kartın' or çantadakiler[1] == 'kimlik kartın'):
        devam = 1































































