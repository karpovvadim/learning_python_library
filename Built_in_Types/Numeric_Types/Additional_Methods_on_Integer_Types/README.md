            Additional Methods on Integer Types     
            Дополнительные методы для целочисленных типов
Тип int реализует numbers.Integral абстрактный базовый класс.
Кроме того, он предоставляет ещё несколько методов:

int.bit_length()
int.bit_count()
int.to_bytes(length=1, byteorder='big', *, signed=False)
classmethod int.from_bytes(bytes, byteorder='big', *, signed=False)
int.as_integer_ratio()