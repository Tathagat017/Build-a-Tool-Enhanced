"""
Mathematical tools for the reasoning script.
Contains functions for basic arithmetic, averages, square roots, etc.
"""

import math


def calculate_average(*numbers):
    """Calculate the average of given numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        return None  # Cannot calculate square root of negative number
    return math.sqrt(number)


def calculate_sum(*numbers):
    """Calculate the sum of given numbers."""
    return sum(numbers)


def calculate_product(*numbers):
    """Calculate the product of given numbers."""
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result


def calculate_power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent


def calculate_factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return None  # Factorial not defined for negative numbers
    return math.factorial(int(n))


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def calculate_percentage(part, whole):
    """Calculate what percentage 'part' is of 'whole'."""
    if whole == 0:
        return 0
    return (part / whole) * 100


# Tool registry for easy access
MATH_TOOLS = {
    'average': calculate_average,
    'square_root': calculate_square_root,
    'sum': calculate_sum,
    'product': calculate_product,
    'power': calculate_power,
    'factorial': calculate_factorial,
    'is_prime': is_prime,
    'percentage': calculate_percentage
} 