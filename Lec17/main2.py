import pickle 
"""
Модуль низкоуровневой сериализации в Python
"""

data = [
    {"id":1, "name":True},
    {"id":501, "name" :"alice"},
    {"id":None, "name" : "petya"},
]

# 1. Представим объект data в виде байтовой последовательности и посмотрим на нее
serialized_data = pickle.dumps(data) # сериализовать и вернуть в виде строки
print(serialized_data)

# 2. Попробуем десериализовать из байтовой строки
new_data = pickle.loads(serialized_data)
print(new_data)