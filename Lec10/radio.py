"""
Модуль содержащий реализацию класса Radio
"""

class Radio:
    """
    Класс Radio = радиоприемник
    Состояние описывается как:
    * model - модель радиоприемника
    * capacity - величина емкости (элемент колебательного контура)
    * volume - громкость (мощность колебаний диафрагмы)

    Публичный интерфейс:
    * get_model()
    * get_capacity()
    * get_volume()
    * set_model()
    * set_capacity()
    * set_volume()
    * change_radiostation() - метод, изменяющий текущую радиоволну
    * change_sound_volume() - метод, который делает тише/громче

    Приватный интерфейс:
    * capacity_up() - увеличивает емкость конденсатора
    * capacity_down() - уменьшает емкость конденсатора
    * volume_up() - увеличивает мощность колебаний диафрагмы
    * volume_down() - уменьшает мощность колебаний диафрагмы
    """
    def __init__(self, model:str, capacity:int, volume:int):
        self.__model = model  
        self.__capacity = capacity 
        self.__volume = volume 

    ### Здесь блок с гетэрами и сетэрами
    def change_radiostation(self, change_to:int):
        if change_to > 0:
            self.__capacity_up(change_to)
        else:
            self.__capacity_down(change_to)

    def change_sound_volume(self, change_to:int):
        if change_to > 0:
            self.__volume_up(change_to)
        else:
            self.__volume_down(change_to)

    def __capacity_up(self, change_to:int):
        print("ПРОИСХОДЯТ СЛОЖНЕЙШИЕ ЭЛЕКТРОТЕХНИЧЕСКИЕ ПРЕОБРАЗОВАНИЯ КОТОРЫЕ МОГУТ ПРИВЕСТИ К СМЕРТИ РАДИОПРИЕМНИКА")
        print("В ИТОГЕ ВСЕ ОК! Частота увелична")
        self.__capacity += change_to

    def __capacity_down(self, change_to:int):
        print("ПРОИСХОДЯТ СЛОЖНЕЙШИЕ ЭЛЕКТРОТЕХНИЧЕСКИЕ ПРЕОБРАЗОВАНИЯ КОТОРЫЕ МОГУТ ПРИВЕСТИ К СМЕРТИ РАДИОПРИЕМНИКА")
        print("В ИТОГЕ ВСЕ ОК! Частота уменьшена")
        self.__capacity -= change_to

    def __volume_up(self, change_to:int):
        pass 

    def __volume_down(self, change_to:int):
        pass 


radio = Radio("Soviet Radio Slasher-Trasher 9000", 100, 50)
## Имитация "крутилки" на радиоприемника
radio.change_radiostation(3)
radio.change_radiostation(-2)
# Теперь я срываю крышку и крутилку. И вручную меняю расстояние между обкладками конденсатора колебательного контура
radio.__capacity_up(3)

