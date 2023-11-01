import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def accelerate(self, nopeuden_muutos):
        self.nopeuden_muutos = nopeuden_muutos
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, hour_count):
        self.hour_count = hour_count
        self.matka += (self.nopeus * hour_count)

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(kuluminen):
        for auto in kuluminen.autot:
            auto.accelerate(random.randint(-10,15))
            auto.kulje(1)

    def tulosta_tilanne(tilanne):
        for auto in tilanne.autot:
            print(f"""
            =========================================
            |Rekkari: {auto.rekisteritunnus}        
            |Huippunopeus: {auto.huippunopeus}km/h  
            |Tämänhetkinen nopeus: {auto.nopeus}km/h
            |Kuljettu matka: {auto.matka}km         
            =========================================
            """)

    def kilpailu_ohi(maali):
        for auto in maali.autot:
            if auto.matka >= maali.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    huippu_nopeus = random.randint(100,200)
    auto = Auto(f"ABC-{i}", huippu_nopeus)
    autot.append(auto)

kilpailu = Kilpailu(f"Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if tunnit == 10:
        kilpailu.tulosta_tilanne()
    tunnit += 1

    if tunnit > 10:
        tunnit = 0
kilpailu.tulosta_tilanne()