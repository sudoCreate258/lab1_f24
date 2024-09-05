import unittest
from temp_converter.temp_converter import c2f  # Import the function to be tested

class TestTempConversion(unittest.TestCase):

    def test_c2f(self):
        # Test cases for c2f function
        self.assertAlmostEqual(c2f(0), 32, places=2)    # Freezing point of water
        self.assertAlmostEqual(c2f(100), 212, places=2)  # Boiling point of water
        self.assertAlmostEqual(c2f(37.78), 100, places=2)  # Very hot day

if __name__ == "__main__":
    unittest.main()
