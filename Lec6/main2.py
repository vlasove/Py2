class Point:
    def __init__(self, X_FROM_INIT, Y_FROM_INIT):
        self.x = X_FROM_INIT
        self.y = Y_FROM_INIT
        
    def print_point(self):
        print("X:", self.x, "Y:", self.y)
        self.z = 200

    def print_point_Z(self):
        print("X:", self.x, "Y:", self.y, "Z:", self.z)

p = Point(10, 20)
p.print_point_Z()
p.print_point()

