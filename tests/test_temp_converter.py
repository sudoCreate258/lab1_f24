# tests/test_temp_converter.py
import pytest
from temp_converter import c2f

def test_c2f_freezing_point():
    # This should pass as the freezing point of water is correctly converted
    assert round(c2f(0), 2) == 32.0

def test_c2f_boiling_point():
    # This should fail if the implementation is incorrect
    assert round(c2f(100), 2) == 212.0

def test_c2f_hot_day():
    # This should fail if the implementation is incorrect
    assert round(c2f(37.78), 2) == 100.0

def test_c2f_failure_case():
    # This should fail to match your expected result for failure cases
    assert round(c2f(0), 2) == 31.0  # This should fail based on your function
