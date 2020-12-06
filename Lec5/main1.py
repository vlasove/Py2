"""
D1:P2 Pre-solution
"""
class Point:
    x = 0
    y = 0 

def create_point(x_coord :int, y_coord :int) -> Point:
    """
    Создает точку по координатам (x, y)
    """
    p = Point()
    p.x = x_coord
    p.y = y_coord
    return p 


class Triangle:
    first_point = Point()
    second_point = Point()
    third_point = Point()

def create_triangle(p1:Point, p2:Point, p3:Point) - >Triangle:
    """
    Создает треугольник по трем точкам
    """
    tr = Triangle()
    tr.first_point = p1 
    tr.second_point = p2 
    tr.third_point = p3 
    return tr 

def triangle_sides_calculation(triangle : Triangle) -> tuple:
    """
    Принимает на вход треугольник,
    возвращает кортеж из длин сторон треугольинка 
    (len(side1), len(side2), len(side3))
    """
    side1 = (triangle.first_point.x - triangle.second_point.x) ** 2 + (triangle.first_point.y - triangle.second_point.y) ** 2
    side1 = side1 ** 0.5 

    side2 = (triangle.second_point.x - triangle.third_point.x) ** 2 + (triangle.second_point.y - triangle.third_point.y) ** 2
    side2 = side2 ** 0.5 

    side3 = (triangle.third_point.x - triangle.first_point.x) ** 2 + (triangle.third_point.y - triangle.first_point.y) ** 2
    side3 = side3 ** 0.5

    return (side1, side2, side3) 

def triangle_perimeter(triangle : Triangle) -> int:
    """
    Высчитываем периметр треугольника и округляем как требуется по условию задачи
    """
    return int(sum(triangle_sides_calculation(triangle)))

def triangle_area(triangle : Triangle) -> int:
    """
    Высчитываем площадь треугольника и округляем как требуется по условию задачи
    """
    semi_p = triangle_perimeter(triangle) / 2
    pass 

"""
Блок считывания с консоли и создание теругольника
"""
x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
x3, y3 = [int(x) for x in input().split()]

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)
p3 = create_point(x3, y3)

triangle = create_triangle(p1, p2, p3)

