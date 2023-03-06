a=int(input("Enter your number 1"))
b=int(input("Enter your number 2"))
c=int(input("Enter your number 3"))
d=int(input("Enter your number 4"))

if(a>b):
    num1=a
else:
    num1=b
if(c>d):
    num2=c
else:
    num2=d

if(num1>num2):
    print(str(num1)+" is greather")
else:
    print(str(num2)+" is greather")