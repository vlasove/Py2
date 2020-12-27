class Stack:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()


books = Stack()
books.push("Fluent Python")
books.push("Learning SQL")
books.push("Linux")

while not books.isEmpty():
    current_book = books.pop()
    print("Now I'm reading book:", current_book)



int(input().split()[0])
