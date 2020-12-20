class A:
    a = 10 
    def print_me(self):
        print("a from A:", self.a)

class B(A):
    b = 20
    def print_me(self):
        print("b from B:", self.b)

class C(A):
    c = 30
    

class D(C, B):
    d = 40


d = D() 
d.print_me()