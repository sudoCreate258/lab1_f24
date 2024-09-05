import pytest
from temp_converter import c2f, f2c

def test_c2f():
    assert round(c2f(0), 2) == 32  # Freezing point of water
    assert round(c2f(100), 2) == 212  # Boiling point of water
    assert round(c2f(37.78), 2) == 100  # Very hot day
