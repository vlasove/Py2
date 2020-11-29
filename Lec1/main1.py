"""
Условный оператор и циклы
"""
age = 28

if age <= 14:
    print("<= 14")
    print("body")
elif age <= 14:
    print("body 2")
elif age <= 25:
    print("body 3")
else:
    print("body 4")


# while True:
#     password = input()
#     if len(password) > 10:
#         break 
#     print('Try again')


for i in range(1, 100, 2):
    print("Elem:", i)