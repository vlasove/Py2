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