import funcs as f 

"""
В общем случае процесс модульного тестирования выглядит следующим образом
* выбираются по-очереди все юниты (функции, классы и т.д.)
* затем данные юниты выполняются на каком-то тестовом наборе (предположительно правильном)
* если юнит проходит все тестовые наборы - значит юнит валидный
* целый блок (программный модуль) работает верно <=> каждый юнит валидный
"""

"""
Блок кода, вмещающий в себя набор Test-Case'ов для одного юнита - это один тест
"""
# Test-case #1
if f.add(2,3) == 5:
    print("add(2,3) == 5. Test passed!")
else:
    raise ValueError("add(2,3) != 5. Test failed!")

# Test-case #2
if f.add(0, 10) == 10:
    print('add(0, 10) == 10. Test passed!')
else:
    raise ValueError("add(0,10) != 10. Test failed!")  


if f.sub(10,20) == -10:
    print('sub(10, 20) == -10. Test passed!')
else:
    raise ValueError("sub(10,20) != -10. Test failed!")  


if f.mult(1, 10) == 10:
    print('mult(1, 10) == 10. Test passed!')
else:
    raise ValueError("mult(1,10) != 10. Test failed!")  