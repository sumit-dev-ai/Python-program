# airthmetic operators
from typing import List


a=4
b=5
print("a+b is: ",a+b)
print("a-b is: ",a-b)
print("a*b is: ",a*b)
print("a/b is: ",a/b)

#assignment operators

a=4
a+=2
print(a)
# it will work as a+2
c=5
c-=4
print(c)
c*=5
print(c)

#comparison operators
d=(5>6)
print(d)
d=(7>5)
print(d)

#Logical operator
i=True
j=False
print("i and j:",(i and j))
print("i or j:",(i or j))
print("i not:",( not i ))

#membership operator
a=[5,6,7,8,9]
print(5 in a)
print(5 not in a)
#Identity operator

z=5
print(z is 5)