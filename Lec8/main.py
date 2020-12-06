"""
Переопределение (shadowing - затенение)
"""


class Calculator:
    def __init__(self, x:int, y:int):
        self.x_value = x 
        self.y_value = y 


    def calc(self):
        return self.x_value + self.y_value

    def calc(self):
        return self.x_value ** 2 + self.y_value ** 2


c = Calculator(2,10)
print(c.calc())