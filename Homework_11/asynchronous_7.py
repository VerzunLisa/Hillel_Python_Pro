import time
import requests
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# URL для тестування
URL = "https://www.liveworksheets.com/worksheets#google_vignette"
NUM_REQUESTS = 10


# ------------------------ ФУНКЦІЯ ДЛЯ ЗАПИТІВ ------------------------
def fetch():
    """Отримати вміст сторінки."""
    response = requests.get(URL)
    response.text


# ------------------------ СИНХРОННИЙ РЕЖИМ ------------------------
def sync_requests():
    """Синхронне виконання запитів."""
    for _ in range(NUM_REQUESTS):
        fetch()


# ------------------------ БАГАТОПОТОКОВИЙ РЕЖИМ ------------------------
def thread_requests():
    """Багатопотокове виконання запитів."""
    with ThreadPoolExecutor(max_workers=50) as executor:  # 50 потоків
        futures = [executor.submit(fetch) for _ in range(NUM_REQUESTS)]
        for future in futures:
            future.result()


# ------------------------ БАГАТОПРОЦЕСОРНИЙ РЕЖИМ ------------------------
def process_requests():
    """Багатопроцесорне виконання запитів."""
    with ProcessPoolExecutor(max_workers=8) as executor:  # 8 процесів
        futures = [executor.submit(fetch) for _ in range(NUM_REQUESTS)]
        for future in futures:
            future.result()


# ------------------------ АСИНХРОННИЙ РЕЖИМ ------------------------
async def async_requests():
    """Асинхронне виконання запитів."""
    async def fetch_async(session):
        async with session.get(URL) as response:
            await response.text()  # Читаємо відповідь

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session) for _ in range(NUM_REQUESTS)]
        await asyncio.gather(*tasks)


# ------------------------ ЗАМІР ЧАСУ ------------------------
def measure_time(func, *args):
    """Вимірює час виконання функції."""
    start = time.time()
    func(*args)
    end = time.time()
    print(f"{func.__name__} виконано за {end - start:.2f} секунд.")


def measure_async_time(coro):
    """Вимірює час виконання асинхронної корутини."""
    start = time.time()
    asyncio.run(coro())
    end = time.time()
    print(f"{coro.__name__} виконано за {end - start:.2f} секунд.")


# ------------------------ ГОЛОВНА ФУНКЦІЯ ------------------------
if __name__ == "__main__":
    print(f"Виконання {NUM_REQUESTS} HTTP-запитів на {URL}...\n")
    measure_time(sync_requests)
    measure_time(thread_requests)
    measure_time(process_requests)
    measure_async_time(async_requests)
