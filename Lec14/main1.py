class B:
    b = 10

    def print_me(self):
        print("b from B:", self.b)

class C:
    c = 20

    def print_me(self):
        print("c from C:", self.c)

class D:
    c =  40
class A(D, C, B):
    a = 30
    
    def print_me(self):
        super().print_me() # Обращение к первому родителю, который имеет даннное поле в распоряжении
        B.print_me(self) # Явное обращение к другому классу
        print("a from A:", self.a)

obj_a = A()
print("obj_a.a:", obj_a.a)
print("obj_a.b:", obj_a.b)
print("obj_a.c:", obj_a.c)

obj_a.print_me()