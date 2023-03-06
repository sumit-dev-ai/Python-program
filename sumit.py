n=int(input())
result=[]
grade=[]
for i in range(n):
    name=input()
    marks=float(input())
    result.append([name,marks])
    grade.append(marks)
m=sorted(set(grade))
s=m[1]
nm=[]
for val in result:
    if s==val[1]:
        nm.append(val[0])
nm.sort()
for name in nm:
    print(nm)