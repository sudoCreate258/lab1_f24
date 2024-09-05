# tests/test_temp_converter.py
import pytest
from temp_converter import c2f

def test_c2f():
    assert round(c2f(0), 2) == 32.0     # Freezing point of water (This should pass)
    assert round(c2f(100), 2) == 211.0   # Boiling point of water (Expected to fail)
    assert round(c2f(37.78), 2) == 99.0 # Very hot day (Expected to fail)
    assert round(c2f(20), 2) == 68.0     # Normal temperature (Expected to fail)
