from aiohttp import web
import asyncio


async def handle_root(request):
    """Обробник для маршруту '/'"""
    return web.Response(text="Hello, World!")


async def handle_slow(request):
    """Обробник для маршруту '/slow' з імітацією довгої операції."""
    await asyncio.sleep(5)  # Симуляція затримки на 5 секунд
    return web.Response(text="Operation completed")


def main():
    app = web.Application()

    app.router.add_get("/", handle_root)
    app.router.add_get("/slow", handle_slow)

    print("Запуск веб-сервера на http://localhost:8080")
    web.run_app(app, host="localhost", port=8080)


if __name__ == "__main__":
    main()
