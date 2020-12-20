class A:
    a = 10

class B(A):
    b = 20 


a = A()
b = B()

print(type(a))
print(type(b))

print("a is instance of A:", isinstance(a, A))
print("b is instance of B:", isinstance(b, B))
print("b is instance of A:", isinstance(b, A))
print("a is instance of B:", isinstance(a, B))
print("None is instance of int:", isinstance(None, NoneType))
print(type(None))