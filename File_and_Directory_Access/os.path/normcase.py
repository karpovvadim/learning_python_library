"""os.path.normcase(path)"""
# Нормализуйте регистр имени пути. В Windows преобразуйте все символы в имени пути
# в нижний регистр, а также преобразуйте косую черту в обратную косую черту.
# В других операционных системах верните путь без изменений.
# Изменено в версии 3.6: принимает объект, подобный пути.
# Windows
import os.path
# >>> os.path.normcase('C:\User\admin\Documents')
# c:\\user\\admin\\documents
print(os.path.normcase('/hoMe/UseR/'))
# \\home\\user
print(os.path.normcase(r'C:\Users/Desktop'))
# c:\\users\\desktop
