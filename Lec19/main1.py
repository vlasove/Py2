import collections
d = collections.defaultdict(int)
d["one"] = 1
d["two"] = 2
d["three"]
print(d)
d["three"] = 3
print(d)

for key, val in d.items():
    print(key, val)