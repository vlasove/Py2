class Rectangle:
    def __init__(self, length, width):
        self.__length = length 
        self.__width = width 

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width 



class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return self.__radius * 2 * 3.14 

    def area(self):
        return 3.14 * self.__radius ** 2 

class Trianlge:
    def __init__(self, a, b, c):
        self.__a = a 
        self.__b = b 
        self.__c = c 

    def perimeter(self):
        return self.__a + self.__b + self.__c 

    def area(self):
        """
        Как во 2-ом классе
        """
        return self.__a * self.__b * self.__c 

### Блок инициализации примитивов
rect1 = Rectangle(100, 15)
rect2 = Rectangle(50, 30)
rect3 = Rectangle(45, 30)
rect4 = Rectangle(50, 30)

circ1 = Circle(10)
circ2 = Circle(11)
circ3 = Circle(9)

triang1 = Trianlge(10, 20, 30)
triang2 = Trianlge(10, 20 ,30)

### Создадим список фигур
figures = [rect1, rect2, rect3, rect4, circ1, circ2, circ3, triang1, triang2]

total_area = 0
total_perimeter = 0

for figure in figures:
    total_area += figure.area()
    total_perimeter += figure.perimeter()

### Блок вывода ответа
print("Total primitive area:", total_area)
print("Total primitive perimeter:", total_perimeter)