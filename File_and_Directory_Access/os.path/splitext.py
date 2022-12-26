"""os.path.splitext(path)"""
# Разделите путь пути на пару (root, ext) так, чтобы root + ext == path, а
# расширение ext было пустым или начиналось с точки и содержало не более одной точки.
# Если путь не содержит расширения, ext будет '':
import os.path
print(os.path.splitext('/os.path/splitext'))
# Если путь содержит расширение, то расширение будет установлено на это расширение,
# включая начальную точку. Обратите внимание, что предыдущие периоды будут игнорироваться:
print(os.path.splitext('os.path/splitext.py'))
print(os.path.splitext('/os.path/splitext.py'))
# Старшие периоды последнего компонента пути считаются частью корня:
print(os.path.splitext('.File_and_Directory_Access'))
print(os.path.splitext('/vadim/python_library/....jpg'))
# Изменено в версии 3.6: принимает объект, подобный пути.
