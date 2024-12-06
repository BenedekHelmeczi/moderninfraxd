from diak import Diak
import unittest

class TestDiakIntegration(unittest.TestCase):
    def test_targyak_es_atlag_szamitas(self):
        diak = Diak("Teszt Elek")
        diak.dolgozat_hozzaadasa("matematika", 20)
        diak.dolgozat_hozzaadasa("matematika", 79)

        diak.dolgozat_hozzaadasa("tortenelem", 95)
        diak.dolgozat_hozzaadasa("tortenelem", 80)

        diak.dolgozat_hozzaadasa("fizika", 45)
        diak.dolgozat_hozzaadasa("fizika", 70)

        self.assertAlmostEqual(diak.atlag_szamitas("matematika"), 49.5)
        self.assertAlmostEqual(diak.atlag_szamitas("tortenelem"), 87.5)
        self.assertAlmostEqual(diak.atlag_szamitas("fizika"), 57.5)

        self.assertAlmostEqual(diak.osszes_targy_atlag(), 87.5)

"""
teszt futtatása
python -m unittest <teszt-fájl-neve>.py
"""