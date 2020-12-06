words = ["bob", "bub", "alice", "george", "frank", "frenk", "jo", "je"]

words_pairs = [] # [(len(word) , word), (....), (....), ..]
for word in words:
    words_pairs.append((len(word), word))

words_pairs.sort()

words_total = []
for pair in words_pairs:
    words_total.append(pair[1])

print("\n".join(words_total))


print("===================================")
print("\n".join(sorted(words, key = lambda p : (len(p), p))))
