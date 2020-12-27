import collections

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __str__(self):
        return f'Point(x = {self.x}, y = {self.y})'

p = Point(1,2)
p2 = Point(1,3)

print(p, p2)

NewPoint = collections.namedtuple('NewPoint', ['x', 'y'])
new_p = NewPoint(1,2)
new_p2 = NewPoint(3,4)
print(new_p, new_p2)
