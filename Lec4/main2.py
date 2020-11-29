"""
Проблема. Функция create_point пусть и не принимает в качестве входных аргументов объект Point,
но эта функция имеет непосредственное отношение к классу Point (она порождает объекты).

Решение - запихаем в класс!
"""



class Point:
    y = 0.0 
    x = 0.0 

    def print_point(self):
        print("Point(X=",self.x, ", Y=", self.y, ")")

    def print_shifted(self, shift:int):
        print("PointShifted(X=", self.x + shift, ", Y=", self.y + shift, ")")

    # Функция, которая конфигурирует объект на этапе его создания - конструктор
    def create_point(self, x_coord:float, y_coord:float):
        """
        Из координат x_coord и y_coord создаем точку и возвращаем ее
        """
        self.x = x_coord
        self.y = y_coord


p = Point()
p.print_point()
p.create_point(10, 20)
p.print_point()
