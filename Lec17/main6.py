import pickle 
# 2. Не плохая идея (СУПЕР ЧАСТО ИСПОЛЬЗУЮТ ПРИ СОХРАНЕНИИ ЯДЕР НЕЙРОННЫХ СЕТЕЙ)

class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author 

    def print(self):
        print(f"Book[{self.title}, {self.author}]")


serialized_class = pickle.dumps(Book)
print(serialized_class)

new_Book = pickle.loads(serialized_class)
nb = new_Book("LOTR:1", "J.J. Tolkin")
nb.print()