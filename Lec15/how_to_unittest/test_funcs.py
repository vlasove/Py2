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