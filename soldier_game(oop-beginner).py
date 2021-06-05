from random import randint

class Asker:
    def __init__(self):
        self.can = randint(30,70)
        self.hasar = randint(30,90)
        self.canli_mi = True

    def ol(self):
        self.canli_mi = False

    def hasar_al(self,alinan_hasar:int):
        if alinan_hasar >= self.can:
            self.ol()
        else:
            self.can -= alinan_hasar


class Oyuncu:
    def __init__(self):
        self.can = randint(300, 900)
        self.hasar = randint(30, 90)
        self.canli_mi = True

    def ol(self):
        self.canli_mi = False

    def hasar_al(self, alinan_hasar: int):
        if alinan_hasar >= self.can:
            self.ol()
        else:
            self.can -= alinan_hasar

askerler = [Asker() for i in range(10)]

oyuncu = Oyuncu()

while True:
    print('----Oyuncu Bilgileri----')

    print('Oyuncu Sağlık: {} --- Oyuncu Hasar: {}'.format(oyuncu.can,oyuncu.hasar))

    print('\n----Askerler----')

    for numara,asker in enumerate(askerler):
        if asker.canli_mi:
            print('{}.Asker--- Can değeri: {} --- Hasar Değeri: {}'.format(numara,asker.can,asker.hasar))

    secilen_asker = int(input('Saldırı için asker seciniz: '))
    if secilen_asker > len(askerler) - 1 or secilen_asker < 0:
        print('Girilen asker numarası yanlış')
        continue
    else:
        askerler[secilen_asker].hasar_al(oyuncu.hasar)

        if askerler[secilen_asker].canli_mi==False:
            askerler.remove(askerler[secilen_asker])
        if askerler:
            saldiran_asker = randint(0,len(askerler)-1)
            oyuncu.hasar_al(askerler[saldiran_asker].hasar)
        else:
            print('Tebrikler tüm düşmanlar öldü kazandın')
            quit()