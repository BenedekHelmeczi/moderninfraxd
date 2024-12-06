from diak import Diak
import unittest

class TestDiakUnit(unittest.TestCase):
    def test_dolgozat_hozzaadasa(self):
        diak = Diak("Teszt Elek")
        diak.dolgozat_hozzaadasa("matematika", 95)
        self.assertEqual(diak.tantargyak["matematika"], [95])
        diak.dolgozat_hozzaadasa("matematika", 80)
        self.assertEqual(diak.tantargyak["matematika"], [95, 80])

"""
Unit teszt futtatása
python -m unittest <teszt-fájl-neve>.py
"""