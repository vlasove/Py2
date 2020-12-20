def mult(*args, **kwargs):
    print(args)
    print(kwargs)


mult(1,2,3, 10, 20, 1, q = 400, d = 20)