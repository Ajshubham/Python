def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

num = int(input("Enter a number: "))
sum = 0
temp = num
while num > 0:
    digit = num % 10
    sum = sum + fact(digit)
    num = num // 10
if temp == sum:
    print(str(temp)+" is strong number.")
else:
    print(str(temp)+ " is not strong number.")