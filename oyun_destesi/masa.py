import random
from deste import Deste
from kart import Kart
from oyuncu import Oyuncu

class Masa:
    def __init__(self, oyuncular: list[Oyuncu]):
        self.deste = Deste()
        self.orta: list[Kart] = [self.deste.kart_ver() for _ in range(4)]
        self.oyuncular = oyuncular

    def dagit(self):
        """Her oyuncuya 4 kart dağıtır."""
        for oyuncu in self.oyuncular:
            for _ in range(4):
                kart = self.deste.kart_ver()
                if kart:
                    oyuncu.el.append(kart)

    def el_oyna(self):
        """Her oyuncunun elindeki kartlar oynar."""
        for oyuncu in self.oyuncular:
            if oyuncu.el:
                rastgele_index = random.randint(0, len(oyuncu.el) - 1)
                kart = oyuncu.kart_at(rastgele_index)
                if kart:
                   print(f"{oyuncu.isim} {kart} kartını oynadı.")
                   if self.kural_kontrol(kart):
                      print(f"{oyuncu.isim} kuralı geçerli!")
                      if len(self.orta) == 1:
                         print(f"{oyuncu.isim} pisti yaptı!")
                         oyuncu.pisti()
                      self.orta.append(kart)
                      oyuncu.topla(self.orta)
                      self.orta.clear()
                   else:
                       self.orta.append(kart)


    def kural_kontrol(self, atilan: Kart):
        if self.orta:
            if atilan.deger == self.orta[-1].deger:
                return True
        return False

    def oyna(self):
        while self.deste.kartlar:
            self.dagit()
            for _ in range(4):
                self.el_oyna()


if __name__ == "__main__":

     oyuncu1 = Oyuncu("Aslı")
     oyuncu2 = Oyuncu("Barbaros")
     oyuncu3 = Oyuncu("Ecem")
     oyuncu4 = Oyuncu("Rüzgar")
     oyuncular = [oyuncu1, oyuncu2, oyuncu3, oyuncu4]

     masa = Masa(oyuncular)
     masa.oyna()

     for oyuncu in oyuncular:
         print(oyuncu)
         print()

     print(f"Orta alandaki kartlar ({len(masa.orta)}):", masa.orta)