class Talo:
    def __init__(self, alin, ylin, hissi):
        self.alin = alin
        self.ylin = ylin
        self.hissi = []

        for i in range(hissi):
            self.hissi.append(Hissi(self.alin, self.alin))

    def aja_hissi(self, numero, kerros):
        self.hissi[numero].siirry_kerrokseen(kerros)

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = self.alin

    def siirry_kerrokseen(self, kerroksen_muutos):
        while kerroksen_muutos != self.sijainti:
            if kerroksen_muutos < self.sijainti:
                self.sijainti -= 1
            else:
                self.sijainti += 1


    def kerros_up(kerros_muutos):
        kerros_muutos.sijainti += 1

    def kerros_down(kerros_muutos):
        kerros_muutos.sijainti -= 1

talo = Talo(0, 10, 3)
talo.aja_hissi(0,8)
talo.aja_hissi(1,6)
talo.aja_hissi(2,10)
print(f"Hissi 1 menee kerrokseen {talo.hissi[0].sijainti}")
print(f"Hissi 2 menee kerrokseen {talo.hissi[1].sijainti}")
print(f"Hissi 3 menee kerrokseen {talo.hissi[2].sijainti}")