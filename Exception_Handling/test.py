"""
Python Script for Exception Handling and Unit Testing

This script demonstrates:
- Exception handling using try-except-finally
- Raising custom exceptions
- Unit testing with unittest framework

"""

import unittest

def divide(a, b):
    """Function to divide two numbers with exception handling"""
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    finally:
        print("Execution of divide function complete")

def validate_input(value):
    """Function to validate input between 5 and 9"""
    if value < 5 or value > 9:
        raise ValueError("Value should be between 5 and 9")
    return value

# Unit Test Class
class TestErrorHandling(unittest.TestCase):
    """Unit tests for exception handling functions"""

    def test_divide_valid(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_validate_input_valid(self):
        self.assertEqual(validate_input(6), 6)

    def test_validate_input_invalid(self):
        with self.assertRaises(ValueError):
            validate_input(10)

if __name__ == "__main__":
    unittest.main()
