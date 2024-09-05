import pytest
from temp_converter import c2f

def test_c2f_freezing_point():
    assert round(c2f(0), 2) == 32.0     # Freezing point of water

def test_c2f_boiling_point():
    assert round(c2f(100), 2) == 212.0   # Boiling point of water

def test_c2f_very_hot_day():
    assert round(c2f(37.78), 2) == 100.0 # Very hot day

def test_c2f_order_independent():
    # Ensure that this test passes based on correct functionality
    assert round(c2f(25), 2) == 77.0     # Example with correct expected value
