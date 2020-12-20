def mult(*args):
    """
    Функция перемножающая абсолютно все переданные аргументы
    """
    print(args)
    print(type(args))
    result = 1 
    for elem in args:
        result *= elem 
    #.....
    return result 

print()


mult(10, 20, 30)
mult()
mult(30, 40)
mult(1,1,1,11,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1)