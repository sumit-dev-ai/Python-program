#Write a program of taking 6 students marks in a sorted manner in a list
m1=int(input("Enter the marks of student 1:"))
m2=int(input("Enter the marks of student 2:"))
m3=int(input("Enter the marks of student 3:"))
m4=int(input("Enter the marks of student 4:"))
m5=int(input("Enter the marks of student 5:"))
m6=int(input("Enter the marks of student 6:"))
list=[m1,m2,m3,m4,m5,m6]
list.sort()
print(list)