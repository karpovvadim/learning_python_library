"""
Awaitables - Ожидаемые события

Мы говорим, что объект является ожидаемым, если его можно использовать в выражении await.
Многие API-интерфейсы asyncio предназначены для приема ожидаемых данных.

Существует три основных типа ожидаемых объектов: coroutines, Tasks, and Futures
(сопрограммы, задачи и фьючерсы).

Сопрограммы

Сопрограммы Python являются ожидаемыми, поэтому их можно ожидать от других сопрограмм:
"""
import asyncio


async def nested():  # nested - вложенный
    return 42


async def main():
    # Ничего не происходит, если мы просто вызываем "nested()".
    # Сопрограмма `nested()` создается, но не будет выполняться,
    # т.к. в таком виде она заблокирует цикл событий, что недопустимо
    # nested()

    # что бы асинхронная функция `nested()` заработала
    # необходимо заставить ее ждать своего выполнения
    # при помощи оператора `await`
    print(await nested(), "\n")  # will print "42".


asyncio.run(main())
"""
Важно. Здесь термин "сопрограмма" может использоваться для двух тесно связанных понятий:

    функция сопрограммы: функция, определенная как *async def*;
    объект сопрограммы: объект, возвращаемый вызовом функции сопрограммы.

Примечание:

Модуль asyncio также поддерживает устаревшие сопрограммы на основе генератора. Поддержка
сопрограмм на основе генераторов запланирована к удалению в Python 3.10.

Задания Task.

Задачи (asyncio.Task) используются для одновременного планирования запуска нескольких
сопрограмм. Когда сопрограмма оборачивается в задачу (передается в функцию 
asyncio.create_task()), то сопрограмма будет автоматически запускаться в ближайшее время,
как только будет это возможным:
"""


async def main2():
    # Запланируйте nested() (вложенный) для одновременного запуска в ближайшее время
    # с помощью 'main2()'.
    task = asyncio.create_task(nested())  # Ожидающая задача name='Task-2'
    print("\nОжидающая задача выполняется =", task, "\n")  # coro=nested() (вложенная) выполняется на (путь)
    # «task» теперь можно использовать для отмены «nested()» или
    # можно просто дождаться завершения:
    final_task = await task  # Задача завершена name='Task-2' coro=nested() выполнено,
    print("выполнено =", task, "\n")  # определено в (путь), result=42
    print(final_task)  # 42


asyncio.run(main2())

"""
Futures - Фьючерсы

Future — это специальный низкоуровневый ожидаемый объект, который представляет конечный
результат асинхронной операции.

Когда ожидается объект Future, это означает, что сопрограмма будет ждать, пока Future 
не будет разрешена в каком-то другом месте.

Будущие объекты в asyncio необходимы, чтобы разрешить использование кода обратного 
вызова с async/await.

Обычно нет необходимости создавать объекты Future на уровне кода приложения.

Будущие объекты, иногда предоставляемые библиотеками и некоторыми API-интерфейсами 
asyncio, можно ожидать:
"""


async def main3():
    await 'function_that_returns_a_future_object()'  # функция, которая возвращает будущий объект()

    # this is also valid (это также верно):
    await asyncio.gather(  # ожидайте асинхронного сбора
        'function_that_returns_a_future_object()',
        'some_python_coroutine()'  # какая-то сопрограмма Python()
    )


# asyncio.run(main3())
"""
Хорошим примером низкоуровневой функции, возвращающей объект Future, является
loop.run_in_executor().
"""
