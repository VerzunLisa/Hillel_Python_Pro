def memoize(a):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Отримано з кешу {args}")
            return cache[args]
        else:
            result = a(*args)
            cache[args] = result
            print(f"Збережено в кеш {args}")
            return result
    return wrapper


def factor(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factor(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(factor(7))
print(fibonacci(16))
