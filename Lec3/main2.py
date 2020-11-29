"""
Хотим создать сервис для потокового воспроизведения фильмов.
Для того, чтобы сохранить фильм, нужно сохранить "критерии фильмовости".

Для того, чтобы сохранить фильмы, создадим структуру Film и опишем в ней все необходимые критерии.


Класс КАК структура.
Структура - это заименованный набор полей.
Для доступа к полям структуры используют следующий синтаксис:
представитель.ПОЛЕ_СТРУКТУРЫ (например f1.title)
"""

class Film:
    title = ""
    duration = 0 
    rating = 0.0 
    actors = []

f1 = Film() # Создаем первого представителя типа Film
f1.title = "HP:1"
f1.duration = 210
f1.rating = 4.9
f1.actors = ['Emma Watson', 'Friend1', 'Rupert Grin']

f2 = Film()
f2.title = "LOTR:1"
f2.duration = 999
f2.rating = 4.8 
f2.actors = ['O Blum', 'Friend1', 'Friend2', 'Fritend3']

f3 = Film()
f3.rating = 5.0


# Самый главный плюс
films = [f1, f2, f3]

for film in films:
    print("Title:", film.title, "Actors:", film.actors)