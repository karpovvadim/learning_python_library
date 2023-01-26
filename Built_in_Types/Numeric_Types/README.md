            Numeric Types — int, float, complex
            Числовые типы — int, float, комплекс

Существует три различных числовых типа: целые числа, числа с плавающей запятой и
комплексные числа. Кроме того, логические значения являются подтипом целых чисел.
Целые числа имеют неограниченную точность. Числа с плавающей запятой обычно реализуются
с помощью double в C; информация о точности и внутреннем представлении чисел с плавающей
запятой для машины, на которой работает ваша программа, доступна в sys.float_info.
Комплексные числа имеют действительную и мнимую части, каждая из которых является числом
с плавающей запятой. Чтобы извлечь эти части из комплексного числа z, используйте z.real
и z.imag. (Стандартная библиотека включает дополнительные числовые типы дроби. Фракция
для рациональных чисел и десятичная дробь. Десятичная для чисел с плавающей запятой с
определяемой пользователем точностью.)
Числа создаются числовыми литералами или в результате встроенных функций и операторов.
Целые литералы без прикрас (включая шестнадцатеричные, восьмеричные и двоичные числа) 
дают целые числа. Числовые литералы, содержащие десятичную точку или знак экспоненты,
дают числа с плавающей запятой. Добавление 'j' или 'J' к числовому литералу дает мнимое
число (комплексное число с нулевой действительной частью), которое вы можете добавить
к целому числу или вещественному числу, чтобы получить комплексное число с действительной
и мнимой частями.
Python полностью поддерживает смешанную арифметику: когда двоичный арифметический 
оператор имеет операнды разных числовых типов, операнд с «более узким» типом расширяется
до другого, где целое уже, чем с плавающей запятой, которое уже, чем сложное. Сравнение
между числами разных типов ведет себя так, как будто сравниваются точные значения этих 
чисел. Как следствие, список [1, 2] считается равным [1.0, 2.0] и аналогично для кортежей.
Конструкторы int(), float() и complex() могут использоваться для получения чисел 
определенного типа.
Все числовые типы (кроме сложных) поддерживают следующие операции
(о приоритетах операций см. Приоритет оператора):

Операция 	Результат 	                            Примечания  Полная документация
x + y 	        сумма x и y 	  	 
x - y 	        разница x и y 	  	 
x * y 	        умножение x и y 	  	 
x / y 	        частное от x и y 	  	 
x // y 	        целочисленное частное x и y 	    (1) 	 
x % y 	        оставшаяся часть x / y 	            (2) 	 
-x 	            измененный x 	  	 
+x 	            x без изменений 	  	 
abs(x) 	        абсолютное значение или величина x 	            abs()
int(x) 	        x конвертируется в целое число 	    (3)(6) 	    int()
float(x) 	    x преобразован в число с плавающей  (4)(6) 	    float()
                точкой 	                            
complex(re, im) комплексное число с действительной  (6) 	    complex()
                частью re, мнимая часть im. im по
                умолчанию ноль. 	                
c.conjugate() 	сопряжение комплексного числа c 	  	 
divmod(x, y) 	пара (x // y, x % y) 	            (2) 	    divmod()
pow(x, y) 	    х в степени у 	                    (5) 	    pow()
x ** y 	        х в степени у 	                    (5) 	

Примечания:
    1. Также называется целочисленным делением. Результирующее значение — целое число,
хотя тип результата необязательно должен быть int. Результат всегда округляется до минус
бесконечности: 1//2 — это 0, (-1)//2 — это -1, 1//(-2) — это -1, а (-1)//(-2) — это 0.
    2. Не для комплексных чисел. Вместо этого конвертируйте в числа с плавающей запятой,
используя abs(), если это необходимо.
    3. Преобразование из числа с плавающей запятой в целое число может округляться или
усекаться, как в C; см. функции math.floor() и math.ceil() для чётко определенных 
преобразований.
    4. float также принимает строки «nan» и «inf» с необязательным префиксом «+» или «-»
для Not a Number (NaN) и положительной или отрицательной бесконечности.
    5. Python определяет pow(0, 0) и 0 ** 0 как 1, что является обычным для языков 
программирования.
    6. Допустимые числовые литералы включают цифры от 0 до 9 или любой Юникод эквивалент
(кодовые точки со свойством Nd).
    См. https://www.unicode.org/Public/14.0.0/ucd/extracted/DerivedNumericType.txt
стандарт для получения полного списка кодовых точек со свойством Nd.

Все типы numbers.Real (int и float) также включают следующие операции:

Операция 	        Результат

math.trunc(x) 	    x усечено до Integral
round(x[, n]) 	    x округляется до n цифр, округление половины до чётной. Если n пропущено, значение по умолчанию равно 0.
math.floor(x) 	    большее Integral <= x
math.ceil(x) 	    меньшее Integral >= x

Дополнительные числовые операции см. в модулях math и cmath.

            Bitwise Operations on Integer Types
            Побитовые операции с целыми типами¶

Побитовые операции имеют смысл только для целых чисел. Результат поразрядных операций 
вычисляется так, как если бы они выполнялись с дополнением до двух с бесконечным числом
битов знака.
Приоритеты двоичных побитовых операций ниже, чем у числовых операций, и выше, чем у
сравнений; у унарной операции ~ тот же приоритет, что и у других унарных числовых 
операций (+ и -).
В этой таблице перечислены побитовые операции, отсортированные по возрастанию приоритета:

Операция 	Результат 	                        Примечания
x | y 	    побитовое или x и y 	            (4)
x ^ y 	    побитовое исключающее или x и y 	(4)
x & y 	    побитовое и x и y 	                (4)
x << n 	    сдвинуть x влево на n бит 	        (1)(2)
x >> n 	    сдвинуть x вправо на n бит 	        (1)(3)
~x 	        инверсия бит x 	 

Примечания:
    1. Отрицательный счётчик сдвигов недопустим и вызывает исключение ValueError.
    2. Сдвиг влево на n битов эквивалентен умножению на pow(2, n).
    3. Сдвиг вправо на n битов эквивалентен делению с округлением вниз на pow(2, n).
    4. Выполнение этих вычислений по крайней мере с одним дополнительным битом 
расширения знака в конечном представлении с двумя дополнениями 
(рабочая разрядность 1 + max(x.bit_length(), y.bit_length()) или более) достаточно 
для получения того же результата, как если бы было бесконечное количество битов знака.