import pickle 

# Плохая №1. Сериализауем явную функцию
def add(a:int, b:int):
    """
    a + b
    """
    return a + b 

serialized_function = pickle.dumps(add)
print("Serialized function:", serialized_function)

# Создадайте вместо этой конструкции - промежуточный файл
#del add

new_add = pickle.loads(serialized_function)
print("result of add(2,3):", new_add(2,3))