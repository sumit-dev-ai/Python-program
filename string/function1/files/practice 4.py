
f=open("poems.txt")
t=f.read()

t=t.replace("twinke","*****")
with open("poems.txt","w") as f:
    f.write(t)



f=open("poems.txt")
data=f.read()
print(data)


