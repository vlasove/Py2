"""
Пример с машиной
"""

class Car:
    price = 0
    rating = 0.0 
    mark = ""
    hp = 0

    def ride(self):
        print("Now I'm riding on my super :", self.mark)
        print("My HP:", self.hp)

    def tuning(self, hp_dop):
        """
        Добавляем лошадиных сил
        """
        self.hp = self.hp + hp_dop

def create_car(price_arg, rating_arg, mark_arg, hp_arg) -> Car:
    """
    Создаем машину и возвращаем
    """
    c = Car()
    c.price = price_arg
    c.rating = rating_arg
    c.mark = mark_arg
    c.hp = hp_arg
    return c 

c1 = create_car(100, 0.00009, "Lada", -2)
c2 = create_car(200000000, 2.0, "Bugatti", -1)
c3 = create_car(30000, 5.0, "BMW", 0)
cars = [c1, c2, c3]
for car in cars:
    car.ride()
    car.tuning(15)
    car.ride()