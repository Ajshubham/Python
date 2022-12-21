# Menu Driven Program Example

def p_circle(radius):
    para=2*3.14*radius
    print("ParameterofCircle:",para)

def p_rectangle(height,width):
    para=2*(height+width)
    print("ParameterofRectangle:",para)

def p_square(side):
    para=4*side
    print("ParameterofSquare:",para)

def a_circle(radius):
    area=3.14*radius*radius
    print("AreaofCircle:",area)

def a_rectangle(height,width):
    area=height*width
    print("AreaofRectangle:",area)

def a_square(side):
    area=side*side
    print("AreaofSquare:",area)

#printingthestartingline
print("WELCOME TO A SIMPLE MENSURATION PROGRAM")

#creatingoptions
while True:
    print("\nMAIN MENU")
    print("1.Calculate Parameter")
    print("2.Calculate Area")
    print("3.Exit")
    choice1=int(input("EntertheChoice:"))

    if choice1==1:
        print("\nCALCULATE PARAMETER")
        print("1.Circle")
        print("2.Rectangle")
        print("3.Square")
        print("4.Exit")
        choice2=int(input("Enter the Choice:"))

        if choice2==1:
            radius=int(input("Enter Radius of Circle:"))
            p_circle(radius)

        elif choice2==2:
            height=int(input("Enter Height of Rectangle:"))
            width=int(input("Enter Width of Rectangle:"))
            p_rectangle(height,width)

        elif choice2==3:
            side=int(input("Enter Side of Square:"))
            p_square(side)

        elif choice2==4:
            break

        else:
            print("Oops! Incorrect Choice.")

    elif choice1==2:
        print("\nCALCULATE AREA")
        print("1.Circle")
        print("2.Rectangle")
        print("3.Square")
        print("4.Exit")
        choice3=int(input("Enter the Choice:"))

        if choice3==1:
            radius=int(input("Enter Radius of Circle:"))
            a_circle(radius)

        elif choice3==2:
            height=int(input("Enter Height of Rectangle:"))
            width=int(input("EnterWidthofRectangle:"))
            a_rectangle(height,width)

        elif choice3==3:
            side=int(input("Enter Side of Square:"))
            a_square(side)

        elif choice3==4:
            break

        else:
            print("Oops!IncorrectChoice.")

    elif choice1==3:
        break

    else:
        print("Oops!IncorrectChoice.")