import math


class Fraction:
    def __init__(self, numerator, denominator):
        """Initialization numerator, denominator"""
        if denominator == 0:
            raise ValueError("Знаменник не може бути нульовим")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        """Reduces a fraction to the lowest common denominator"""
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        """Adding two fractions"""
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Subtraction of two fractions."""
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Multiplication of two fractions"""
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """Division of two fractions"""
        if other.numerator == 0:
            raise ValueError("Не можна ділити на нульовий чисельник")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __repr__(self):
        """The format of outputting a fraction in the form 'numerator/denominator'."""
        return f"{self.numerator}/{self.denominator}"


f1 = Fraction(1, 2)  # 1/2
f2 = Fraction(3, 4)  # 3/4

print(f"Дріб 1: {f1}")  # Виведе: 1/2
print(f"Дріб 2: {f2}")  # Виведе: 3/4

print(f"Додавання: {f1 + f2}")  # Виведе: 5/4
print(f"Віднімання: {f1 - f2}")  # Виведе: -1/4
