class book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        print(type(total))
        return total
b1=book("A",300)
b2=book("B",500)
print("Total pages are :",b1+b2)

    
