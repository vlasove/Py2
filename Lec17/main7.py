import sqlite3

# создаем подключение 
conn = sqlite3.connect("data.db")
# создаем интерфейс взаимодействия с базой данных
cur = conn.cursor()



# Правила хорошего тона
cur.close()
conn.close()
