s = input("Enter a string")
l = s.split()
d = {}
for word in l:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for key in d:
    print(key, d[key])