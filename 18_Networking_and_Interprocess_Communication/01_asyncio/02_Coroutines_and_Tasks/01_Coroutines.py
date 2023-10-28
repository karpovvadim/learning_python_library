"""
Сопрограммы или coroutines, объявленные с синтаксисом async/await, являются
предпочтительным способом написания приложений, с использованием модуля asyncio.


Функция asyncio.run() для запуска функции main() точки входа верхнего уровня.

Например, следующий фрагмент кода (требуется Python 3.7+) печатает "hello", ждет 1 секунду,
а затем печатает "world":
"""
import asyncio
import time


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world\n')


# запуск основного цикла событий
asyncio.run(main())

"""
Обратите внимание, что простой вызов сопрограммы main() не приведет к ее выполнению:

>>> main()
# <coroutine object main at 0x1053bb7c8>


Ожидание сопрограммы.
Запуск сопрограмм, которые должны или могут ждать каких-то результатов (например, ответа
сервера с результатами запроса) запускаются оператором await.

Следующий фрагмент кода выведет «hello» после ожидания в течение 
1 секунды, а затем выведет «world» после ожидания еще в течение 2 секунд:
"""


async def say_after(delay, what):
    """Асинхронная функция (сопрограмма)"""
    await asyncio.sleep(delay)
    print("what:", what)


async def main2():
    """Точка входа в асинхронную программу"""
    print(f"started at {time.strftime('%X')}")

    # запуск сопрограммы `say_after()` происходит при
    # помощи оператора `await`, т. к. в самой сопрограмме
    # есть объект ожидания - неблокирующая функция
    # `asyncio.sleep()`, которая эмитирует ожидание ответа сервера
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}\n")


# запуск основного цикла событий

asyncio.run(main2())
"""started at 12:23:15
   hello
   world
   finished at 12:23:18"""

"""
запуск сопрограмм можно осуществлять через создание и планирование задач при помощи 
функции asyncio.create_task(). Объекты задач Task также являются объектами ожидания 
результата, т.к. планируют запуск сопрограмм в будущем, как только это станет возможным.
Следовательно, задачи, то же запускаем оператором await

Изменим предыдущий пример и одновременно запустим две сопрограммы say_after():
"""


# async def say_after(delay, what):
#     """Асинхронная функция (сопрограмма)"""
#     await asyncio.sleep(delay)
#     print(what)

async def main3():
    """Точка входа в асинхронную программу"""

    # создаем задачи `task1` и `task2`
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Ждем, пока обе задачи будут выполнены
    # (должно занять около 4 секунд.)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}\n")


asyncio.run(main3())
"""
Обратите внимание, что фрагмент кода выполняется на 1 секунду быстрее, чем раньше.


Класс asyncio.TaskGroup() (добавлен в Python 3.11) представляет собой более современную
альтернативу asyncio.create_task(). Используя этот API, последний пример становится 
таким:
"""
async def main4():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(2, 'hello'))

        task2 = tg.create_task(
            say_after(4, 'world'))

        print(f"started at {time.strftime('%X')}")
    # Ожидание является неявным при выходе из контекстного менеджера.
    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main4())

# Время и вывод должны быть такими же, как и для предыдущей версии.
