S={1,8,3,2,4}
print(len(S))   # prints length of set

S.remove(8)             #removes 8 from list
print(S)

S.add(7)
print(S)

S.pop()             #Removes an item from set
print(S.pop())      #removes an item from set and prints the value which is deleted
print(S)

# S.clear()   deletes all elements of set
print(S.union({8,11,19}))                   #union of set but it doesnt add it in original set as you can see in print function given below
print(S)
print(S.intersection({3,4}))