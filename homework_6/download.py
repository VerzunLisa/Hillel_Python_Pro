import requests


def download_page(url, filename="page_content.txt"):
    try:
        # Надсилаємо запит GET до вказаного URL
        response = requests.get(url)

        # Перевіряємо статус відповіді
        response.raise_for_status()

        # Записуємо вміст сторінки у текстовий файл
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Сторінка успішно збережена у файл '{filename}'")

    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")


# Приклад використання
url = "https://www.example.com"  # Введіть потрібний URL
download_page(url)
