def even_number_generator():
    """Генератор для нескінченної послідовності парних чисел."""
    number = 0
    while True:
        yield number
        number += 2


def save_even_numbers(file_path, limit=100):
    """Функція для збереження перших 'limit' парних чисел у файл."""
    with open(file_path, 'w') as file:
        gen = even_number_generator()
        for _ in range(limit):
            even_number = next(gen)
            file.write(f"{even_number}\n")


output_file = 'even_numbers.txt'
save_even_numbers(output_file, limit=100)
print(f"Перші 100 парних чисел збережено у файл {output_file}.")