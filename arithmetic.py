"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    sum = (num1+num2)

    return sum


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    remain = (num1 - num2)
    return remain


def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    mult = (num1 * num2)
    return mult

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    div = (num1 / num2 )
    return div

def square(num1):
    """Return the square of num1."""
    square = num1 ** 2
    return square

def cube(num1):
    """Return the cube of num1."""
    cube = num1 ** 3
    return cube


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    sq = pow(num1, num2)
    return sq

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    modulus = num1 % num2
    return modulus