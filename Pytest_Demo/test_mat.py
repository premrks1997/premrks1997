import Pytest_Demo.mathlib
import pytest

from Pytest_Demo import mathlib


def test_calc_addition():
    #Verifytheoutputof`calc_addition`function”””
    output = mathlib.calc_addition(2, 4)
    assert output == 6
def test_calc_substraction():
    #Verifytheoutputof`calc_substraction`function”””
    output = mathlib.calc_substraction(2, 4)
    assert output == -2
def test_calc_multiply():
    #Verifytheoutputof`calc_multiply`function”””
    output = mathlib.calc_multiply(2, 4)
    assert output == 8