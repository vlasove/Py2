import pickle 
"""
Модуль низкоуровневой сериализации в Python
"""

data = [
    {"id":1, "name":True},
    {"id":501, "name" :"alice"},
    {"id":None, "name" : "petya"},
]

# 3. Сериализация в байтовый файл
with open("data.pickle", "wb") as fhand:
    pickle.dump(data, fhand)


# 4. Десериализация из байтового файла
new_data = None 
with open("data.pickle", "rb") as fhand:
    new_data = pickle.load(fhand)

print(new_data)