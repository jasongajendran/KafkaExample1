import pytest
from test import add_two_numbers, multiply_two_numbers


class TestAddTwoNumbers:
    """Test cases for add_two_numbers function"""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        assert add_two_numbers(5, 3) == 8
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers"""
        assert add_two_numbers(-5, -3) == -8
    
    def test_add_mixed_signs(self):
        """Test adding positive and negative numbers"""
        assert add_two_numbers(5, -3) == 2
        assert add_two_numbers(-5, 3) == -2
    
    def test_add_zero(self):
        """Test adding with zero"""
        assert add_two_numbers(5, 0) == 5
        assert add_two_numbers(0, 0) == 0
    
    def test_add_floats(self):
        """Test adding floating point numbers"""
        assert add_two_numbers(5.5, 3.2) == pytest.approx(8.7)
    
    def test_add_large_numbers(self):
        """Test adding large numbers"""
        assert add_two_numbers(1000000, 2000000) == 3000000


class TestMultiplyTwoNumbers:
    """Test cases for multiply_two_numbers function"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers"""
        assert multiply_two_numbers(5, 3) == 15
    
    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers"""
        assert multiply_two_numbers(-5, -3) == 15
    
    def test_multiply_mixed_signs(self):
        """Test multiplying positive and negative numbers"""
        assert multiply_two_numbers(5, -3) == -15
        assert multiply_two_numbers(-5, 3) == -15
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply_two_numbers(5, 0) == 0
        assert multiply_two_numbers(0, 0) == 0
    
    def test_multiply_by_one(self):
        """Test multiplying by one"""
        assert multiply_two_numbers(5, 1) == 5
        assert multiply_two_numbers(-5, 1) == -5
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers"""
        assert multiply_two_numbers(5.5, 3.2) == pytest.approx(17.6)
    
    def test_multiply_large_numbers(self):
        """Test multiplying large numbers"""
        assert multiply_two_numbers(1000, 2000) == 2000000