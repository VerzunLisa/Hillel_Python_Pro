import shutil
import os


class BackupManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.backup_path = f"{file_path}.bak"

    def __enter__(self):
        if os.path.exists(self.file_path):
            shutil.copy2(self.file_path, self.backup_path)
            print(f"Створено резервну копію: {self.backup_path}")
        else:
            raise FileNotFoundError(f"Файл не знайдено: {self.file_path}")

        return self.file_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Виникла помилка: {exc_val}. Відновлюємо резервну копію.")
            shutil.copy2(self.backup_path, self.file_path)
            print(f"Резервну копію відновлено: {self.file_path}")
        else:
            os.remove(self.backup_path)
            print(f"Резервна копія видалена: {self.backup_path}")


try:
    with BackupManager('important_file.txt') as file:
        with open(file, 'r+') as f:
            content = f.read()
            print("Зміст файлу:", content)
            raise Exception("Приклад помилки під час обробки файлу.")

except Exception as e:
    print(f"Обробка файлу не вдалася: {e}")
