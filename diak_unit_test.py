from diak import Diak
import unittest

class TestDiakUnit(unittest.TestCase):
    def test_add_points(self):
        diak = Diak("Teszt Elek")
        diak.add_points("matematika", 95)
        self.assertEqual(diak.subjects["matematika"], [95])
        diak.add_points("matematika", 80)
        self.assertEqual(diak.subjects["matematika"], [95, 80])



if __name__ == '__main__':
    unittest.main()
