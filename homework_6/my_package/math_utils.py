def factorial(n):
    """Calculation of the factorial of a number n."""
    if n < 0:
        raise ValueError("Факторіал не визначений для від'ємних чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    """Finding the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a
