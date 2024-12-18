from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import os


def process_image(input_path, output_path, size):
    """Функція для обробки одного зображення (зміна розміру)."""
    try:
        with Image.open(input_path) as img:
            img = img.resize(size)  # Змінюємо розмір
            img.save(output_path)  # Зберігаємо оброблене зображення
        print(f"Оброблено: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Помилка обробки {input_path}: {e}")


def process_images_concurrently(input_dir, output_dir, size, max_workers=4):
    """Паралельна обробка всіх зображень у каталозі."""
    # Створюємо каталог для збереження результатів
    os.makedirs(output_dir, exist_ok=True)

    # Отримуємо список усіх зображень у вхідному каталозі
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    # Використовуємо ThreadPoolExecutor для паралельної обробки
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for image_file in image_files:
            input_path = os.path.join(input_dir, image_file)
            output_path = os.path.join(output_dir, image_file)
            # Додаємо завдання до пулу
            futures.append(executor.submit(process_image, input_path, output_path, size))

        # Очікуємо завершення всіх завдань
        for future in futures:
            future.result()


if __name__ == "__main__":
    # Вхідний та вихідний каталоги
    input_dir = "input_images"
    output_dir = "output_images"

    # Розмір, до якого потрібно змінити зображення (ширина, висота)
    target_size = (200, 200)

    # Запуск обробки зображень
    process_images_concurrently(input_dir, output_dir, target_size)
