def line_filter(file_path, keyword):
    """Генератор, який повертає рядки з файлу, що містять певне ключове слово."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                yield line


def save_filtered_lines(input_file, output_file, keyword):
    """Функція для збереження відфільтрованих рядків у новий файл."""
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for filtered_line in line_filter(input_file, keyword):
            out_file.write(filtered_line)


input_file = 'large_log.txt'
output_file = 'filtered_log.txt'
keyword = 'ERROR'
save_filtered_lines(input_file, output_file, keyword)
print(f"Відфільтровані рядки з ключовим словом '{keyword}' збережено у файл {output_file}.")
