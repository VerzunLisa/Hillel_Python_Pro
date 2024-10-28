import json


class ConfigManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def __enter__(self):
        try:
            with open(self.file_path, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"Файл конфігурації не знайдено: {self.file_path}. Створюємо новий.")
            self.config = {}
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_path, 'w') as file:
            json.dump(self.config, file, indent=4)
        if exc_type:
            print(f"Виникла помилка: {exc_val}")


config_file = 'config.json'

with ConfigManager(config_file) as config:
    print("Поточна конфігурація:", config)
    config['new_setting'] = 'new_value'
    config['version'] = 1.0

print("Конфігурацію збережено.")
