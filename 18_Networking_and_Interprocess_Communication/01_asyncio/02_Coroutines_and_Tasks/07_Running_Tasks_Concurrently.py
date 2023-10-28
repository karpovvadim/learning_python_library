"""
Running Tasks Concurrently (Параллельное выполнение задач)

awaitable asyncio.gather(*aws, return_exceptions=False)

     Запускайте ожидаемые объекты в последовательности aws одновременно.

     Если какое-либо ожидаемое событие в aws является сопрограммой, оно автоматически
     назначается как задача.
     Если все ожидаемые объекты выполнены успешно, результатом является совокупный список
     возвращаемых значений. Порядок значений результатов соответствует порядку ожидаемых
     значений в aws.
     Если return_Exceptions имеет значение False (по умолчанию), первое возникшее
     исключение немедленно распространяется на задачу, ожидающую метода сбора(). Другие
     awaitables в последовательности aws не будут отменены и продолжат выполняться.
     Если return_Exceptions имеет значение True, исключения обрабатываются так же, как
     успешные результаты, и объединяются в список результатов.
     Если метод сбора() отменяется, все отправленные ожидаемые объекты (которые еще не з
     авершены) также отменяются.
     Если какая-либо задача или будущее из последовательности aws отменяется, это
     рассматривается так, как если бы она вызвала CancelledError — вызов метода сбора() в
     этом случае не отменяется. Это сделано для того, чтобы предотвратить отмену одной
     отправленной задачи/фьючерса, которая может привести к отмене других задач/фьючерсов.

     Примечание: Новой альтернативой для одновременного создания и запуска задач и ожидания
     их завершения является asyncio.TaskGroup. TaskGroup обеспечивает более сильные гарантии
     безопасности, чем сбор для планирования вложенных подзадач: если задача (или подзадача,
     задача, запланированная задачей) вызывает исключение, TaskGroup, а сбор не отменит
     оставшиеся запланированные задачи).

     Пример: """

import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule five calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
        factorial("D", 5),
        factorial("E", 6),
    )
    print(L)

asyncio.run(main())

"""
Примечание: Если return_Exceptions имеет значение False, отмена метода gather() (сбора) 
после того, как он был помечен как выполненный, не отменит отправленные ожидаемые объекты. 
Например, сбор может быть помечен как выполненный после распространения исключения 
вызывающему объекту, поэтому вызов метода gather.cancel() (сбора.отмена) после перехвата 
исключения (вызванного одним из ожидаемых объектов) из сбора не приведет к отмене других 
ожидаемых объектов.

Изменено в версии 3.7: Если сама сборка отменена, отмена распространяется независимо от 
return_Exceptions.

Изменено в версии 3.10: Убран параметр loop (цикл).

Устарело с версии 3.10: предупреждение об устаревании выдается, если не указаны 
позиционные аргументы или не все позиционные аргументы являются объектами типа Future и 
нет текущего цикла событий.
"""