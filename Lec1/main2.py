"""
Коллекции
1) set()
2) str()
3) list()
4) tuple()
5) dict()
"""

# Множество set()
a_set = set([1,2,3,4])
b_set = set([3, 4, 5, 6])

print("Intersection:", a_set.intersection(b_set))
print("Union:", a_set.union(b_set))
print("Difference A - B:", a_set.difference(b_set))
print("Symmetric Diff A^B:", a_set.symmetric_difference(b_set))

# Строки str()
word1 = "a"
word2 = "A"
print(word2 > word1)
print("A ordinal:", ord("A"))
print("a ordinal:", ord("a"))

word1 = "aaaa"
word2 = "aa"

print(word1 > word2)


# Списки list() и кортежи tuple()
lst = [10, 20, 30]
lst[0] = 2000
tpl = (20,) + (10,)

print("List:", type(lst), lst)
print('Type:', type(tpl), tpl)

# Сортировка с изменением состояния
nums = [10, 3, 4, -2, 200, 3, 4, -100, 1]
snums = sorted(nums)
#nums.sort()
print("Oririn:", nums)
print("Sorted:", snums)

# Словари dict()
"""
Что можно использовать в качестве ключа? Любой неизменяемый тип.
Ключи должны быть УНИКАЛЬНЫМИ.
"""

d = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
}

d["four"] = 4

# Перебор ключей
for key in d.keys():
    print("Key:", key)

for val in d.values():
    print('Val:', val)

for key, val in d.items():
    print("Key:", key, "Val:", val)

