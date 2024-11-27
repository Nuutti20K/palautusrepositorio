class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin pitää olla epänegatiivinen kokonaisluku")

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon pitää olla epänegatiivinen kokonaisluku")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujoukko = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.lukujoukko:
            return True
        else:
            return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujoukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm >= len(self.lukujoukko):
                kasvatettu = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(self.lukujoukko, kasvatettu)
                self.lukujoukko = kasvatettu

    #def poista(self, luku):
    #    if luku in self.lukujoukko:
    #        self.lukujoukko.remove(luku)
    #        self.lukujoukko.append(0)
    #        self.alkioiden_lkm -= 1

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujoukko[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujoukko[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.lukujoukko[j]
                self.lukujoukko[j] = self.lukujoukko[j + 1]
                self.lukujoukko[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(len(taulu)):
            taulu[i] = self.lukujoukko[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujoukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujoukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujoukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
