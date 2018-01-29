import random
count=0 #gives the initial value of your coins
print("welcome to snake and ladder game")
while (count<=100): #using while condition
    print("player 1's turn")
    player1=input("Press r to roll a dice:")
    if (player1=='r'):
        r=random.randint(1,6)#selects any random number from1 to 6
        count=count+r
    print("You're current position is",count)
    print ("The dice value ",r)
    print("player2's turn")
    player2=input("Press s to roll a dice:")
    if (player2=='s'):
        s=random.randint(1,6)#selects any random number from1 to 6
        count=count+s
    print("You're current position is",count)
    print ("The dice value ",s)
    #the given if conditions checks where the player climbs the ladder
    #and where he gets bitten by the snake
    if (count==8):
        count=37
        print("you have climbed the ladder")

    if (count==11):
        count=2
        print("oops the snake bit you")
    
    if (count==13):
        count=34
        print("you have climbed the ladder")
    
    if (count==25):
        count=4
        print("oops the snake bit you")
    
    if (count==38):
        count=9
        print("oops the snake bit you")
    
    if (count==40):
        count=68
        print("you have climbed the ladder")
    
    if (count==52):
        count=81
        print("you have climbed the ladder")

    if (count==65):
        count=46
        print("oops the snake bit you")
   
    if (count==76):
        count=97
        print("you have climbed the ladder")
   
    if (count==89):
        count=70
        print("oops the snake bit you")

    if (count==93):
        count=64
        print("oops the snake bit you")
        
if (count>=100):
    print("player1 wins")
    
        

    
