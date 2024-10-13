import math


class Vector:

    def __init__(self, *component):
        """Initialization components vector"""
        self.component = component

    def __repr__(self):
        """Returns representation Vector"""
        return f"Вектор {self.component}"

    def __add__(self, other):
        """Adding vectors"""
        if len(self.component) == len(other.component):
            result = tuple(a + b for a, b in zip(self.component, other. component))
            return Vector(*result)
        else:
            print("Вектори повинні мати однакову кількість вимірів.")

    def __sub__(self, other):
        """Subtraction of vectors"""
        if len(self.component) == len(other.component):
            result = tuple(a - b for a, b in zip(self.component, other. component))
            return Vector(*result)
        else:
            print("Вектори повинні мати однакову кількість вимірів.")

    def __mul__(self, other):
        """Scalar product of vectors"""
        if len(self.component) == len(other.component):
            result = tuple(a * b for a, b in zip(self.component, other. component))
            return Vector(*result)
        else:
            print("Вектори повинні мати однакову кількість вимірів.")

    def magnitude(self):
        """Calculates the length of a vector"""
        return math.sqrt(sum(x ** 2 for x in self.component))

    def __eq__(self, other):
        """Determining whether two vectors are equal"""
        return self.magnitude() == other.magnitude

    def __lt__(self, other):
        """Compare the length of two vectors"""
        return self.magnitude() < other.magnitude()

    def __gt__(self, other):
        """Compare the length of two vectors"""
        return self.magnitude() > other.magnitude()


vect1 = Vector(18, 25, 6)
vect2 = Vector(13, 8, 76)
vect3 = Vector(43, 20, 6, 9)

print(vect1-vect2)
print(vect3+vect2)
