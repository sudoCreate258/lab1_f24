import unittest
from temp_converter import c2f, main  # Import your module

class TestTempConversion(unittest.TestCase):
    def test_c2f(self):
        # Test cases (input, expected output)
        test_cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (37.78, 100)
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
