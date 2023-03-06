English=int(input("Enter English marks"))
math=int(input("Enter math marks"))
Hindi=int(input("Enter Hindi marks"))
total=(English+math+Hindi)*100/300
if(total>40 and (English>30 and Hindi >30 and math >33)):
    print("You passed the exam with percentage of ",total)
else:
    print("you failed your total percentage is ",total)