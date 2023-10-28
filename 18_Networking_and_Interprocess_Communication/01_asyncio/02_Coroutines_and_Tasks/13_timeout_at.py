"""
asyncio.timeout_at(when)
Аналогично asyncio.timeout(), за исключением случаев, когда указано абсолютное время
прекращения ожидания или нет.

Пример: """
import asyncio
from asyncio import get_running_loop


async def long_running_task(x):
    return x ** 3


async def main():
    loop = get_running_loop()
    deadline = loop.time() + 20
    try:
        # We do not know the timeout when starting, so we pass ``None``.
        # Мы не знаем таймаут при запуске, поэтому передаем None.
        async with asyncio.timeout_at(deadline):
            result = await long_running_task(5)
            print(result)
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")
        # Время длительной операции истекло, но мы справились

    print("This statement will run regardless.")
    # Этот оператор будет выполнен в любом случае

asyncio.run(main())

"""New in version 3.11."""
