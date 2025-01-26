import pytest
from source import experiment_code1, experiment_code2, experiment_code3

# Test experiment_code1
def test_experiment_code1_scalene():
    # Test for scalene triangle
    result = experiment_code1(3, 4, 5)
    assert result == (3, 4, 5)

def test_experiment_code1_equilateral():
    # Test for equilateral triangle
    result = experiment_code1(3, 3, 3)
    assert result == (3, 3, 3)

def test_experiment_code1_isosceles():
    # Test for isosceles triangle
    result = experiment_code1(3, 3, 5)
    assert result == (3, 3, 5)

# Test experiment_code2
def test_experiment_code2_all_equal():
    # Test when all inputs are equal
    result = experiment_code2(1, 1, 1, 1, 1, 1)
    assert result == (1, 1, 1, 1, 1, 1)

def test_experiment_code2_not_all_equal():
    # Test when not all inputs are equal
    result = experiment_code2(1, 2, 3, 4, 5, 6)
    assert result == (1, 2, 3, 4, 5, 6)

def test_experiment_code2_partial_equality():
    # Test when some inputs are equal
    result = experiment_code2(1, 1, 1, 2, 3, 4)
    assert result == (1, 1, 1, 2, 3, 4)

# Test experiment_code3
def test_experiment_code3_case1():
    # Test where first condition is True and nested conditions are checked
    result = experiment_code3(2, 10, 3, 19, 7)
    assert result == (2, 10, 3, 19, 7)

def test_experiment_code3_case2():
    # Test where first condition is False
    result = experiment_code3(1, 2, 3, 4, 5)
    assert result == (1, 2, 3, 4, 5)

def test_experiment_code3_case3():
    # Test where first condition is True but nested conditions vary
    result = experiment_code3(2, 10, 3, 15, 4)
    assert result == (2, 10, 3, 15, 4)

def test_experiment_code3_case4():
    # Test where first condition is True but b != 10
    result = experiment_code3(2, 5, 3, 19, 7)
    assert result == (2, 5, 3, 19, 7)
