import pytest
from temp_converter import c2f

def test_c2f():
    # Valid cases for c2f
    assert round(c2f(0), 2) == 32.0     # Freezing point of water
    assert round(c2f(100), 2) == 212.0   # Boiling point of water
    assert round(c2f(37.78), 2) == 100.0 # Very hot day

def test_c2f_failure_case():
    # Intentionally failing test cases for c2f
    assert round(c2f(0), 2) == 30.0  # This should fail based on your function
    assert round(c2f(100), 2) == 210.0  # This should fail based on your function
    assert round(c2f(37.78), 2) == 102.0  # This should fail based on your function
