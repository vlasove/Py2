"""
Пример структуры Book
"""
class Book:
    title = ""
    actors = []
    rating = 0.0
    duration = 0


def create_book(title, actors, rating, duration):
    """
    Сборка книги
    """
    b1 = Book()
    b1.title =  title
    b1.actors = actors
    b1.rating = rating
    b1.duration = duration
    return b1 

def is_good(b:Book):
    """
    """
    return b.rating > 4.5 

