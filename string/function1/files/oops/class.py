class StudentForm:
        form="addmison"
        
        def printdata(self):
            print(f"Student name is {self.name}")
            print(f"Student rollno is {self.rollno}")
            print(f"Student year is {self.year}")
 



sumit=StudentForm()
sumit.name="Sumit jindal"
sumit.rollno="2005111530021"
sumit.year="btech 3rd year"
sumit.printdata() 
sumit.form