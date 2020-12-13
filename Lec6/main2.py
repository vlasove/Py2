class Point:
    def __init__(self, X_FROM_INIT, Y_FROM_INIT):
        self.x = X_FROM_INIT
        self.y = Y_FROM_INIT
        self.z = 200
        
    def print_point(self):
        print("X:", self.x, "Y:", self.y)
       

    def print_point_Z(self):
        print("X:", self.x, "Y:", self.y, "Z:", self.z)

    def length(self, another_point):
        return ((self.x -another_point.x)**2 + (self.y - another_point.y) ** 2 )**0.5


class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1 
        self.p2 = p2 

    def length(self):
        return ((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2 )**0.5 

p = Point(10, 20)
p2 = Point(30, 40)
p.print_point_Z()
p.print_point()

val = p.length(p2)

l = Line(p, p2)
l.length()
