import collections
word = ["bob","fedya", "alice" , "cat", "dog", "bob", "alice", "fedya", "bob"]
counter = collections.Counter(word) # На вход Counter() можно скормить ЛЮБОЙ ИТРЕИРУЕМЫЙ ОБЪЕКТ
print(counter)
print("bob:", counter["bob"])

print("Elements:", list(counter.elements()))

print("Top 2 words:", counter.most_common(3))

# Сходство с нижележащим словарем
for key, val in counter.items():
    print(key, val)