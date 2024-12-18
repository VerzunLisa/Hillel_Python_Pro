import aiohttp
import asyncio


async def fetch_content(url: str) -> str:
    """Виконує HTTP-запит і повертає вміст сторінки або повідомлення про помилку."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    print(f"Успішно завантажено: {url}")
                    return await response.text()
                else:
                    print(f"Помилка {response.status} при завантаженні: {url}")
                    return f"Помилка {response.status}: {url}"
    except asyncio.TimeoutError:
        print(f"Таймаут при завантаженні: {url}")
        return f"Таймаут: {url}"
    except aiohttp.ClientError as e:
        print(f"Помилка підключення: {url} - {e}")
        return f"Помилка підключення: {url} - {e}"
    except Exception as e:
        print(f"Невідома помилка: {url} - {e}")
        return f"Невідома помилка: {url} - {e}"


async def fetch_all(urls: list):
    """Запускає завантаження всіх URL паралельно."""
    tasks = [fetch_content(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    # Список URL для завантаження
    urls = [
        "https://example.com",
        "https://httpbin.org/delay/2",  # Затримка у 2 секунди
        "https://httpbin.org/status/404",  # Помилка 404
        "https://httpbin.org/status/500",  # Помилка 500
        "https://invalid-url-test123.com"  # Некоректний URL
    ]

    print("Початок завантаження сторінок...\n")
    results = asyncio.run(fetch_all(urls))
    print("\nРезультати завантаження:")
    for i, result in enumerate(results):
        print(f"URL {i + 1}: {result[:100]}...")  # Виводимо перші 100 символів вмісту або повідомлення
