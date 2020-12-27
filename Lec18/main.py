import sqlite3

# создаем подключение 
conn = sqlite3.connect("data.db")
# создаем интерфейс взаимодействия с базой данных
cur = conn.cursor()

#1. Запрос на создание таблицы в data.db
query_create = "CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, pages INT, price REAL)"
cur.execute(query_create)
conn.commit() # Применение выполненного запроса к бд (всегда выполняет супердолго)

#2. Запрос на добавление книги в data.db
#INSERT INTO books (title, author, pages, price) VALUES("LOTR:1", "J.J.Tolkin", 750, 14.99);
query_insert = "INSERT INTO books (title, author, pages, price) VALUES(?, ?, ?, ?)"
for i in range(1, 1000):
    book = ("LOTR:1", "J.J.Tolkin", 750+i, 14.99)
    cur.execute(query_insert, book)
conn.commit()

# 4. Скоро 2021, вермя увеличить все цены в 10 раз
query_update = "UPDATE books SET price = ? WHERE title = ?"
cur.execute(query_update, (149.99, "LOTR:1"))
conn.commit()

# 5. Удалим все книги, где страниц > 750
query_delete = "DELETE FROM books WHERE pages > 751"
cur.execute(query_delete)
conn.commit()
    
#3. Прочитаем что сейчас творится в бд
query_select = "SELECT * FROM books"
for row in cur.execute(query_select):
    print(row)


# Правила хорошего тона
cur.close()
conn.close()
