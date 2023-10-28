"""
Task Groups (Группы задач)

Группы задач сочетают в себе API создания задач с удобным и надежным способом ожидания
завершения всех задач в группе.

class asyncio.TaskGroup
     Асинхронный контекстный менеджер, содержащий группу задач. Задачи можно добавить в
     группу с помощью create_task(). Все задачи ожидаются после выхода из контекстного
     менеджера.

     Новое в версии 3.11.

     create_task(coro, *, name=None, context=None)

         Создайте задачу в этой группе задач. Подпись соответствует подписи asyncio.create_task().
Пример: """
import asyncio


async def some_coro(value):
    print(f'>task {value} executing')
    # приостановка работы на некоторое время
    await asyncio.sleep(1)
    return value**2


async def another_coro(value):
    # приостановка работы на некоторое время
    await asyncio.sleep(3)
    print(f'>task {value} executing')
    return value**2


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(1))
        task2 = tg.create_task(another_coro(2))
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")

asyncio.run(main())
"""
Оператор async with будет ждать завершения всех задач в группе. Во время ожидания в группу
все еще можно добавлять новые задачи (например, передав tg в одну из сопрограмм и вызвав
tg.create_task() в этой сопрограмме). После завершения последней задачи и выхода из блока
async with новые задачи не могут быть добавлены в группу.

При первом сбое какой-либо задачи, принадлежащей группе, за исключением 
asyncio.CancelledError, остальные задачи в группе отменяются. После этого в группу 
невозможно будет добавить никакие дальнейшие задачи. На этом этапе, если тело оператора 
async with все еще активно (т. е. __aexit__() еще не была вызвана), задача, непосредственно 
содержащая оператор async with, также отменяется. Полученный результат asyncio.CancelledError
прервет ожидание, но не выйдет за пределы содержащегося оператора async with.

Если после завершения всех задач какие-либо задачи завершились сбоем с исключением, 
отличным от asyncio.CancelledError, эти исключения объединяются в ExceptionGroup или 
BaseExceptionGroup (в зависимости от ситуации; см. их документацию), которая затем 
вызывается.

Два базовых исключения обрабатываются особым образом: если какая-либо задача завершается с ошибкой KeyboardInterrupt или SystemExit, группа задач по-прежнему отменяет оставшиеся задачи и ожидает их, но затем повторно вызывается первоначальный KeyboardInterrupt или SystemExit вместо ExceptionGroup или BaseExceptionGroup.

Если тело оператора async with завершается с исключением (поэтому __aexit__() вызывается 
с набором исключений), это обрабатывается так же, как если бы одна из задач завершилась 
неудачно: оставшиеся задачи отменяются, а затем ожидаются, и не -Исключения отмены 
группируются в группу исключений и вызываются. Исключение, переданное в __aexit__(), если
оно не является asyncio.CancelledError, также включается в группу исключений. Для 
KeyboardInterrupt и SystemExit предусмотрен тот же особый случай, что и в предыдущем абзаце.
"""