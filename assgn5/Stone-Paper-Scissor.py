import random
i=1
count_u=0
count_c=0
while(i<=5):
    i+=1
    print("Enter-\n1 to select Stone\n2 to select Scissor\n3 to select Paper\n-->")
    user=int(input())
    comp=random.randint(1,3)
    if user==1 and comp==2:
        count_u+=1
        print("Comp:I lose this Round :-(")
    elif user==1 and comp==3:
        count_c+=1
        print("Comp:I win this Round :-)")
    elif user==2 and comp==3:
        count_u+=1
        print("Comp:I lose this Round :-(")
    elif user==2 and comp==1:
        count_c+=1
        print("Comp:I win this Round :-)")
    elif user==3 and comp==1:
        count_u+=1
        print("Comp:I lose this Round :-(")
    elif user==3 and comp==2:
        count_c+=1
        print("Comp:I win this Round :-)")
    else:
        print("Comp:Guess....we both chose the same")
    print("Scores:\nUser-",count_u,"\nComputer-",count_c)

print("Result:")
if count_u>count_c:
    print("The User Wins")
elif count_u==count_c:
    print("The game is drawn")
else:
    print("The Computer Wins")
