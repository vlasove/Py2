def description(**kwargs):
    """
    Континуальный аругмент с ключевыми словами
    """
    print(kwargs)
    print(type(kwargs))


description(a = 10, b= 20, c = 30)