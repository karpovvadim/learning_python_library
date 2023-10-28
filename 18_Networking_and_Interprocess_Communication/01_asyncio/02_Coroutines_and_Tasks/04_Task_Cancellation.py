import asyncio
from asyncio import CancelledError

var = asyncio.CancelledError

"""
Task Cancellation

Отмена задачи

Задачи можно легко и безопасно отменить. Когда задача отменяется, asyncio.CancelledError
будет вызван в задаче при следующей возможности.

Рекомендуется, чтобы сопрограммы использовали блоки try/finally для надежного выполнения
логики очистки. В случае явного обнаружения asyncio.CancelledError его обычно следует
распространять после завершения очистки. asyncio.CancelledError напрямую является
подклассом BaseException, поэтому большинству кода не нужно знать об этом.

Компоненты asyncio, обеспечивающие структурированный параллелизм, такие как
asyncio.TaskGroup и asyncio.timeout(), реализуются с использованием внутренней отмены и
могут работать неправильно, если сопрограмма проглотит asyncio.CancelledError.
Аналогично, пользовательский код обычно не должен вызывать команду uncancel 
(отменить отмену). Однако в случаях, когда подавление asyncio.CancelledError действительно
желательно, необходимо также вызвать uncancel(), чтобы полностью удалить состояние отмены.
"""


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    time_elapsed = 0
    while not task.done():
        time_elapsed += 1
        await asyncio.sleep(1)
        print('Task has not completed, checking again in a second')
        if time_elapsed == 3:
            print('Cancelling the task...')
            task.cancel()
            break

    try:
        await task
    except CancelledError:
        print('Task has been cancelled.')

asyncio.run(main())
