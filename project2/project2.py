import random
randnumber= random.randint(1,100)
#print(randnumber)
gussednumber=None
guess=0
while(gussednumber!=randnumber):
    gussednumber=int(input("enter your guess"))
    if(randnumber==gussednumber):
        print("your guess is right")
    else:
        if(randnumber>gussednumber):
            print("enter the greater number")
        else:
            print("enter the lower number")
    guess =guess+1
print(f"you guessed the number in {guess} guesses")
with open("highscore.txt","r") as f:
    a=int(f.read())
    print(f"the privous high score was{a}")
with open("highscore.txt","w") as f:
    if(guess<a):
        f.write(str(guess))
        