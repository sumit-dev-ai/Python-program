letter='''Name: <|NAME|>
Date:<|DATE|>
Dear <|NAME|>, You are selected for job in our company
you can join here by this month'''
name=input("Enter Your Name;")
date=input("Enter Date;")
letter=(letter.replace("<|NAME|>",name))
letter=(letter.replace("<|DATE|>",date))
print(letter)