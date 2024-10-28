def log_error_generator(log_file_path):
    """
    Генератор, що читає лог-файл і повертає тільки рядки з кодами помилок 4XX або 5XX.
    """
    with open(log_file_path, 'r') as file:
        for line in file:
            status_code = int(line.split()[-2])
            if 400 <= status_code < 600:
                yield line


def write_errors_to_file(log_file_path, error_file_path):
    """
    Функція, що зчитує лог-файл, отримує рядки з помилками та записує їх у новий файл.
    """
    with open(error_file_path, 'w') as error_file:
        for error_line in log_error_generator(log_file_path):
            error_file.write(error_line)


log_file = 'server.log'
error_log_file = 'errors.log'
write_errors_to_file(log_file, error_log_file)
print(f"Помилки записані у файл {error_log_file}")
