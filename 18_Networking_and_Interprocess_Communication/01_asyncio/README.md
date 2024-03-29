asyncio — Asynchronous I/O (asyncio — Асинхронный ввод-вывод)

asyncio — это библиотека для написания параллельного кода с использованием
синтаксиса async/await.

asyncio используется в качестве основы для нескольких асинхронных фреймворков
Python, которые обеспечивают высокопроизводительные сетевые и веб-серверы,
библиотеки подключений к базам данных, распределенные очереди задач и т. д.

asyncio часто идеально подходит для высокоуровневого структурированного
сетевого кода, связанного с вводом-выводом.

asyncio предоставляет набор API-интерфейсов (интерфейс программирования 
приложения) высокого уровня для:

     одновременно запускать сопрограммы Python и иметь полный контроль над
     их выполнением;

     выполнять сетевой ввод-вывод и IPC (Inter Process Communications - 
     межпроцессное взаимодействие);

     управлять подпроцессами;

     распределять задачи по очередям;

     синхронизировать параллельный код;

Кроме того, существуют низкоуровневые API-интерфейсы для разработчиков
библиотек и платформ, позволяющие:

     создавать циклы событий и управлять ими, которые предоставляют 
     асинхронные API для работы в сети, запуска подпроцессов, обработки 
     сигналов ОС и т. д.;

     реализовать эффективные протоколы с использованием транспортов;

     мостовые библиотеки на основе обратных вызовов и код с синтаксисом async/await.

>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
# 'hello'

Наличие: не Emscripten, не WASI.

Этот модуль не работает или недоступен на платформах WebAssembly Wasm32-emscripten и
Wasm32-Wasi. Дополнительную информацию см. в разделе «Платформы WebAssembly».

Reference                           Ссылка

High-level APIs                     API высокого уровня

    Runners                         бегуны
    Coroutines and Tasks            Сопрограммы и задачи
    Streams                         Потоки
    Synchronization Primitives      Примитивы синхронизации
    Subprocesses                    Подпроцессы
    Queues                          Очереди
    Exceptions                      Исключения

Low-level APIs                      Низкоуровневые API

    Event Loop                      Цикл событий
    Futures                         Фьючерсы
    Transports and Protocols        Транспорты и протоколы
    Policies                        Политика
    Platform Support                Поддержка платформы
    Extending                       Расширение

Guides and Tutorials                Руководства и учебные пособия

    High-level API Index            Индекс API высокого уровня
    Low-level API Index             Индекс API низкого уровня
    Developing with asyncio         Разработка с помощью asyncio

Примечание

Исходный код asyncio можно найти в Lib/asyncio/.