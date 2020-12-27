a = {"one" : 1, "two" : 2}
b = {"three" : 3, "four" : 4}
c = {"five" : 5, "one" : 3}
import collections

totaldict = collections.ChainMap(a, b)
a.pop("one")
totaldict["vova"] = 10
totaldict = totaldict.new_child(c)
for key, val in totaldict.items():
    print(key, val)

print(totaldict["one"])


