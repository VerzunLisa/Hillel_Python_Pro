import os
import csv
from PIL import Image


class ImageMetadataIterator:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.image_files):
            raise StopIteration

        image_file = self.image_files[self.index]
        self.index += 1

        image_path = os.path.join(self.folder_path, image_file)
        with Image.open(image_path) as img:
            metadata = {
                'filename': image_file,
                'format': img.format,
                'size': img.size,
                'mode': img.mode
            }

        return metadata


def save_metadata_to_csv(image_iterator, output_csv):
    # Створюємо та відкриваємо CSV файл для запису
    with open(output_csv, mode='w', newline='') as csv_file:
        fieldnames = ['filename', 'format', 'size', 'mode']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for metadata in image_iterator:
            writer.writerow(metadata)


folder_path = 'path_to_your_image_folder'
output_csv = 'image_metadata.csv'
image_iterator = ImageMetadataIterator(folder_path)
save_metadata_to_csv(image_iterator, output_csv)
print(f"Метадані зображень збережені у файл {output_csv}")
