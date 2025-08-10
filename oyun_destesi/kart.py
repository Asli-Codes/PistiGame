from tkinter.ttk import Style
from colorama import Fore,Style

class Kart:
    def __init__(self, isim, deger):
        self.isim = isim
        self.deger = deger
        if self.deger == 'As' or self.deger =='Vale':
            self.puan = 1
        elif self.deger == 2 and self.isim == 'Sinek':
            self.puan = 2
        elif self.deger == 10 and self.isim == 'Karo':
            self.puan = 3
        else:
            self.puan = 0

    def __str__(self):
        semboller = {
            "Kupa":"♥",
            "Maça":"♠",
            "Karo":"♦",
            "Sinek":"♣"
        }
        renk = Fore.RED if self.isim in ["Kupa","Karo"] else Fore.WHITE
        return f"{renk}{semboller[self.isim]}{self.deger}{Style.RESET_ALL}({self.puan}p)"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    kart1 = Kart("Sinek", "As")
    kart2 = Kart("Karo", 10)
    kart3 = Kart("Kupa", 2)

    print(kart1)
    print(kart2)
    print(kart3)
