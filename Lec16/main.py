class Book:
    path_to_db = "database.db" # Классовые атрибуты

    def __init__(self, title, pages, author, price):
        self.title = title 
        self.pages = pages 
        self.author = author
        self.price = price 

    @classmethod 
    def born_book(cls, new_title):
        return cls(new_title, 0, None, 0)

    @staticmethod
    def create_databse(path_to_file):
        with open(path_to_file, "w") as fhand:
            fhand.write("created")


b = Book("hp1", 500, "Author", 500)
print(b.path_to_db)

b2 = Book("hp2", 600, "Author", 600)


print(Book.path_to_db)
b3 = Book.born_book("new book")

Book.create_databse("database.db")
