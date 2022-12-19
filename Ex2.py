# Program to count the word frequency in a sentence in decreasing order

s = input("Enter string:")
s = s.lower()
d = {}
for ch in s:
    if ch.isalpha():
        d[ch] = d.get(ch,0)+1
for key,value in sorted(d.items()):
    print(key,value,end='')