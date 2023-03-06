class Movie:
    def __init__(self,title,runtime,actor):
        self.title=title
        self.runtime=runtime
        self.actor=actor
    def printer(self):
        print(f"Title is : {self.title}\nRuntime is: {self.runtime}mins\nActor Name: {self.actor}")
        print("------------------------------------------------------------------------------------")
list_of_movies=[]
while True:
    title=input("Title is : ")
    runtime=input("Runtime is : ")
    actor=input("Actor is : ")
    obj=Movie(title,runtime, actor)
    list_of_movies.append(obj)
    print("Movie added into List")
    ch=input("Add another Movie (y/n)")
    if ch!="y":
        break
print("all Movies Details")
print("-----------------------------------------------------------------------------------------")
for obj in list_of_movies:
    obj.printer()






