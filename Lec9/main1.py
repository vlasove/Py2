"""
Более умная реализация смартфона
"""

class SmartPhone:
    def __init__(self, mark:str, resolution:int, RAM:int, freq:float):
        self.__mark = mark 
        self.__resolution = resolution 
        self.__RAM = RAM
        self.__freq = freq 
        self.__like_counter = 0

    def __str__(self):
        return f"Phone(Mark={self.__mark}, RAM={self.__RAM}, Freq={self.__freq})"


# Шаг 1. Сделаем приватизацию для всех атрибутов класса SmartPhone - пользователь не должен уметь их менять в ручную
samsung = SmartPhone("Samsung", 1440, 3, 1.9)
samsung.__mark = "Nokia"
print(samsung)

#print("Samsung RAM:", samsung.__RAM)