"""
coroutine asyncio.wait_for(aw, timeout)
Подождите, пока aw awaitable завершится с тайм-аутом.

Если aw является сопрограммой, она автоматически назначается как Задача.

timeout может быть либо None, либо числом с плавающей запятой или целым числом секунд
ожидания. Если тайм-аут равен None, блокируется до завершения будущего.

Если происходит тайм-аут, задача отменяется и выдается TimeoutError.

Чтобы избежать отмены задачи, оберните ее в Shield().

Функция будет ждать, пока будущее не будет фактически отменено, поэтому общее время
ожидания может превысить таймаут. Если во время отмены возникает исключение, оно
распространяется.

Если ожидание отменяется, будущее aw также отменяется.

Изменено в версии 3.10: Убран параметр цикла.

Пример: """
import asyncio


async def eternity():  # вечность
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')


async def main():
    # Wait for at most 1 second (Подождите не более 1 секунды.)
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except TimeoutError:
        print('timeout!')

asyncio.run(main())
