class Figure:
    """
    Родительский класс - фигура.
    Знает про цвет и красивый ли он?
    """
    def __init__(self, color:str, nice:bool):
        self.color = color
        self.nice = nice 

    def get_color(self):
        return self.color 

    def __str__(self):
        return f'Figure(color={self.color}, nice={self.nice})'

class Circle(Figure):
    """
    Дочерний класс - кружок.
    У него есть цвет, он знает про то, красивый ли он, а еще умеет
    считать периметр и площадь
    """
    
    def __init__(self, color:str, nice:bool, R:float):
        """
        Хотим передать работу родительскому классу по определению
        атрибутов color и nice
        """
        super().__init__(color, nice)
        self.R = R 

    def perimeter(self):
        print(self.get_color())
        return self.R * 3.14 * 2 

    def area(self):
        print(self.get_color())
        return 3.14 * self.R ** 2

    def __str__(self):
        return f'Circle(color={self.color}, nice={self.nice}, R={self.R})'

c = Circle("green", True, 10)
f = Figure("red", False )

print(c)
print(f)

c.perimeter()
c.area()