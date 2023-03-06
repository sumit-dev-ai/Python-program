#the game function is a program lets a user play a game and returns the score as an integer you need to read a file 
#hiscore.txt which is either blank or contains the previous high score you need to write a program to update the hiscore wheather game breaks the highscore

def game():
    return 44
score=game()
f=open("highscore.txt","r") 
hiscore=f.read()
if hiscore=="":
    f=open("highscore.txt","w") 
    f.write(str(score))
    f.close()

elif int(hiscore)<score:
    f=open("highscore.txt","w") 
    f.write(str(score))
    f.close()
