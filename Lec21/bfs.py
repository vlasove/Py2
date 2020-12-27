"""
Инициализация графа
"""
class Person:
    def __init__(self, name:str):
        self.name = name 
    hasCyberpunk = False # есть ли у персоны киберпанк? 
    visited = False  # спрашивали ли у этого персонажа, есть у него киберпанк?

p = Person("Me")
p1 = Person("Vitya")
p2 = Person("Petya")
p2.hasCyberpunk = True 
p3 = Person("Marina")
p4 = Person("Zalina")
p5 = Person("Nikolay")
p6 = Person("Fedya")
p6.hasCyberpunk = True 

def check(p:Person):
    return p.hasCyberpunk

# Наш граф
graph = {
    p : [p1, p2],
    p1 : [p3],
    p2 : [p3, p4, p5],
    p3 :[],
    p4 : [],
    p5 : [p4, p6],
    p6 : [],
}

def bfs(graph, start_Person:Person, check):
    """
    graph - словарь, реализующий граф
    start_Person - персона, с который мы начинаем опрашивать
    check - функция, которая првоеряет, есть ли у персоны киберпанк или нет
    """
    # Очередь проверки персон
    queue = [] 
    # Добавляем себя в очередь проверок
    queue.append(start_Person)
    # Помечаем себя как проверенного
    start_Person.visited = True 
    # Проверка, есть ли у нас киберпанк?
    if check(start_Person):
        return start_Person
    
    # Пока очередь не пуста
    while len(queue) > 0:
        # Снимаем первый элемент из очереди
        current_Person = queue.pop(0)
        # Перебираем всех друзей текущей персоны
        for neighbor in graph[current_Person]:
            # Если у друга не спрашивали про киберпанк
            if (not neighbor.visited):
                # Добавляем в очередь проверок 
                queue.append(neighbor)
                # Помечаем его, что мы тут спрашивали
                neighbor.visited = True 

                # Проверяем, есть ли у этого дружка киберпанк?
                if (check(neighbor)):
                    # Если есть - возвращаем его
                    return neighbor
    # В случае, если мы перебрали весь граф и ничего не нашли - отдаем None
    return None


personWithCyberPunk2077 = bfs(graph, p, check)
if personWithCyberPunk2077 is not None:
    print("Name:", personWithCyberPunk2077.name)