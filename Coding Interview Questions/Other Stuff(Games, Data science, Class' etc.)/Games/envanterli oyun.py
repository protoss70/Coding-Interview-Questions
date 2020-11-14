import random

Sıra = 1

class çanta():
    def __init__(self, isim, eşya_yeri, içindekiler=[]):
        self.eşya_yeri = eşya_yeri
        self.içindekiler = içindekiler
        self.isim = isim

    def İçerik_Göster(self):
        Dön = []
        for i in range(0,len(self.içindekiler)):

           Dön.append(self.içindekiler[i].isim)
        return Dön
    def Eşya_Bırakma(self,Bırakılacak_Eşya):
        self.içindekiler.pop(Bırakılacak_Eşya)



    def Eşya_Ekleme(self, eklenecek_eşya):
        if eklenecek_eşya.alan + len(self.içindekiler) > self.eşya_yeri:
            print('eşya alanınız yeterli değil.\n açmanız gereken alan:',
                  (len(self.içindekiler) + eklenecek_eşya.alan) - self.eşya_yeri)
        elif eklenecek_eşya.alan + len(self.içindekiler) <= self.eşya_yeri:
            self.içindekiler.append(eklenecek_eşya)

İptidai_Çanta = çanta('İptidai Çanta', 2)


class Bölge():
    def __init__(self,Boss_Durumu,Bossa_Ulaşma_Sayısı,Tehlike):
        self.Boss_Durumu = Boss_Durumu
        self.Bossa_Ulaşma_Sayısı = Bossa_Ulaşma_Sayısı
        self.Tehlike = Tehlike

Orman = Bölge(1,5,2)



class Karakter():
    def __init__(self, Karakter_Adı, Can, Hasar, Karakter_Çantası=İptidai_Çanta, Kemer = 0):
        self.kemer = Kemer
        self.Karakter_Adı = Karakter_Adı
        self.Karakter_Çantası = Karakter_Çantası
        self.Hasar = Hasar
        self.Can = Can

    def Eşya_Alma(self, Alınan_Eşya):
        self.Karakter_Çantası.Eşya_Ekleme(Alınan_Eşya)

    def Eşya_Kullanma(self, Kullanılacak_Eşya,İşlem):
        try:

            if Kullanılacak_Eşya.Etki == 'can basma':
                self.Can += Kullanılacak_Eşya.Etki_Katsayısı
                print('karakteriniz iyileştirildi', self.Can)
            elif Kullanılacak_Eşya.Etki == 'güç arttırma':
                self.Hasar += Kullanılacak_Eşya.Etki_Katsayısı
                print('Hasarınız arttı', self.Hasar)
            self.Karakter_Çantası.içindekiler.pop(İşlem-1)
        except:
            print('seçtiğiniz eşya {} bu tip bir kullanıma uygun değil'.format(Kullanılacak_Eşya.isim))
    def Saldırma(self,Kılıç):

        try:

            return self.Hasar+Kılıç.hasar
        except:
            print('Seçtiğiniz eşya saldırı eşyası değil')
            return self.Hasar







class Düşman():
    def __init__(self,İsim,Can,Hasar,Tehlike):
        self.İsim = İsim
        self.Can = Can
        self.Hasar = Hasar
        self.Tehlike = Tehlike
    def Saldırı(self,Sıra):
        if Sıra == 1:
            print('{} Saldırdı ve {} Hasar verdi.'.format(self.İsim,self.Hasar))
            BozKurtxx_32.Can -= Düşman.Hasar
            Sıra = 0
    def Hasar_Alma(self,Alınan_Hasar):
        self.Can -= Alınan_Hasar

    def Eşya_Düşürme(self):
        a = random.randint(1, 11)
        if a <6:
            x = random.randint(1,self.Tehlike + 1)
            for i in range(0,len(İksirler)):
                if İksirler[i].Değer== x:
                    return İksirler[i]

class Boss():
    def __init__(self, İsim, Can, Hasar, Tehlike):
        self.İsim = İsim
        self.Can = Can
        self.Hasar = Hasar
        self.Tehlike = Tehlike

    def Saldırı(self, Sıra):
        if Sıra == 1:
            print('{} Saldırdı ve {} Hasar verdi.'.format(self.İsim, self.Hasar))
            BozKurtxx_32.Can -= Düşman.Hasar
            Sıra = 0

    def Hasar_Alma(self, Alınan_Hasar):
        self.Can -= Alınan_Hasar

    def Eşya_Düşürme(self):
        a = random.randint(1, 11)
        if a < 6:
            x = random.randint(1, self.Tehlike + 1)
            for i in range(0, len(İksirler)):
                if İksirler[i].Değer == x:
                    return İksirler[i]





class Eşya_Genel():
    def __init__(self, isim, açıklama, alan, Etki='Etkisiz', Etki_Katsayısı=0,Değer = 0):
        self.alan = alan
        self.açıklama = açıklama
        self.isim = isim
        self.Etki = Etki
        self.Etki_Katsayısı = Etki_Katsayısı
        self.Değer = Değer

class Silah():
    def __init__(self, isim, açıklama, alan, tür, vuruş_hızı, hasar):
        self.alan = alan
        self.açıklama = açıklama
        self.tür = tür
        self.vuruş_hızı = vuruş_hızı
        self.isim = isim
        self.hasar = hasar


Can_İksiri = Eşya_Genel('Can İksiri', 'kullanımda karakterin canını 10 arttırır.', 1,'can basma',10,1)

Emre_İksiri = Eşya_Genel("Emre iksiri","20 can basar",1,"can basma",20,30)

İsmail_İksiri = Eşya_Genel("İsmail_İksiri","50 can basar",1,"can basma",50,50)

Güç_İksiri = Eşya_Genel('Güç İksiri', 'kullanımda Karakterin asıl hasarını 2 arttırır', 1,'güç arttırma',2,2)

Kuvetli_Can_İksiri = Eşya_Genel('Kuvetli Güç İksiri','Kullanımda 25 can arttırır',2,'can basma',25,3)

Protein_İksiri = Eşya_Genel('Protein İksiri','Kullanımda 4 hasar arttırır',3,'güç arttırma',4,4)

İksirler = [Can_İksiri,Güç_İksiri,Kuvetli_Can_İksiri,Protein_İksiri]

Talim_Kılıcı = Silah('Talim Kılıcı', 'insan ırkını üretimi, talimlerde kullanılar iptidai bir kılıç', 2, 'Kılıç', 5, 30)

Kuzeyli_Kılıcı = Silah('Kuzeyli Kılıcı','Kuzeyli insanların muharebe sırasında kullandıkları ortalama bir kılıç',2,'kılıç,',2,25)

Cüce_Azman_Topuzu = Silah('Cüce Azman Topuzu','Cüce ırkının ölümcül silahı, moria dağlarının derinliklerindeki cevherlerden yapılmış kusursuz bir silah',3,'Topuz',2,50)

Kudret_Çekici = Silah('Kudret Çekici', 'Elf ırkının büyülü ve paha biçilmez  çekici', 4,
                      'Çekiç', 2, 80)

Dev_Örümcek = Boss('Dev Örümcek',60,8,3)

Zombi = Düşman('Zombi',25,3,1)

İskelet = Düşman('İskelet',30,5,2)

Şeytan = Düşman('Şeytan',90,10,3)

Karabasan = Düşman('Karabasan',110,12,4)

Kurt_Binici = Düşman('Kurt Binici',170,20,4)

Ork_Savaş_Şefi = Düşman('Ork Savaş Şefi',200,25,4)

Düşmanlar = [Ork_Savaş_Şefi,Kurt_Binici,Karabasan,Şeytan,İskelet,Zombi]

Taşıyıcı_Çantası = çanta('Taşıyıcı Çantası', 5,[Can_İksiri,Talim_Kılıcı])



Dev_Kemer = çanta('Dev Kemer', 2)


BozKurtxx_32 = Karakter('BozkurtCCC',100,10,Taşıyıcı_Çantası,Dev_Kemer)
Geri_Karakterdol = BozKurtxx_32.Can
while True:
    BozKurtxx_32.Can = Geri_Karakterdol
    print('**********Kral, en iyi kelle avcısı olan seni krallık sınırlarına gördüğün küçük düşman gruplarını temizlemen ve sınır böglelerini güvene alman için yolladı**********')
    işlem = input("1-Ormana git(1-3 Tehlike)\n2-Mağaraya git(3-6 Tehlike)\n3-Ork Yerleşkesine git(6-9 tehlike)\n4-Kudretli vampir Nosferatu'nun şatosuna git(10 Tehlike) ")

    if işlem == '1':
        while Orman.Boss_Durumu != 0:
            if BozKurtxx_32.Can <= 0:
                print('Öldünüz.')
                break
            elif BozKurtxx_32.Can >0:
                Sıra = 2
                if Orman.Bossa_Ulaşma_Sayısı != 0:
                    x = random.randint(1, Orman.Tehlike)
                    for i in range(0, len(Düşmanlar)):
                        if x == Düşmanlar[i].Tehlike:
                            Rakip = Düşmanlar[i]
                            print('\n>>>Karşınıza vahşi bir {} çıktı<<<\n'.format(Rakip.İsim))
                            Geri_Dolum = Rakip.Can
                elif Orman.Bossa_Ulaşma_Sayısı == 0:
                    Rakip = Dev_Örümcek
                while Rakip.Can > 0 and BozKurtxx_32.Can > 0:
                    if Sıra == 2:
                        while Sıra == 2:

                            print('\n***{} Canı {}***\n'.format(Rakip.İsim, Rakip.Can))

                            Seçim = input('1- bütün bilgileri Göster\n2- İksir Kullan\n3- Saldır')
                            if Seçim == '1':
                                print('**********\nCan: {}\nHasar: {}\nEşyalar: {}\n**********'.format(BozKurtxx_32.Can,
                                                                                                       BozKurtxx_32.Hasar,
                                                                                                       BozKurtxx_32.Karakter_Çantası.İçerik_Göster()))

                            if Seçim == '2':

                                while True:
                                    İşlem = input(
                                        'istediğiniz eşyanın sıra numarasını girin.\nVazgeçmek için q ya basın.')

                                    if İşlem == 'q':
                                        break

                                    try:
                                        print('**********\nEşyalar: {}\n**********'.format(
                                            BozKurtxx_32.Karakter_Çantası.İçerik_Göster()))
                                        if İşlem != 'q':
                                            Sıra = 1
                                            BozKurtxx_32.Eşya_Kullanma(
                                                BozKurtxx_32.Karakter_Çantası.içindekiler[int(İşlem) - 1], int(İşlem))
                                            break
                                    except:
                                         print('Hatalı İşlem:')
                            if Seçim == '3':
                                while True:
                                    try:
                                        print('**********\nEşyalar: {}\n**********'.format(
                                            BozKurtxx_32.Karakter_Çantası.İçerik_Göster()))
                                        Saldırı_Eşyası = input('Saldırmak İstediğiniz Eşyanın numarasını girin')
                                        Rakip.Can -= BozKurtxx_32.Saldırma(
                                            BozKurtxx_32.Karakter_Çantası.içindekiler[int(Saldırı_Eşyası) - 1])
                                        print(
                                            '\n>vurulan hasar {}\nRakip Kalan canı: {}<\n'.format(BozKurtxx_32.Saldırma(
                                                BozKurtxx_32.Karakter_Çantası.içindekiler[int(Saldırı_Eşyası) - 1]),
                                                Rakip.Can))
                                        Sıra = 1
                                        break
                                    except:
                                        print('Hatalı seçim')

                    elif Sıra == 1:
                        BozKurtxx_32.Can -= Rakip.Hasar
                        print('\n{} size {} hasar verdi\n'.format(Rakip.İsim, Rakip.Hasar))
                        Sıra = 2
                Rakip.Can = Geri_Dolum
                Orman.Bossa_Ulaşma_Sayısı -= 1





















