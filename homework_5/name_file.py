import os


class DirectoryIterator:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration
        file_name = self.files[self.index]
        file_path = os.path.join(self.directory_path, file_name)
        file_size = os.path.getsize(file_path)
        self.index += 1
        return file_name, file_size


directory = './my_directory'  # Задайте шлях до каталогу
iterator = DirectoryIterator(directory)
for file_name, file_size in iterator:
    print(f"Файл: {file_name}, Розмір: {file_size} байт")
    