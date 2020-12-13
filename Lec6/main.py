"""
Пример простейшего класса
"""
class Book:
    title = ""
    author = ""

    def read(self):
        """
        Метод выводит на консоль факт того, что эту книгу читают
        """
        print("Now I'm reading book with title:", self.title, "and author:", self.author)

    def get_title(self):
        """
        Метод возвращает название книги
        """
        return self.title 

    def get_author(self):
        """
        Метод возвращает автора книги
        """
        return self.author

b = Book()
b.title = "HP:1"
b.author = "J. Rawling"

b.read()
print("Title:", b.get_title())
print("Author:", b.get_author())