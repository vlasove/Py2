## Лекция 18. Реализация простейшего ORM-принципа

***ORM***-принцип - это рекомендации по созданию объектов в архитектуре того или иного языка, с включением ***МЕТОДОВ***, позволяющих этому объекту обзаться с какой-либо базой данных.

***ORM == Object Relational Mapping***

***Основная задача при реализации принипа ORM*** состоит в том, чтобы наделить объект возможность удовлетворять правилу ```CruD```.

***CrUD*** = ```Create + Update + Delete``` /(```Create + Read + Update + Delete```)


### Шаг 1. Определим базовый объект book
* Создадим отдельный пакет ```store```
* Определим в пакете ```__init__.py``` , ```book.py```

* Реализуем базовы методы для ```Book```:
```
"""
Модуль для рабоыт с книгой
"""

class Book:
    def __init__(self, title:str, author:str, pages:int, price:float):
        self.__title = title 
        self.__author = author
        self.__pages = pages 
        self.__price = price 


    def __str__(self):
        return f"Book(title = {self.__title}, author = {self.__author}, pages = {self.__pages})" 
```


### Шаг 2. Инициализация БД в файле ```__init__.py```
Поскольку файл ```__init__.py``` выполняет самым первы при первом обращении к пакету ```store``` есть идея, поместить в него код, который будет инициализировать бд, если ее еще не было создано.

```
# __init__.py

import sqlite3 

conn = sqlite3.connect("info.db")
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, pages INT, price REAL)"
cur.execute(query_create)
conn.commit()


cur.close()
conn.close()
```

```
# store/book.py
"""
Модуль для работы с книгой
"""
import sqlite3

class Book:
    __database__ = "info.db"
    __tablename__ = "books"
    def __init__(self, title:str, author:str, pages:int, price:float):
        self.__title = title 
        self.__author = author
        self.__pages = pages 
        self.__price = price 

    def save(self):
        conn = sqlite3.connect(self.__database__)
        cur = conn.cursor()

        query_insert = f"INSERT INTO {self.__tablename__} VALUES(?, ?, ?, ?)"
        cur.execute(query_insert, (self.__title, self.__author, self.__pages, self.__price))
        conn.commit()

        cur.close()
        conn.close()

    def delete(self):
        conn = sqlite3.connect(self.__database__)
        cur = conn.cursor()

        query_delete = f"DELETE FROM {self.__tablename__} WHERE title = ?"
        cur.execute(query_delete, (self.__title, ))
        conn.commit()
        cur.close()
        conn.close()

    def update_pages(self, page_to_update:int):
        conn = sqlite3.connect(self.__database__)
        cur = conn.cursor()

        query_update = f"UPDATE {self.__tablename__} SET pages = ? WHERE title = ?"
        cur.execute(query_update, (page_to_update, self.__title))
        conn.commit()


        cur.close()
        conn.close()

    @classmethod
    def read_all(cls):
        conn = sqlite3.connect(cls.__database__)
        cur = conn.cursor()

        query_select = f'SELECT * FROM {cls.__tablename__}'
        for row in cur.execute(query_select):
            print(row)

        cur.close()
        conn.close()



    def __str__(self):
        return f"Book(title = {self.__title}, author = {self.__author}, pages = {self.__pages})" 
```

