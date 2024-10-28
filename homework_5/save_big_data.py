import zipfile
import os


class ZipArchiveManager:
    def __init__(self, archive_name):
        """initializes the file"""
        self.archive_name = archive_name
        self.archive = None

    def __enter__(self):
        """Open the archive in recording mode"""
        self.archive = zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED)
        print(f"'{self.archive_name}' створено.")
        return self

    def add_file(self, file_path):
        """ We add the file to the archive"""
        if os.path.exists(file_path):
            self.archive.write(file_path, os.path.basename(file_path))
            print(f"Додано файл '{file_path}' до архіву.")
        else:
            print(f"Файл '{file_path}' не знайдено і не був доданий до архіву.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ We close the archive after exiting the context"""
        if self.archive:
            self.archive.close()
            print(f"Архів '{self.archive_name}' закрито.")


with ZipArchiveManager('example_archive.zip') as zip_manager:
    zip_manager.add_file('file1.txt')
    zip_manager.add_file('file2.txt')
