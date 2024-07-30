import random as rnd  # random modülünü içe aktar


class Iskambil:  # iskambil adında sınıf tanımladık
    turler = ["KARO", "KUPA", "MAÇA", "SİNEK"]  # türler adında bir liste oluşturduk
    sayilar = ["A"] + [str(x) for x in range(2, 11)] + ["J", "Q", "K"]  # sayılar adında bir liste oluşturduk
    DKS = 52  # bir destedeki kart sayısını tanımladık

    def __init__(self):  # sınıf oluşturma metodu
        self.destem = []  # destem adlı bir liste oluşturulmuş

    def olustur(self, *x):  # *x= değişken sayıda argüman alabilir demek. olustur adında bir metod oluşturduk
        param = x[0]
        if param == 1:
            for tur in self.turler:
                for sayi in self.sayilar:
                    self.destem.append(tur + " " + sayi)
            print(self.destem)
        elif param == 2:
            self.destem = [tur + " " + sayi for tur in self.turler for sayi in self.sayilar]
            print(self.destem)
        elif param == 3:  # Hatalı çalışıyordu, düzeltildi
            self.destem = [tur + " " + sayi for tur in self.turler for sayi in self.sayilar]
            print(self.destem)

    def karistir(self, *x):
        param = x[0]
        if param == 1:
            rnd.shuffle(self.destem)
        elif param == 2:
            self.destem = rnd.sample(self.destem, self.DKS)

    def kes(self):
        rs = rnd.randint(1, self.DKS - 1)
        self.destem = self.destem[rs:] + self.destem[:rs]
        print(self.destem)

    def dagit(self, adet=4):
        kartlar = []
        for _ in range(adet):
            kartlar.append(self.destem.pop(0))
        return kartlar


# Sınıfı kullanarak test edelim
abc = Iskambil()
abc.olustur(1)
abc.karistir(1)
abc.kes()
