import unittest
from temp_converter import c2f, main  # Import your module

class TestTempConversion(unittest.TestCase):
    def test_c2f(self):
        test_cases = [
            # (Celsius Input, Expected Fahrenheit Output, Incorrect Fahrenheit Output)
            (20, 68, 104),        # Room Temperature
            (0, 32, 0),           # Freezing Point of Water
            (100, 212, 180),      # Boiling Point of Water
            (37.78, 100, 68)      # Very Hot Day
        ]
        
        for cel, expected_fah in test_cases:
            with self.subTest(c=cel):
                self.assertAlmostEqual(c2f(cel), expected_fah, places=2)

    def test_main_output(self):
        cel = 100
        expected_fah = 212
        self.assertAlmostEqual(main(cel), expected_fah, places=2)

if __name__ == "__main__":
    unittest.main()
