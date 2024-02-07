# Task
# You are given a string.
# Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Output Format

# In the first line, print True if
# has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if has any alphabetical characters. Otherwise, print False.
# In the third line, print True if has any digits. Otherwise, print False.
# In the fourth line, print True if has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if has any uppercase characters. Otherwise, print False. 
if __name__ == '__main__':
    s = input()
    has_lower, has_upper, alpha, digit, alnum = False, False, False, False, False
    
    for a in range(len(s)):
        if s[a].isalnum():
            alnum = True
            break
        
    for a in range(len(s)):
        if s[a].isalpha():
            alpha = True
            break
        
    for b in range(len(s)):
        if s[b].isdigit():
            digit = True
            break
        
    for x in range(len(s)):
        if s[x].islower():
            has_lower = True
            break
        
    for y in range(len(s)):
        if s[y].isupper():
            has_upper = True
            break
     
    print(alnum)
    print(alpha)
    print(digit)
    print(has_lower)
    print(has_upper)
