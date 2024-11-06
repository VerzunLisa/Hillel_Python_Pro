from my_package.math_utils import factorial, gcd
from my_package.string_utils import to_upper, strip_spaces


def main():
    print("Факторіал 5:", factorial(5))
    print("НСД чисел 48 і 18:", gcd(48, 18))
    text = "   Hello, Python!   "
    print("Верхній регістр:", to_upper(text))
    print("Без пробілів на початку та в кінці:", strip_spaces(text))


if __name__ == "__main__":
    main()
