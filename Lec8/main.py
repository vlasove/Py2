"""
Переопределение (shadowing - затенение)
"""
class Point:
    def __init__(self, x, y):
        self.x_val = x 
        self.y_val = y 
    def __str__(self):
        return f"Point[X:{self.x_val}, Y:{self.y_val}]" 
    
    def __eq__(self, other): 
        return (self.x_val, self.y_val) == (other.x_val, other.y_val) 

    def __gt__(self, other): # Сравнение строго `>`. Аналог __lt__
        """
        greater than
        """
        return (self.x_val, self.y_val) > (other.x_val, other.y_val)

    def __ge__(self, other): # Сравнение на `>=`. Важно, что `>=` это не `>` + `==`
        return (self.x_val, self.y_val) >= (other.x_val, other.y_val)

    def __del__(self): # Этот метод вызывается в тот момент, когда происходит передача вашего объекта GC
        print("ЭТОТ ОБЪЕКТ ПЕРЕДАН ВО ВЛАЖНЫЕ ЛАДОШКИ СБОРЩИКА МУСОРА")
        print(self)


p = Point(10, 20)
1/0
p2 = Point(30, 40)

