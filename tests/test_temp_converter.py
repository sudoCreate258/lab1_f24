import unittest
import c2f  # Import your module

class TestTempConversion(unittest.TestCase):
    def test_c2f(self):
        test_cases = [
            # (Celsius Input, Expected Fahrenheit Output)
            (20, 68),        # Room Temperature
            (0, 32),         # Freezing Point of Water
            (100, 212),      # Boiling Point of Water
            (37.78, 100)     # Very Hot Day
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
