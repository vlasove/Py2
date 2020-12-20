## Лекция 15. Модульное тестирование

***Задача:*** научиться контролировать "правильность" решения в рамках развития продукта.
Виды тестирования:
* Полное тестирование. ***Плюсы***: быстро, не нужно подготавливать код, легко реализуется. ***Минусы:*** сложно локализовать ошибку, ошибки могут в некоторых ситуациях компенсировать друг друга (может казаться, что в данный момент в коде нет ошибок, но на самом деле - их очень много).

* Модульное тестирование (```unit``` тестирование). Идея состоит в том, что мы разбиваем код на независимые друг от друга единицы (юниты) [***классы***, ***функции***] - ***декомпозируем*** код. Основная аксиома модульного тестирования состоит в том, что весь код работает правильно тогда и только тогда, когда ***каждый юнит работает правильно***. ***Плюсы:*** локализация ошибки, делаете код более читабельным. ***Минусы:*** разбивка на юниты требует предварительной подготовки кода.

### Шаг 1. Попробуем реализовать простейшее модульно тестирование
* Решаем задачку : https://contest.yandex.ru/contest/23646/problems/K/
* Лекция стартует в 14:15 (Нужно к этому моменту решить задачу)

Одно из возможных неправильных решений могло выглядеть вот так:
```
"""
Полотно решения задачи D3:K
"""
coeffs = []

with open("input.txt", "r") as fhand:
    line_with_coeffs = fhand.read() # "2 3 4"
    coeffs = [float(x) for x in line_with_coeffs.split()] # ["2" , "3", "4"]

def solve(coeffs:list):
    """
    Решатель квадратного уравнения
    """
    a, b, c = coeffs 
    d = b**2 - 4*a*c 
    if d > 0:
        return 2
    elif d == 0:
        return 1 
    return 0 

with open("output.txt", "w") as fhand:
    fhand.write(str(solve(coeffs)))
```

### Шаг 2. Попробуем обложить код модульными тестами.
Для того, чтобы обложить код модульными тестами нам необходимо ***ДЕКОМПОЗИРОВАТЬ*** наше решение. Под декомпозицией мы подразумеваем разбиение кода на независимые юниты.***Код работает верно тогда и только тогда, когда все юниты работают верно.***
***Предложение***. Введем в код 2 юнита ```linear(B,C)``` и ```quadratic(A,B,C)``` - функции, которые решают линейное и квадратное уравнение соответственно. Задаче же функции ```solve``` будет выбор - кому передать работу.


Реализуем функцию ```linear(B,C)```:
```
def linear(B:float, C:float):
    """
    Функция для решения линейного уравнения вида Bx + C = 0
    x = - C/B
    Возвращает количество корней
    """
    if B ==0:
        return 0 
    return 1
```

Реализуем функцию ```quadratic(A,B,C)```:
```
def quadratic(A:float, B:float, C:float):
    """
    Функция для решения квадратного уравнения вида Ax^2 + Bx + C = 0 
    Возвращает количество вещественных корней
    """
    D = B**2 - 4*A*C 
    if D > 0:
        return 2 
    elif D == 0:
        return 1 
    return 0
```

Перепишем функцию ```solve```:
```
def solve(coeffs:list):
    """
    Выбирает, какому решателю передать работу
    """
    if coeffs[0] == 0:
        return linear(coeffs[1], coeffs[2])
    return quadratic(coeffs[0], coeffs[1], coeffs[2])
```

И теперь наш код магическим образом стал понятным всем.
В итоге код выглядит следующим образом:
```
"""
Стандартное решения задачи D3:K
"""

def linear(B:float, C:float):
    """
    Функция для решения линейного уравнения вида Bx + C = 0
    x = - C/B
    Возвращает количество корней
    """
    if B ==0:
        return 0 
    return 1

def quadratic(A:float, B:float, C:float):
    """
    Функция для решения квадратного уравнения вида Ax^2 + Bx + C = 0 
    Возвращает количество вещественных корней
    """
    D = B**2 - 4*A*C 
    if D > 0:
        return 2 
    elif D == 0:
        return 1 
    return 0

def solve(coeffs:list):
    """
    Выбирает, какому решателю передать работу
    """
    if coeffs[0] == 0:
        return linear(coeffs[1], coeffs[2])
    return quadratic(coeffs[0], coeffs[1], coeffs[2])


def main():
    coeffs = []

    with open("input.txt", "r") as fhand:
        line_with_coeffs = fhand.read() # "2 3 4"
        coeffs = [float(x) for x in line_with_coeffs.split()] # ["2" , "3", "4"]

    with open("output.txt", "w") as fhand:
        fhand.write(str(solve(coeffs)))

if __name__ == "__main__":
    main()
```

