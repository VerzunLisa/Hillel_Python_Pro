import asyncio


async def producer(queue: asyncio.Queue):
    """Функція для додавання завдань у чергу."""
    for i in range(4):
        await asyncio.sleep(1)
        task = f"Завдання {i + 1}"
        await queue.put(task)
        print(f"Producer: додано {task} до черги")
    print("Producer: всі завдання додано.")


async def consumer(queue: asyncio.Queue, consumer_id: int):
    """Функція для обробки завдань з черги."""
    while True:
        task = await queue.get()
        if task is None:
            print(f"Consumer {consumer_id}: завершення роботи.")
            queue.task_done()
            break

        print(f"Consumer {consumer_id}: почав виконувати {task}")
        await asyncio.sleep(2)
        print(f"Consumer {consumer_id}: завершив виконання {task}")
        queue.task_done()


async def main():
    """Основна функція для запуску producer та consumer."""
    queue = asyncio.Queue()
    num_consumers = 3
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(1, num_consumers + 1)]
    producer_task = asyncio.create_task(producer(queue))
    await producer_task
    for _ in range(num_consumers):
        await queue.put(None)
    await asyncio.gather(*consumers)
    print("Всі завдання оброблено.")

if __name__ == "__main__":
    asyncio.run(main())
