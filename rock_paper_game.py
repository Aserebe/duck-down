import random
#c=['r','p','s']
comp=random.choice( ['r', 'p', 's'] )
#comp=random.rand(c)
user=input("enter r for rock ,p for paper and s for scissors:")
print("the computer's choice is:",comp)
if(comp==user):
    print("its a tie")
elif (comp=="r" and user=='s'):
    print("comp won")
elif (comp=="s" and user=='p'):
    print("comp won")
elif (comp=="p" and user=='r'):
    print("comp won")
else:
    print("user won")
    

    
    
