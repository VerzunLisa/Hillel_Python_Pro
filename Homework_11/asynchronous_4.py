import asyncio


async def slow_task():
    """Імітація повільного завдання, яке виконується 10 секунд."""
    print("slow_task: Завдання починається...")
    await asyncio.sleep(10)
    print("slow_task: Завдання завершено.")


async def main():
    """Основна функція для запуску slow_task із таймаутом."""
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("main: Час очікування завершився. Завдання не виконане вчасно.")

if __name__ == "__main__":
    asyncio.run(main())
