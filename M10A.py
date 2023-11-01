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

hissi = Hissi(0,10)

print(f"Hissi on kerroksessa {hissi.sijainti}")
hissi.siirry_kerrokseen(6)
print(f"Hissi on kerroksessa {hissi.sijainti}")
hissi.kerros_up()
print(f"Hissi on kerroksessa {hissi.sijainti}")
hissi.kerros_down()
print(f"Hissi on kerroksessa {hissi.sijainti}")
hissi.siirry_kerrokseen(0)
print(f"Hissi on kerroksessa {hissi.sijainti}")