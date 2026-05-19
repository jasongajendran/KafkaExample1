from math import sqrt
def add_two_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply_two_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b    

#use square root function from math module
def calculate_square_root(x):
    """Calculate the square root of a number."""
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return sqrt(x)


# Test the function
result = add_two_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")
result = multiply_two_numbers(5, 3)
print(f"The product of 5 and 3 is: {result}")
result = calculate_square_root(25)
print(f"The square root of 25 is: {result}")
