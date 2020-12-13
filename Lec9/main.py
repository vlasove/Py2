"""
Беды с инкапсуляцией
"""

class SmartPhone:
    """
    Класс описывающий классический смартфон
    """
    def __init__(self, mark:str, resolution:int, RAM:int, freq:float):
        self.mark = mark 
        self.resolution = resolution 
        self.RAM = RAM
        self.freq = freq 
        self.like_counter = 0

    def reboot(self):
        """
        Перезагрузка
        """
        if self.RAM < 0 or self.freq < 0:
            raise Exception("ПОШЛО ЧТО-ТО НЕ ТАК. ТЕЛЕФОН СЛОМАЛСЯ. ПОДУМОЙ ЧТО ТЫ НАДЕЛАЛ") 
    
        print("Rebooting........")
        for i in range(1000000):
            i**3
            continue 
        print("Done.....")

    def like(self):
        """
        Поставить лайк
        """
        self.like_counter += 1
        print("Like coefficient:", self.like_counter * self.resolution / self.RAM)

    def get_call(self):
        """
        Принимаем входящий звонок
        """
        if self.freq <0  and (self.mark is not None) :
            raise Exception("ЛУЧШЕ НЕ БЕРИ ТРУБКУ. ТЕЛЕФОН СОБРАН ГДЕ-ТО В ГАРАЖЕ")
        print("Get call .....")
    

samsung = SmartPhone("Samsung", 1440, 3, 1.9)
iphone = SmartPhone("IPhone", 10000, 400000, 99999999999992.1)
my_phone = SmartPhone("MyPhone", 1, 1, 1)


### Начнем работать с объектами
### 1. Часть. Общая перезагрузка
samsung.reboot()
iphone.freq = -30000000
samsung.resolution = -100
my_phone.reboot()
### 2. Часть . Прием входящих звонков
iphone.mark = "IPear" # Поскольку под крышку я уже залез - телефон слетел с гарантии . И я хочу его переназвать
samsung.get_call()
my_phone.get_call()


### 3. Часть . Попробуем лайкнуть котов
samsung.like()
my_phone.like()