from concurrent.futures import ProcessPoolExecutor
import math
from functools import reduce


def factorial_partial(start, end):
    """Обчислення часткового факторіалу в діапазоні [start, end]."""
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def calculate_chunk(chunk):
    """Обгортка для передачі діапазону в pool."""
    return factorial_partial(chunk[0], chunk[1])


def parallel_factorial(n, num_workers=4):
    """Паралельне обчислення факторіалу числа n."""
    if n == 0 or n == 1:
        return 1

    # Розподіляємо роботу між процесами
    chunk_size = n // num_workers
    ranges = [
        (i * chunk_size + 1, (i + 1) * chunk_size if i < num_workers - 1 else n)
        for i in range(num_workers)
    ]

    # Використовуємо ProcessPoolExecutor для паралельного виконання
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = executor.map(calculate_chunk, ranges)

    # Підсумовуємо часткові результати
    return reduce(lambda x, y: x * y, results)


if __name__ == "__main__":
    large_number = 850
    print(f"Обчислення факторіалу {large_number}...")
    result = parallel_factorial(large_number, num_workers=8)
    print(f"Факторіал {large_number} обчислено. Кількість цифр у результаті: {len(str(result))}")
