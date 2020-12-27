import pickle 
# 2. Не плохая идея (СУПЕР ЧАСТО ИСПОЛЬЗУЮТ ПРИ СОХРАНЕНИИ ЯДЕР НЕЙРОННЫХ СЕТЕЙ)

class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author 

    def print(self):
        print(f"Book[{self.title}, {self.author}]")

b =Book("hp1", "several authors")

serialized_b = pickle.dumps(b)
print(serialized_b)

new_b = pickle.loads(serialized_b)
new_b.print()