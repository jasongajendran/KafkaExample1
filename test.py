from math import sqrt
from typing import Union


def add_two_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers and return the result.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The sum of a and b
    """
    return a + b


def multiply_two_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers and return the result.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The product of a and b
    """
    return a * b


def calculate_square_root(x: Union[int, float]) -> float:
    """
    Calculate the square root of a number using the math module.

    Args:
        x: A non-negative number (int or float)

    Returns:
        The square root of x

    Raises:
        ValueError: If x is negative
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return sqrt(x)


if __name__ == "__main__":
    # Test the functions
    result = add_two_numbers(5, 3)
    print(f"The sum of 5 and 3 is: {result}")
    result = multiply_two_numbers(5, 3)
    print(f"The product of 5 and 3 is: {result}")
    result = calculate_square_root(25)
    print(f"The square root of 25 is: {result}")
