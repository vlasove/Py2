"""
Базовые типы.
1) int()
2) float()
3) str()
4) bool()
5) NoneType() 
"""

# Целые числа + Веществ
print("Rem:", 10 % 5)
print("Int divs:", -4 //3 )
print("Pow:", 4 ** 3)

a_int = 20
b_float = 20.5
print(a_int + b_float)


# Строки str()
message = "Hello world!"
letter = "m"
empty = ""


print("Len:", len(message))
print(message + " concating")
print(message * 10)

# Логический тип
t_bool, f_bool = True, False 
print("Result:", t_bool + t_bool**(f_bool + 200) and t_bool)

# NoneType()
a_none = None 