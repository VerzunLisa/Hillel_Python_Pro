import aiohttp
import asyncio
import os


async def download_image(session, url, filename):
    """
    Завантажує зображення з вказаного URL та зберігає його у файл.
    :param session: Сесія aiohttp для виконання HTTP-запитів
    :param url: URL зображення для завантаження
    :param filename: Ім'я файлу, куди зберегти зображення
    """
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                with open(filename, 'wb') as f:
                    f.write(content)
                print(f"Зображення завантажено: {filename}")
            else:
                print(f"Не вдалося завантажити {url}. Код: {response.status}")
    except Exception as e:
        print(f"Помилка при завантаженні {url}: {e}")


async def main(image_urls, output_dir):
    """
    Завантажує всі зображення за списком URL одночасно.
    :param image_urls: Список URL для завантаження
    :param output_dir: Каталог для збереження завантажених зображень
    """

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(image_urls):
            filename = os.path.join(output_dir, f"image_{i + 1}.jpg")
            tasks.append(download_image(session, url, filename))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    image_urls = [
        "https://www.karpaty.info/ua/uk/lv/st/volosyanka/houses/hirska.domivka/#gallery-4",
        "https://www.karpaty.info/ua/uk/lv/st/volosyanka/houses/hirska.domivka/#gallery-5",
        "https://www.karpaty.info/ua/uk/lv/st/volosyanka/houses/hirska.domivka/#gallery-9"
    ]

    output_dir = "downloaded_images"

    print("Початок завантаження зображень...")
    asyncio.run(main(image_urls, output_dir))
    print("Завершено!")
