"""
Создадим структуру Point.
1) Создаем функцию, которая распечатывает информацию про точку.

def print_point(x:float, y:float):
    print("Point Xcoord=", x, "Ycoord=", y) 

2) Создаем функцию, которая работает НА ПРЯМУЮ, с представителями структур Point
def print_point(p:Point):
    ```
    Функция для вывода на печать отдельно взятой конкретной точки p
    ```
    print("Point Xcoord=", p.x, "Ycoord=", p.y) 

3) Создадим функцию, для удобного порождения новых точек:
def create_point(x_coord:float, y_coord:float):
    ```
    Из координат x_coord и y_coord создаем точку и возвращаем ее
    ```
    p = Point()
    p.x = x_coord
    p.y = y_coord
    return p
"""
class Point:
    x = 0.0
    y = 0.0 

def print_point(p:Point):
    """
    Функция для вывода на печать отдельно взятой конкретной точки p
    """
    print("Point Xcoord=", p.x, "Ycoord=", p.y) 

def create_point(x_coord:float, y_coord:float):
    """
    Из координат x_coord и y_coord создаем точку и возвращаем ее
    """
    p = Point()
    p.x = x_coord
    p.y = y_coord
    return p

# Создание представителя структуры Point == Создание конкретной точки
p1 = create_point(5,5)
p2 = create_point(10, 10)

# Выведу на консоль информацию про первую точку
print_point(p1)

# -//- для второй точки
print_point(p2)

