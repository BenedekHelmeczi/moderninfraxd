class Diak:
    def __init__(self, nev):
        self.nev = nev
        self.tantargyak = {
            "matematika": [],
            "tortenelem": [],
            "fizika": []
        }

    def dolgozat_hozzaadasa(self, tantargy, pontszam):
        if tantargy in self.tantargyak:
            if isinstance(pontszam, int) and pontszam >= 0:
                self.tantargyak[tantargy].append(pontszam)
            else:
                raise ValueError("A pontszám egy nemnegatív egész szám kell, hogy legyen.")
        else:
            raise ValueError(f"{tantargy} nem érvényes tantárgy.")

    def atlag_szamitas(self, tantargy):
        if tantargy in self.tantargyak:
            dolgozatok = self.tantargyak[tantargy]
            if dolgozatok:
                return sum(dolgozatok) / len(dolgozatok)
            return None
        else:
            raise ValueError(f"{tantargy} nem érvényes tantárgy.")

    def osszes_targy_atlag(self):

        osszes_dolgozat = []
        for tantargy, dolgozatok in self.tantargyak.items():
            osszes_dolgozat.extend(dolgozatok)
        if osszes_dolgozat:
            return sum(osszes_dolgozat) / len(osszes_dolgozat)
        return None
