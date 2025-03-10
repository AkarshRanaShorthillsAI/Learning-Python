"""
Fraction Data Type Implementation using Object-Oriented Programming in Python.
This class allows users to:
1. Represent fractions
2. Perform arithmetic operations (+, -, *, /)
3. Display fractions in a readable format

Special methods (__add__, __sub__, __mul__, __truediv__) are used to overload operators.
"""

class Fraction:
    """Class representing a mathematical fraction."""
    
    def __init__(self, numerator, denominator):
        """Constructor to initialize the fraction with numerator and denominator."""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.num = numerator
        self.den = denominator
    
    def __str__(self):
        """Returns a string representation of the fraction."""
        return f"{self.num}/{self.den}"
    
    def __add__(self, other):
        """Overloads the + operator to add two fractions."""
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __sub__(self, other):
        """Overloads the - operator to subtract two fractions."""
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __mul__(self, other):
        """Overloads the * operator to multiply two fractions."""
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __truediv__(self, other):
        """Overloads the / operator to divide two fractions."""
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

# Example usage
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

print("Fraction 1:", frac1)
print("Fraction 2:", frac2)
print("Addition:", frac1 + frac2)
print("Subtraction:", frac1 - frac2)
print("Multiplication:", frac1 * frac2)
print("Division:", frac1 / frac2)
