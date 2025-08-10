from deste import Deste

class Oyuncu:
    def __init__(self, isim):
        self.isim = isim
        self.el = []
        self.toplanan = []
        self.pisti_sayisi = 0

    def __str__(self):
        el_str = str(self.el)
        toplanan_str = str(self.toplanan)
        return f"{self.isim} ({self.skor()}):\n\tEl: {el_str}\n\tToplanan: {toplanan_str}\n\tPisti: {self.pisti_sayisi}"

    def kart_at(self, index):
        """Elindeki kartlardan belirtilen indeksteki kartı atar."""
        if 0 <= index < len(self.el):
            return self.el.pop(index)
        else:
            return None

    def topla(self, kartlar):
        """Verilen kartları toplayarak oyuncunun toplanan kartlarına ekler."""
        self.toplanan.extend(kartlar)

    def pisti(self):
        """Pisti sayısını artırır."""
        self.pisti_sayisi += 1

    def skor(self):
        cevap = self.pisti_sayisi * 10
        for kart in self.toplanan:
            cevap += kart.puan
        return cevap


if __name__ == "__main__":
    oyuncu1 = Oyuncu("Aslı")
    oyuncu2 = Oyuncu("Barbaros")

    deste = Deste()
    for i in range(4):
        oyuncu1.el.append((deste.kart_ver()))
        oyuncu2.el.append(deste.kart_ver())

    print(oyuncu1)
    print()
    print(oyuncu2)
    print()
    print(deste)