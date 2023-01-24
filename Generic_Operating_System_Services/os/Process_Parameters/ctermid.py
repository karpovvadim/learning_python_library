"""os.ctermid()"""
# Вернуть имя файла, соответствующее управляющему терминалу процесса.
#      Доступность: Unix, не Emscripten, не WASI.

import os
print("os.ctermid(): ", os.ctermid())
