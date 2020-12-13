"""
Обход приватизации или почему она условная?
"""
class Book:
    def __init__(self, title):
        self.__title = title 

    def __print(self):
        print("This book has title:", self.__title)


b = Book("LOTR:1")
print(b._Book__title )
b._Book__title = "HP:1"
b._Book__print()
print(dir(b))