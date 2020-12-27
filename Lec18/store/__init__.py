import sqlite3 

conn = sqlite3.connect("info.db")
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, pages INT, price REAL)"
cur.execute(query_create)
conn.commit()


cur.close()
conn.close()