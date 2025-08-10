from kart import Kart
import random

class Deste:
    def __init__(self):
        isimler = ['Sinek', 'Karo', 'Kupa', 'Maça']
        degerler = ['As', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Vale', 'Kız', 'Papaz']
        self.kartlar = []
        for isim in isimler:
            for deger in degerler:
                kart = Kart(isim, deger)
                self.kartlar.append(kart)
        self.__karistir()

    def __str__(self):
        return str(self.kartlar)

    def kart_ver(self):
        if self.kartlar:
            return self.kartlar.pop(0)
        else:
            return None

    def __karistir(self):
        random.shuffle(self.kartlar)


if __name__ == "main":
    deste = Deste()

    print(deste)
