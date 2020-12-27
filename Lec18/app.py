from store.book import Book

b = Book("LOTR:2", "J.J.Tolkin", 1750, 15.99)

print("Initital creation:")
b.save()
Book.read_all() # выводит на печать все объекты из бд
print("After update:")
b.update_pages(1950) # обновляет количество страниц у данной книги
Book.read_all() # выводит на печать все объекты из бд
print('After delete:')
b.delete() # удаляет эту книги из БД
Book.read_all() # выводит на печать все объекты из бд


