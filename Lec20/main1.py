class Queue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def push(self, element):
        self.elements.append(element)

    def popHead(self):
        if not self.isEmpty():
            return self.elements.pop(0)

server = Queue()
server.push("GET 1.1/ users/")
server.push("GET 1.1/ users/vasyan/photo")
server.push("POST 1.1/ users/register")
server.push("GET 1.1/ users/photo/archive?id=20&likes=251")

while not server.isEmpty():
    current_request = server.popHead()
    print("Server currently working with request:", current_request)