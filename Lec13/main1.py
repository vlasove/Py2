class Horse:
    """
    Лошадь(конь) - класс родитель
    """
    hooves = 4 # копыта
    tail =  True 
    weight = 250
    body = True 
    love_grass = True 


class Unicorn(Horse):
    """
    Наш шедевр. Мы хотим его создать по образу и подобию Horse
    """
    has_horn = True 

h = Horse()
u = Unicorn()

h.weight = 360
print(h.weight)
print(u.weight)