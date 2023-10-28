"""
class asyncio.Timeout(when)
Асинхронный контекстный менеджер для отмены просроченных сопрограмм.

When должно быть абсолютным временем, в которое контекст должен истечь, измеренный часами
цикла событий:

    If when is None, тайм-аут никогда не сработает.
    If when < loop.time(), тайм-аут сработает на следующей итерации цикла событий.

    when() → float | None
    Верните текущий крайний срок или None, если текущий крайний срок не установлен.

    reschedule(when: float | None) (перенести расписание)
    Перепланируйте тайм-аут.

    expired() → bool (истек)
    Возвращает информацию о том, превысил ли менеджер контекста свой крайний срок (истек).

Пример: """

import asyncio
from asyncio import get_running_loop


async def long_running_task(x):
    return x ** 3


async def main():
    try:
        # We do not know the timeout when starting, so we pass ``None``.
        # Мы не знаем таймаут при запуске, поэтому передаем None.
        async with asyncio.timeout(None) as cm:
            # We know the timeout now, so we reschedule it.
            # Теперь мы знаем тайм-аут, поэтому переносим его.
            new_deadline = get_running_loop().time() + 10
            cm.reschedule(new_deadline)

            result = await long_running_task(5)
            print(result)
    except TimeoutError:
        pass

    if cm.expired():
        print("Looks like we haven't finished on time.")

asyncio.run(main())

"""
Менеджеры контекста таймаута могут быть безопасно вложены.

Новое в версии 3.11."""