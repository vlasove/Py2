class SmartPhone:
    """
    Что можно делать с объектами этого класса
    ....
    ....
    ....
    ...
    ..
    """
    def __init__(self, mark:str, resolution:int, RAM:int, freq:float):
        self.__mark = mark 
        self.__resolution = resolution 
        self.__RAM = RAM
        self.__freq = freq 
        self.__like_counter = 0

    def set_resolution(self, new_resolution:int):
        if new_resolution <= 0:
            raise ValueError("Разрешение не может быть отрицательным числом!")
        self.__resolution = new_resolution

    

    def set_RAM(self, new_RAM:int):
        if new_RAM <= 0:
            raise ValueError("Величина оперативной памяти не может быть отрицательной!")
        self.__RAM = new_RAM

    #Наш гетэр для предоставления на чтение поля RAM
    def get_RAM(self):
        return self.__RAM
    
    def get_freq(self):
        return self.__freq 

    def get_mark(self):
        return self.__mark 

    def __str__(self):
        return f"Phone(Mark={self.__mark}, RAM={self.__RAM}, Freq={self.__freq})"

if __name__ == "__main__":
    samsung = SmartPhone("samsung", 1440, 3, 1.7)
    print(samsung.get_RAM())
    print("Мой телефон недостаточно мощный. Поставлю в него дополнительные 2 гб Оперативки")
    print("Оперативки было столько:", samsung.get_RAM())
    old_RAM = samsung.get_RAM()
    print("Увеличиваю на 2 гб")
    new_RAM = old_RAM + 2
    samsung.set_RAM(new_RAM)
    print("Теперь в моем телефоне вот столько гб опертивки:", samsung.get_RAM())
    print(samsung)