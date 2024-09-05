# tests/test_temp_converter.py
import pytest
from temp_converter import c2f

def test_c2f_freezing_point():
    # This test is expected to pass
    assert round(c2f(0), 2) == 32.0  # Freezing point of water

def test_c2f_boiling_point():
    # This test is expected to fail
    assert round(c2f(100), 2) == 212.0  # Boiling point of water

def test_c2f_hot_day():
    # This test is expected to fail
    assert round(c2f(37.78), 2) == 100.0  # Very hot day

def test_c2f_failure_case():
    # This test is expected to fail
    assert round(c2f(0), 2) == 31.0  # This should fail based on your function
