from pickle import TRUE
import random # this will randomly chooses things it is an module
print("Com turn :  snake(S),water(W),gun(G)")#this gun(g) is function which helps in game
no=random.randint(1,3)# this is function of random modules
def game(com,you):
    if(com==you):
        return None
    if com=='S':
        if you=='W':
            return False
        elif you=='G':
            return True
    if com=='W':
        if you=='G':
            return False 
        elif you=='S':
            return True
    if com=='G':
        if you=='S':
            return False
        elif you=='W':
            return True        
        
if(no==1):
    com ='S'
elif(no==2):
    com='W'
elif(no==3):
    com='G'
you =input("Com turn :  snake(S),water(W),gun(G)")
winner=game(com,you)
print("your choice",you)
print("com choice",com)
if (winner==None):
    print("the match is tie!")
elif(winner==True):
    print("you won!")
else:
    print("you lose!!")
    