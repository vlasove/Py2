"""
Пусть задано 4 точки, и известно , что они образуют прямоугольный примитив.
Задача: подсчитать периметр и плозадь примитива.
1) Периметр: perimetr(p1:Point, p2:Point, p3:Point, p4:Point)
2) area(p1:Point, p2:Point, p3:Point, p4:Point):
"""

class Point:
    x = 0.0 # Атрибут x класса (структуры) Point
    y = 0.0 # Атрибут y класса (структуры) Point

def create_point(x_coord:float, y_coord:float):
    """
    Из координат x_coord и y_coord создаем точку и возвращаем ее
    """
    p = Point()
    p.x = x_coord
    p.y = y_coord
    return p


def print_point(p:Point):
    """
    Функция для вывода на печать отдельно взятой конкретной точки p
    """
    print("Point Xcoord=", p.x, "Ycoord=", p.y) 


def length_calc(p1:Point, p2:Point):
    """
    Считает Декартово расстояние между двумя точками на 2Д плоскости
    """
    deltaX = p1.x - p2.x 
    deltaY = p1.y - p2.y 
    length = (deltaX**2 + deltaY**2) ** 0.5 
    return length

def perimetr(p1:Point, p2:Point, p3:Point, p4:Point):
    """
    Считает периетр прямоугольника p1p2p3p4
    """
    side1 = length_calc(p1, p2)
    side2 = length_calc(p2, p3)
    side3 = length_calc(p3, p4)
    side4 = length_calc(p4, p1)

    return side1 + side2 + side3 + side4

def area(p1:Point, p2:Point, p3:Point, p4:Point):
    """
    Считает периетр прямоугольника p1p2p3p4
    """
    side1 = length_calc(p1, p2)
    side2 = length_calc(p2, p3)
    # side3 = length_calc(p3, p4)
    # side4 = length_calc(p4, p1)

    return side1 * side2

p1 = create_point(0, 0)
p2 = create_point(0, 5)
p3 = create_point(5,5)
p4 = create_point(5, 0)

print("Perimeter:", perimetr(p1, p2, p3, p4))
print("Area:", area(p1, p2, p3, p4))
# Как считать 4 значения из одной строки
input().split() # 0 0 10 10 -> ["0", "0", "10", "10"]