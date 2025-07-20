import unittest
from app.calculator import calc_comm, calc_final

class TestOFPPTCalculator(unittest.TestCase):
    def test_calc_comm(self):
        self.assertAlmostEqual(calc_comm(12, 14, 10), 12.67, places=2)

    def test_calc_final(self):
        moyenne = calc_final(10, 12, 11, 13, 14, 13, 12)
        self.assertTrue(0 <= moyenne <= 20)
        self.assertAlmostEqual(moyenne, 12.83, places=2)

if __name__ == "__main__":
    unittest.main()
