from diak import Diak
import unittest

class TestDiakIntegration(unittest.TestCase):
    def test_average(self):
        diak = Diak("Teszt Elek")
        diak.add_points("matematika", 20)
        diak.add_points("matematika", 80)

        diak.add_points("tortenelem", 95)
        diak.add_points("tortenelem", 80)

        diak.add_points("fizika", 45)
        diak.add_points("fizika", 70)

        self.assertAlmostEqual(diak.calc_average("matematika"), 50)
        self.assertAlmostEqual(diak.calc_average("tortenelem"), 87.5)
        self.assertAlmostEqual(diak.calc_average("fizika"), 57.5)

        self.assertAlmostEqual(diak.calc_all_average(), 65)


if __name__ == '__main__':
    unittest.main()