### Шаг 2.1. Модульные тесты. Это кто?
В общем случае процесс модульного тестирования выглядит следующим образом
* выбираются по-очереди все юниты (функции, классы и т.д.)
* затем данные юниты выполняются на каком-то тестовом наборе (предположительно правильном)
* если юнит проходит все тестовые наборы - значит юнит валидный
* целый блок (программный модуль) работает верно <=> каждый юнит валидный

Создаются тесты по следующему сценарию:
```
import funcs as f 

# Импортируем стандартный фреймворк для написания модульных тестов
import unittest

"""
Для создания юнит-тестов данный фреймворк требует наличие тестового класса-сценария
Класс называют `Test<Module_Name>`
Наследуемся от встроенного класса unittest.TestCase
Для того, чтобы запустить данный модуль необходимо выполнить команду

python -m unittest -v test_funcs.py 
(-v) - полная тестовая развертка
"""
class TestFuncs(unittest.TestCase):
    """
    Тестовый сценарий для модуля funcs.py
    """
    # Создадим первый тест
    # важно - название теста начинается со слова `test_`
    def test_add(self):
        # TestCase #1
        self.assertEqual(f.add(2,3), 5)
        self.assertEqual(f.add(0, 10), 10)
        self.assertEqual(f.add(10, 0), 10)
        self.assertEqual(f.add(0,0), 0)
        self.assertEqual(f.add(-2,-3), -5)
        self.assertEqual(f.add(2, -2), 0)
        self.assertEqual(f.add(-2, 4), 2)
    
    def test_sub(self):
        self.assertEqual(f.sub(10, 2), 8)
        self.assertEqual(f.sub(2, 10), -8)
        self.assertEqual(f.sub(5, 0), 5)
        self.assertEqual(f.sub(0, 5), -5)
        self.assertEqual(f.sub(1, 9), -8)
        self.assertEqual(f.sub(-3, 10), -13)
        self.assertEqual(f.sub(-2, -9), 7)

    def test_mult(self):
        self.assertEqual(f.mult(0, 10), 0)
        self.assertEqual(f.mult(10, 3), 30)
        self.assertEqual(f.mult(20, 1), 20)
        self.assertEqual(f.mult(2,2), 4)


if __name__ == "__main__":
    unittest.main()

```

### Шаг 4. Квадратное уравнение
Общий код решения:
```
# equation.py
"""
Стандартное решения задачи D3:K
"""


def linear(b_arg: float, c_arg: float):
    """
    Функция для решения линейного уравнения вида Bx + C = 0
    x = - C/B
    Возвращает количество корней
    """
    if b_arg == 0 and c_arg != 0:
        return 0
    return 1


def quadratic(a_arg: float, b_arg: float, c_arg: float):
    """
    Функция для решения квадратного уравнения вида Ax^2 + Bx + C = 0
    Возвращает количество вещественных корней
    """
    descrim = b_arg**2 - 4 * a_arg * c_arg
    if descrim > 0:
        return 2
    if descrim == 0:
        return 1
    return 0


def solve(coeffs: list):
    """
    Выбирает, какому решателю передать работу
    """
    if coeffs[0] == 0:
        return linear(coeffs[1], coeffs[2])
    return quadratic(coeffs[0], coeffs[1], coeffs[2])


def main():
    """
    Основная точка входа в программу
    """
    coeffs = []

    with open("input.txt", "r") as fhand:
        line_with_coeffs = fhand.read()  # "2 3 4"
        coeffs = [float(x)
                  for x in line_with_coeffs.split()]  # ["2" , "3", "4"]

    with open("output.txt", "w") as fhand:
        fhand.write(str(solve(coeffs)))


if __name__ == "__main__":
    main()

```

Тесты дя квадратного уравнения:
```
# test_equation.py
import equation as eq 

import unittest 

class TestEquation(unittest.TestCase):
    def test_linear(self):
        self.assertEqual(eq.linear(10,2), 1)
        self.assertEqual(eq.linear(10, 0), 1)
        self.assertEqual(eq.linear(0, 10), 0) 

    def test_quadratic(self):
        self.assertEqual(eq.quadratic(1, 10000, 2), 2)
        self.assertEqual(eq.quadratic(3, 4, 5), 0)
        self.assertEqual(eq.quadratic(1, -4, 4), 1)
        self.assertEqual(eq.quadratic(10, 0, 0), 1) 

    def test_solve(self):
        self.assertEqual(eq.solve([0, 10, 2]), 1) 
        self.assertEqual(eq.solve([0, 10, 0]), 1)
        self.assertEqual(eq.solve([0, 0, 10]), 0)
        self.assertEqual(eq.solve([1, 10000, 2]), 2)
        self.assertEqual(eq.solve([3,4,5]), 0)


if __name__ == "__main__":
    unittest.main()
```

### Запуски
* Запуск модульных тестов : ```python -m unittest -v test_equation.py```
* Запуск ```autopep8``` : ```python -m autopep8 --in-place --aggressive equation.py```
* Запуск ```pylint``` : ```python -m pylint equation.py```
* Повторяем, пока не будем все ***супер-блестяще***.