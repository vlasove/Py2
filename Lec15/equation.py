"""
Стандартное решения задачи D3:K
"""
# import equation as eq

# import unittest

# class TestEquation(unittest.TestCase):
#     def test_linear(self):
#         self.assertEqual(eq.linear(10,2), 1)
#         self.assertEqual(eq.linear(10, 0), 1)
#         self.assertEqual(eq.linear(0, 10), 0)

#     def test_quadratic(self):
#         self.assertEqual(eq.quadratic(1, 10000, 2), 2)
#         self.assertEqual(eq.quadratic(3, 4, 5), 0)
#         self.assertEqual(eq.quadratic(1, -4, 4), 1)
#         self.assertEqual(eq.quadratic(10, 0, 0), 1)

#     def test_solve(self):
#         self.assertEqual(eq.solve([0, 10, 2]), 1)
#         self.assertEqual(eq.solve([0, 10, 0]), 1)
#         self.assertEqual(eq.solve([0, 0, 10]), 0)
#         self.assertEqual(eq.solve([1, 10000, 2]), 2)
#         self.assertEqual(eq.solve([3,4,5]), 0)


# if __name__ == "__main__":
#     unittest.main()


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
