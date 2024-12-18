import asyncio
import random


async def download_page(url: str):
    """Симулює завантаження сторінки за випадковий проміжок часу."""
    load_time = random.randint(1, 5)  # Випадковий час завантаження від 1 до 5 секунд
    print(f"Початок завантаження: {url} (очікуваний час: {load_time} с)")
    await asyncio.sleep(load_time)  # Симуляція затримки завантаження
    print(f"Завершено завантаження: {url} за {load_time} секунд")


async def main(urls: list):
    """Запускає завантаження сторінок одночасно."""
    tasks = [download_page(url) for url in urls]  # Створення списку завдань
    await asyncio.gather(*tasks)  # Одночасне виконання всіх завдань

if __name__ == "__main__":
    # Список URL для симуляції
    urls = [
        "https://www.lingoda.com/blog/ru/yazyki-kotorye-legko-vyuchit/",
        "https://www.liveworksheets.com/worksheets",
        "https://khashtamov.com/ru/pandas-introduction/",
        "https://www.nippon-gatari.info/2015/06/spisok-grammatiki-dlya-sdachi-urovnya-n4-jlpt.html"
    ]

    print("Початок завантаження сторінок...\n")
    asyncio.run(main(urls))
    print("\nЗавершено завантаження всіх сторінок.")
