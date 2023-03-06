import numpy as np
list=[]
for i in range(1,10):
    data=int(input())
    list.append(data)
arr=np.array(list)
print(np.reshape(arr,(3,3)))