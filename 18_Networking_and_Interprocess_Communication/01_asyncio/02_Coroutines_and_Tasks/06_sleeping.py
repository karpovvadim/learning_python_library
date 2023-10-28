"""
Sleeping (Спать)

coroutine asyncio.sleep(delay, result=None)
сопрограмма asyncio.sleep(задержка, результат = нет)

     Блокировка на секунды задержки.
     Если результат предоставлен, он возвращается вызывающей стороне после завершения
     сопрограммы.
     Sleep() всегда приостанавливает текущую задачу, позволяя запустить другие задачи.
     Установка задержки на 0 обеспечивает оптимизированный путь для запуска других задач.
     Это может использоваться долго выполняющимися функциями, чтобы избежать блокировки
     цикла событий на весь период вызова функции.

     Пример сопрограммы, отображающей текущую дату каждую секунду в течение 5 секунд: """

import asyncio
import datetime


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


# asyncio.run(display_date())

"""Изменено в версии 3.10: Убран параметр цикла."""


async def fff(tt):
    await asyncio.sleep(tt)


async def display():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 10.0
    while True:
        print(datetime.datetime.now())
        if loop.time() >= end_time:
            break

        tt = 3
        await fff(tt)


asyncio.run(display())