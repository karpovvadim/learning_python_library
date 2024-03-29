"""
asyncio.create_eager_task_factory(custom_task_constructor)
создать фабрику активных задач (конструктор пользовательских задач)

Создайте фабрику нетерпеливых задач, аналогичную eager_task_factory(), используя
предоставленный custom_task_constructor при создании новой задачи вместо задачи по
умолчанию.

custom_task_constructor должен быть вызываемым объектом с сигнатурой, соответствующей
сигнатуре Task.__init__. Вызываемый объект должен возвращать объект, совместимый с
asyncio.Task.

Эта функция возвращает вызываемый объект, предназначенный для использования в качестве
фабрики задач цикла событий через loop.set_task_factory(factory)).

     Новое в версии 3.12.

"""