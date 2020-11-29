"""
Что можно делать из точек?
Задача: посчитать длину отрезка, построенного на точках p1 и p2
1) Используем теорему Пифагора и создадим функцию length_calc
"""

class Point:
    x = 0.0
    y = 0.0 

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

p1 = create_point(0, 0)
p2 = create_point(5, 5)

print("Length of:", length_calc(p1, p2))
print("Proof:", length_calc(p2, p1))