s = input("Enter a string: ")
s.lower()
d = {}
l = s.split()
for word in l:
    d[word] = d.get(word)
print("Unique Words:\n")
for word in d:
    print(word,end=' ')