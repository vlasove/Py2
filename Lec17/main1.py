import json
# 2. Нативная десериализация
new_data = None
with open("data.json", "r") as fhand:
    new_data = json.load(fhand)

print("Read from json:", new_data)
print("Type:", type(new_data))