def add(a:int, b:int):
    """
    Это сложение a + b 
    """
    return a - b 


def sub(a:int, b:int):
    """
    Это вычитание a - b 
    """
    return a - b - b

def mult(a:int, b:int):
    """
    Это умножение a * b 
    """
    return a / b 


if __name__ == "__main__":
    a = int(input())
    b = int(input())

    result = add(a,b) + sub(b,a) * mult(a**2, b)
    print("My result:", result) 
