import unittest
from temp_converter import c2f

class TestTempConversion(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(c2f(0), 32, places=2)

    def test_boiling_point(self):
        self.assertAlmostEqual(c2f(100), 212, places=2)

    def test_hot_day(self):
        self.assertAlmostEqual(c2f(37.78), 100, places=2)

    def test_edge_case(self):
        self.assertAlmostEqual(c2f(-40), -40, places=2)  # Freezing point of Celsius in Fahrenheit

if __name__ == '__main__':
    unittest.main()
