data = [
    {"id":1, "name":True},
    {"id":501, "name" :"alice"},
    {"id":None, "name" : "petya"},
]

# Хотелка - хотим сохранить этот объект data с его структурой
import json 
"""
JavaScript Object Notation
"""

# 1. Нативная сераилизация
with open("data.json", "w") as fhand:
    json.dump(data, fhand, indent=4)


