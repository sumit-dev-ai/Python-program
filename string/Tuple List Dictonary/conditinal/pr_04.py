print("             *****Username must not contain more than 10 words*****                                 ")
username=input("Enter you username: ")

if(len(username)>10):
    print("Invalid user name")
else:
    print("Enter your password to login to website")