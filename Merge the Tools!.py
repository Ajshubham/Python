def merge_the_tools(string, k):
    if k<= 0 or len(string) % k != 0:
        return 0
    distinct = set()
    result = ""
    for i in range(len(string)):
        word = string[i]
        if word not in distinct:
            distinct.add(word)
            result += word
        if (i+1) % k == 0:
            print(result)
            distinct.clear()
            result = ""
