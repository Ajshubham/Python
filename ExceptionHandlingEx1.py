try:
    num1, num2 = eval(input("Enter two numbers:"))
    result = num1/num2
except ZeroDivisionError:
    print("Zero Divison is not allowed!")
except SyntaxError:
    print("Check your syntax again!")
except:
    print("Wrong Input!")
else:
    print("No Exceptions")
finally:
    print("This will print irrespective of exceptions.")