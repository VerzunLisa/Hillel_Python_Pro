import threading
import requests


def download_file(url, filename):
    """Функція для завантаження файлу за вказаним URL."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Перевіряємо, чи запит був успішним
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Файл {filename} успішно завантажено.")
    except requests.RequestException as e:
        print(f"Помилка завантаження {filename}: {e}")


def download_files(urls, output_dir):
    """Завантаження кількох файлів одночасно за допомогою потоків."""
    threads = []
    for i, url in enumerate(urls):
        filename = f"{output_dir}/file_{i + 1}.bin"
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()  # Запускаємо потік

    for thread in threads:
        thread.join()  # Чекаємо завершення всіх потоків


if __name__ == "__main__":
    # Список URL для завантаження
    urls = [
        "https://www.karpaty.info/ua/uk/lv/st/volosyanka/houses/hirska.domivka/#gallery-4",
        "https://www.karpaty.info/ua/uk/lv/st/volosyanka/houses/hirska.domivka/#gallery-5",
        "https://www.karpaty.info/ua/uk/lv/st/volosyanka/houses/hirska.domivka/#gallery-9",
    ]

    output_dir = "downloads"  # Папка для збереження файлів

    # Завантажуємо файли
    download_files(urls, output_dir)
