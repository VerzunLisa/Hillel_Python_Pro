def is_even(n: int) -> bool:
    """
    Перевіряє, чи є число парним.

    Приклади:
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-3)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Обчислює факторіал числа.

    Приклади:
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: Факторіал визначений тільки для невід'ємних чисел.
    """
    if n < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних чисел.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
