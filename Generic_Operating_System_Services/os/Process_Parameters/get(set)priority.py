"""os.getpriority(which, who)"""
# Получить приоритет планирования программы. Аргумент which является одним из
# os.PRIO_PROCESS, os.PRIO_PGRP или os.PRIO_USER и аргумент who интерпретируется
# относительно which. Нулевое значение для who обозначает (соответственно) вызывающий
# процесс, группу процессов вызывающего процесса или реальный идентификатор пользователя
# вызывающего процесса.
# Доступность: Unix, не Emscripten, не WASI.
#     Константа os.PRIO_PROCESS - идентификатор процесса,
#     Константа os.PRIO_PGRP - идентификатор группы процессов,
#     Константа os.PRIO_USER - идентификатор пользователя.
# Параметры для функций os.getpriority() и os.setpriority().
# print("os.getpriority(which, who):", os.getpriority(which, who))

"""os.setpriority(which, who, priority)"""
# Функции os.setpriority() устанавливает приоритет планирования программы priority.
# Аргумент which является одним из os.PRIO_PROCESS, os.PRIO_PGRP или os.PRIO_USER и who
# интерпретируется относительно which. Нулевое значение для who обозначает
# (соответственно) вызывающий процесс, группу процессов вызывающего процесса или
# реальный идентификатор пользователя вызывающего процесса. Приоритет priority -
# значение в диапазоне от -20 до 19. Приоритет по умолчанию - 0, более низкие приоритеты
# вызывают более благоприятное планирование.

import errno
import os
import unittest
from unittest import TestCase

base = os.getpriority(os.PRIO_PROCESS, os.getpid())
print("priority:", base)

pid = os.getpid()
os.setpriority(os.PRIO_PROCESS, pid, 10)
base = os.getpriority(os.PRIO_PROCESS, os.getpid())
print("\npriority:", base)

def test_set_get_priority(self):
    base = os.getpriority(os.PRIO_PROCESS, os.getpid())
    os.setpriority(os.PRIO_PROCESS, os.getpid(), base + 1)
    try:
        new_prio = os.getpriority(os.PRIO_PROCESS, os.getpid())
        if base >= 19 and new_prio <= 19:
            raise unittest.SkipTest(
                "unable to reliably test setpriority at current nice level of %s" % base)
        # невозможно надежно протестировать setpriority на текущем приятном уровне 0
        else:
            self.assertEqual(new_prio, base + 1)
    finally:
        try:
            os.setpriority(os.PRIO_PROCESS, os.getpid(), base)
        except OSError as err:
            if err.errno != errno.EACCES:
                raise


test_set_get_priority(TestCase())

"""class TestCase(object)"""
# Класс, экземпляры которого являются одиночными тестовыми примерами.
# По умолчанию сам тестовый код должен быть помещен в метод с именем
#      'выполнить тест'.
# Если прибор можно использовать для многих тестовых случаев, создайте его как
# многие методы испытаний по мере необходимости. При создании такого TestCase
# подкласс, укажите в аргументах конструктора имя тестового метода что экземпляр должен
# выполняться.
# Авторы тестов должны создавать подклассы TestCase для своих собственных тестов.
# Строительство и деконструкция тестовой среды («фикстура») может быть реализуется
# путем переопределения методов setUp и tearDown соответственно.
# Если необходимо переопределить метод __init__, Метод __init__ базового класса должен
# вызываться всегда. Важно, чтобы подклассы не должны менять сигнатуру своего
# метода __init__, поскольку экземпляры экземпляры классов создаются автоматически
# частями фреймворка для того, чтобы быть запущенным.
# При создании подкласса TestCase вы можете установить следующие атрибуты:
#      * failureException: определяет, какое исключение будет вызвано, когда
#          методы утверждения экземпляра терпят неудачу; тестовые методы повышения этого
#          исключение будет считаться «неудачным», а не «ошибочным».
#      * longMessage: определяет, будут ли длинные сообщения (включая
#          объекты, используемые в методах assert), будут напечатаны при ошибке в
#          *дополнительно* на любое переданное явное сообщение.
#      * maxDiff: устанавливает максимальную длину различий в сообщениях об ошибках.
#          методами assert с использованием difflib. Он рассматривается как экземпляр
#          атрибут, поэтому при необходимости его можно настроить с помощью отдельных
#          тестов.
