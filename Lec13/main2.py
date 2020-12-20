class A:
    shape = 20
    a = -30


class B(A):
    b = 40
    shape = 100 # Происходит переопределение родительского поля

obj_a = A()
obj_b = B()

print("Info about obj_a", obj_a.a, obj_a.shape)
print("Info about obj_b:", obj_b.a, obj_b.shape, obj_b.b)


