class Price:
    def __init__(self, amount):
        """Initialization amount"""
        self.amount = amount

    @staticmethod
    def _round_two_decimal(value):
        return round(value, 2)

    def __add__(self, other):
        """Adding two prices"""
        return Price(self.amount + other.amount)

    def __sub__(self, other):
        """Subtraction of two prices"""
        return Price(self.amount - other.amount)

    def __eq__(self, other):
        """Determination of the equality of two prices"""
        return self.amount == other.amount

    def __lt__(self, other):
        """Comparing two prices, is the first price lower than the second"""
        return self.amount < other.amount

    def __gt__(self, other):
        """Comparing two prices, whether the first price is greater than the second"""
        return self.amount > other.amount

    def __repr__(self):
        """Representation of the price with no more than 2 decimal places"""
        return f"{self.amount:.2f}"


p1 = Price(18.256)
p2 = Price(4.504)

print(f"Ціна 1: {p1}")
print(f"Ціна 2: {p2}")
print(f"Додавання: {p1 + p2}")
print(f"Віднімання: {p2 - p1}")

print(f"Ціна 1 == Ціна 2: {p1 == p2}")
print(f"Ціна 1 < Ціна 2: {p1 < p2}")
print(f"Ціна 1 > Ціна 2: {p1 > p2}")
