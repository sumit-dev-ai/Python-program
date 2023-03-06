List=[1,45,3,2,32]

List.sort()                                 #It  will  sort  the  list                 [1,2,3,32,45]
print("List after sorting",List)            

List.reverse()                              #it  will  reverse  the  list              [45,32,3,2,1]
print("\nlist after reversing",List)        

List.append(8)                              #it will add 8 in the end of list          [45,32,3,2,1,8]
print("\nlist after adding 8 in last",List) 

List.insert(3,8)                            #It  will 8  at  index  3                  [45,32,3,8,2,1,8]     
print("\n8 at index 3",List)

List.pop(2)                                 #It  will pop data from index 2            [45,32,8,2,1,8]
print("\npop data from index 2",List)       

List.remove(45)                             #It will remove 45 from list               [32,8,2,1,8]
print("\nremove 45 from list",List)