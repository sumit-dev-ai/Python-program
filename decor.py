def decor(addition):
    a=addition()+int(input("Enter Third number:"))
    print(a)


def addition():
    num1= int(input("Enter first number : "))
    num2= int(input("Enter Second number : "))
    result=num1+num2
    return result

addition=decor(addition)
