"""
Running an asyncio Program - Запуск программы asyncio

asyncio.run(coro, *, debug=None, loop_factory=None) - (отладка=нет, фабрика_цикла=нет)

    Выполните сопрограмму coro и верните результат.

    Эта функция запускает переданную сопрограмму, беря на себя управление циклом
событий asyncio, завершая работу асинхронных генераторов и закрывая пул потоков.

    Эту функцию нельзя вызвать, когда в том же потоке выполняется другой цикл событий
asyncio.

    Если параметр debug имеет значение True, цикл событий будет выполняться в режиме
отладки. Значение False явно отключает режим отладки. None используется для соблюдения
глобальных настроек режима отладки.

    Эта функция всегда создает новый цикл событий и закрывает его в конце. Его,
цикл событий, следует использовать в качестве основной точки входа для
асинхронных программ, и в идеале его следует вызывать только один раз.

Пример:
"""

import asyncio

async def main():
    await asyncio.sleep(3)
    print('hello')


asyncio.run(main())
"""
Новое в версии 3.7.
Изменено в версии 3.9: обновлено использование цикла.shutdown_default_executor().
Изменено в версии 3.10: по умолчанию для отладки установлено значение «Нет», что 
соответствует глобальным настройкам режима отладки.
Изменено в версии 3.12: Добавлен параметр loop_factory.
"""
import datetime
import random


# async def my_sleep_func():
#     await asyncio.sleep(random.randint(0, 5))
#
#
# async def display_date(num, loop_):
#     end_time = loop_.time() + 50.0
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop_.time() + 1.0) >= end_time:
#             break
#         await my_sleep_func()
#
#
# loop = asyncio.get_event_loop()
#
# asyncio.ensure_future(display_date(1, loop))
# asyncio.ensure_future(display_date(2, loop))
#
# loop.run_forever()
