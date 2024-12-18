import os
from concurrent.futures import ThreadPoolExecutor
from typing import List


def search_in_file(file_path: str, search_text: str) -> List[str]:
    """
    Шукає заданий текст у файлі та повертає список рядків, які містять цей текст.

    :param file_path: Шлях до файлу.
    :param search_text: Текст для пошуку.
    :return: Список рядків із текстом.
    """
    matching_lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, start=1):
                if search_text in line:
                    matching_lines.append(f"{file_path} (рядок {line_num}): {line.strip()}")
    except Exception as e:
        print(f"Помилка читання файлу {file_path}: {e}")
    return matching_lines


def search_in_files_concurrently(directory: str, search_text: str, max_workers: int = 4) -> None:
    """
    Виконує паралельний пошук тексту у файлах каталогу.

    :param directory: Шлях до каталогу.
    :param search_text: Текст для пошуку.
    :param max_workers: Кількість потоків для обробки.
    """
    # Отримуємо список файлів у каталозі
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Використовуємо ThreadPoolExecutor для паралельного виконання
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(search_in_file, file, search_text): file for file in files}

        # Обробка результатів
        for future in futures:
            try:
                matching_lines = future.result()
                if matching_lines:
                    for line in matching_lines:
                        print(line)
            except Exception as e:
                print(f"Помилка у файлі {futures[future]}: {e}")


if __name__ == "__main__":
    directory_path = "files"
    search_query = "hobbies"
    search_in_files_concurrently(directory_path, search_query)
