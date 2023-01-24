"""os.sysconf(name)"""
# Возвращает целочисленные значения конфигурации системы. Если значение конфигурации,
# указанное в name, не определено, возвращается -1. Комментарии относительно параметра
# name для confstr() применимы и здесь; словарь, который предоставляет информацию об
# известных именах, представлен sysconf_names.
#     Доступность: Unix.

"""os.sysconf_names"""
# Имена сопоставления словаря, принятые sysconf(), с целочисленными значениями,
# определенными для этих имён операционной системой хоста. Это можно использовать для
# определения набора имён, известных системе.
#    Доступность: Unix.

import os
# System Configuration variable (Переменная конфигурации системы)
name = "SC_PAGE_SIZE"

# Получите целочисленное значение конфигурации, соответствующее указанной переменной
# конфигурации, используя метод os.sysconf().
value = os.sysconf(name)
print("% s :" % name, value)

name1 = "SC_INT_MIN"
name2 = "SC_INT_MAX"

value1 = os.sysconf(name1)
value2 = os.sysconf(name2)

print("% s :" % name1, value1)
print("% s :" % name2, value2)

# Мы также можем передать целочисленное значение для параметра имени.
# Целочисленное значение должно присутствовать в словаре os.sysconf_names как значение
# любой переменной конфигурации, например
conf_var = "SC_INT_MIN"
name = os.sysconf_names[conf_var]
print("\nInteger value corresponding to % s:" % conf_var, name)
# Целочисленное значение, соответствующее conf_var и name метода os.sysconf_names

value = os.sysconf(name)
print("Configuration value corresponding to % s :" % name, value)

# Примечание: -1 возвращается, если переменная конфигурации не определена системой.

print("\nИмена, известные операционной системе, принятые sysconf(), \
с целочисленными значениями")
for item in os.sysconf_names.items():
    print(item)
