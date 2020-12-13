a_list = [0] * 10000
print("A_list Original size:", a_list.__sizeof__(), "Bytes")

for i in range(len(a_list.copy())):
    if i% 100 == 0:
        print("Current size on iteration #", i, a_list.__sizeof__(), "Bytes")

    del a_list[0]
