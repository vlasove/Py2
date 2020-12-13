"""
D1P2: A
"""
class Point:
    X = 0.0
    Y = 0.0

def create_point(x_coord:float, y_coord:float):
    """
    Из координат x_coord и y_coord создаем точку и возвращаем ее
    """
    p = Point()
    p.X = x_coord
    p.Y = y_coord
    return p

def line_equation_calculation(p1:Point, p2:Point):
    """
    По точкам p1 и p2 строит уравнение прямой вида y = kx + b 
    и возвращает пару коэффициентов (k, b)
    """
    pass 

def point_on_line(p3:Point, k:float, b:float):
    """
    Возвращает True если точка p3 принадлежит прямой y = kx + b
    False в противном случае
    """
    pass 

def coord_in_sample(p1:Point, p2:Point, p3:Point):
    """
    Возвращает True если точка P3 лежит между P1 И P2
    False  противном случае
    """
    pass 

# Образующие отрезка
x1, y1, x2, y2 = [int(x) for x in input().split()]
p1, p2 = create_point(x1,y1), create_point(x2, y2)

# Валидационная точка
x3, y3 = [int(x) for x in input().split()]
p3 = create_point(x3, y3)

k, b = line_equation_calculation(p1, p2)
if point_on_line(p3, k, b) and coord_in_sample(p1, p2, p3):
    print("YES")
else:
    print("NO")
