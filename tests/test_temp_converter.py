# tests/test_temp_converter.py
import pytest
from temp_converter import c2f

def test_c2f_pass():
    assert round(c2f(0), 2) == 32.0     # This should pass

def test_c2f_fail_1():
    assert round(c2f(100), 2) == 211.0   # This should fail

def test_c2f_fail_2():
    assert round(c2f(37.78), 2) == 99.0 # This should fail

def test_c2f_fail_3():
    assert round(c2f(20), 2) == 68.0     # This should fail
