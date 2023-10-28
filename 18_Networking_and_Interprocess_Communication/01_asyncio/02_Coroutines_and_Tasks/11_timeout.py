"""
asyncio.timeout(delay)
Возвращает асинхронный менеджер контекста, который можно использовать для ограничения времени
ожидания чего-либо.
задержка может быть либо None, либо числом с плавающей запятой или целым числом секунд
ожидания. Если задержка равна «Нет», ограничение по времени применяться не будет; это
может быть полезно, если задержка неизвестна при создании диспетчера контекста.
В любом случае диспетчер контекста можно перепланировать после создания с помощью
Timeout.reschedule().

Пример: """
import asyncio


async def long_running_task(x):
    return x**3


async def main():
    async with asyncio.timeout(10):
        result = await long_running_task(5)
        print(result)

asyncio.run(main())

"""
Если выполнение long_running_task занимает более 10 секунд, диспетчер контекста отменит 
текущую задачу и обработает полученный результат asyncio.CancelledError внутри себя, 
преобразуя его в TimeoutError, который можно перехватить и обработать.

Примечание: Контекстный менеджер asyncio.timeout() преобразует asyncio.CancelledError в 
TimeoutError, что означает, что TimeoutError можно обнаружить только вне контекстного 
менеджера.

Пример перехвата ошибки тайм-аута:
"""


async def main1():
    try:
        async with asyncio.timeout(10):
            result = await long_running_task(5)
            print(result)
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")
        # Время длительной операции истекло, но мы справились

    print("This statement will run regardless.")
    # Этот оператор будет выполняться независимо

# asyncio.run(main1())

"""
Менеджер контекста, созданный с помощью asyncio.timeout(), может быть перенесен на 
другой крайний срок и проверен."""
