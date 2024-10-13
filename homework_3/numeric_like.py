import math


class Vector(object):
    """ Working with vectors"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        """Adding two vectors """
        return Vector(self.a + other.a, self.a + other.b)

    def __sub__(self, other):
        """Subtracting two vectors"""
        return Vector(self.a - other.a, self.b - other.b)

    def __mul__(self, scalar):
        """Multiplying a vector by a scalar number"""
        return Vector(self.a * scalar, self.b * scalar)

    def __eq__(self, other):
        """Determining whether two vectors are equal"""
        return Vector(self.a == other.a, self.b == other.b)

    def length(self):
        """Calculating the length of a vector"""
        return math.sqrt(self.a**2 + self.b**2)

    def __lt__(self, other):
        """Compare the length of two vectors"""
        return self.length() < other.length()

    def __repr__(self):
        """Deriving the answer"""
        return f"Vector({self.a}, {self.b})"


vector1 = Vector(2, 5)
vector2 = Vector(1, 3)

print(vector1 - vector2)
print(vector1 + vector2)
print(vector2 * 3)
print(vector2.length())
print(vector2 == vector1)
