Coroutines and Tasks - Сопрограммы и задачи 

В этом разделе описываются высокоуровневые API-интерфейсы asyncio для работы с 
сопрограммами и задачами.

        Coroutines                                      Сопрограммы
async def function():

        Awaitables                                      Ожидаемые события
await, asyncio.create_task(), Futures - Фьючерсы

        Creating Tasks                                  Создание задач
asyncio.create_task(coro, *, name=None, context=None)

        Task Cancellation                               Отмена задачи
asyncio.CancelledError

        Task Groups                                     Группы задач
class asyncio.TaskGroup

        Sleeping                                        Спать
coroutine asyncio.sleep(delay, result=None)

        Running Tasks Concurrently                      Одновременное выполнение задач
awaitable asyncio.gather(*aws, return_exceptions=False)

        Eager Task Factory                              Фабрика нетерпеливых задач
asyncio.eager_task_factory(loop, coro, *, name=None, context=None)
asyncio.create_eager_task_factory(custom_task_constructor)

        Shielding From Cancellation                     Защита от отмены
awaitable asyncio.shield(aw)

        Timeouts                                        Таймауты
asyncio.timeout(delay)
class asyncio.Timeout(when)
asyncio.timeout_at(when)
coroutine asyncio.wait_for(aw, timeout)

        Waiting Primitives                              Ожидающие примитивы
coroutine asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)
asyncio.as_completed(aws, *, timeout=None)

        Running in Threads                              Работа в потоках
coroutine asyncio.to_thread(func, /, *args, **kwargs)

        Scheduling From Other Threads                   Планирование из других потоков
asyncio.run_coroutine_threadsafe(coro, loop)

        Introspection                                   Самоанализ

asyncio.current_task(loop=None)

Возвращает текущий запущенный экземпляр задачи или None, если ни одна задача не выполняется.
Если цикл равен None, get_running_loop() используется для получения текущего цикла.
Новое в версии 3.7.

asyncio.all_tasks(loop=None)

Возвращает набор еще не завершенных объектов Task, выполняемых циклом.
Если цикл имеет значение None, get_running_loop() используется для получения текущего цикла.
New in version 3.7.

asyncio.iscoroutine(obj)
Возвращайте True, если obj является объектом сопрограммы.
Новое в версии 3.4.

        Task Object                                     Объект задачи
class asyncio.Task(coro, *, loop=None, name=None, context=None, eager_start=False)