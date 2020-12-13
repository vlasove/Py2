## Лекция 11. Полиморфизм
Вторая составляющая ***ООП*** - это полиморфизм.

***Полиморфизм*** - способность объекта наблюдения провлять свои свойства по-разному, в зависимости от окружающей обстановки.

### Шаг 1. Постановка задачи.
Допустим - вы ```UX-дизайнер```. Любая веб-страница представляет из себя полотно, заполненное различными геометрическими примитивами.  
Допустим на нашей странице существует 2 вида примитивов:
* Прямоугольный примитив
* Круглый примитив

***Задача*** подсчитать общую площадь и периметр абсолоюнто всех примитивов на странице. Если данные числа окажутся больше, чем некие пороговые значений - значет дизайн плохой (надо упрощать страницу). В случае, если все ок - можем даже добавить какие-нибудь новые элементы дизайна.

### Шаг 2. Описание классов Rectangle и Circle
```
class Rectangle:
    def __init__(self, length, width):
        self.__length = length 
        self.__width = width 

    def perimeter_rectangle(self):
        return 2 * (self.__length + self.__width)

    def area_rectangle(self):
        return self.__length * self.__width 



class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def perimeter_circle(self):
        return self.__radius * 2 * 3.14 

    def area_circle(self):
        return 3.14 * self.__radius ** 2 

### Блок инициализации примитивов
rect1 = Rectangle(100, 15)
rect2 = Rectangle(50, 30)
rect3 = Rectangle(45, 30)
rect4 = Rectangle(50, 30)

circ1 = Circle(10)
circ2 = Circle(11)
circ3 = Circle(9)

### Блок подсчета общей площади и общего периметра для прямоугольников
rectangles = [rect1, rect2, rect3, rect4]
total_rect_perimeter = 0
total_rect_area = 0
for rectangle in rectangles:
    total_rect_area += rectangle.area_rectangle()
    total_rect_perimeter += rectangle.perimeter_rectangle()

### Блок подсчета общей площади и общего периметра для кружочков
circles = [circ1, circ2, circ3]
total_circle_perimeter = 0
total_circle_area = 0
for circle in circles:
    total_circle_perimeter += circle.perimeter_circle()
    total_circle_area += circle.area_circle()

### Блок вывода ответа
print("Total primitive area:", total_circle_area + total_rect_area)
print("Total primitive perimeter:", total_rect_perimeter + total_circle_perimeter)
```


***Теперь введем полиморфные методы*** - полиморфные методы - это методы имеющие одинаковую сигнатуру (одинаковое поределение), но их результат будет зависеть от объекта, у которого они вызываются
```
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
```

Введение полиморфных методов позволяет создавать универсальный код, который легко масштабировать.
***Под масштабированием*** понимается процесс добавления новых сущностей, усовершенствование старых, с целью добавления нового функционала. Очень хочется, чтобы в процессе масштабирвоания старый код продолжал работать правильно - все это обеспечивает ***полиморфизм***.