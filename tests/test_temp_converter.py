import pytest
from temp_converter import c2f

def test_c2f_freezing_point():
    assert round(c2f(0), 2) == 32.0  # Freezing point of water

def test_c2f_boiling_point():
    assert round(c2f(100), 2) == 212.0  # Boiling point of water

def test_c2f_very_hot_day():
    assert round(c2f(37.78), 2) == 100.0  # Very hot day

# Additional tests
def test_c2f_order_independent():
    values = [0, 100, 37.78]
    results = [c2f(value) for value in values]
    expected = [32.0, 212.0, 100.0]
    for result, exp in zip(results, expected):
        assert round(result, 2) == exp
