letter='''Dear <|NAME|>
You are Selected
Date: <|DATE|>'''

name=input("Enter name\n")
date=input("Enter date\n")

letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)