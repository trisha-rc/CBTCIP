import random
print("Rock Paper Scissor Game\n")
print("Winning Rules as follows:\nRock vs Paper-> Paper wins\nRock vs Scissor-> Rock wins\nPaper vs Scissor-> Scissor wins\n")
while True:
    print("Choices for the user:\n1. Rock\n2. Paper\n3. Scissor\n")
    user_choice=int(input("Enter 1 or 2 or 3 as per your choice:"))
    if user_choice==1:
        uc='Rock'
    elif user_choice==2:
        uc='Paper'
    elif user_choice==3:
        uc='Scissor'
    else:
        uc='nothing'
        print("Wrong choice")
        continue
    print("You have chosen",uc)

    print("\nNow it is Computer's turn to choose...")
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        cc='Rock'
    elif comp_choice==2:
        cc='Paper'
    elif comp_choice==3:
        cc='Scissor'
    print("The Computer has chosen",cc)

    print("\n",uc," vs ",cc)
    if user_choice==comp_choice:
        result='Draw'
    elif user_choice==1 and comp_choice==2:
        result=cc
    elif user_choice==1 and comp_choice==3:
        result=uc
    elif user_choice==2 and comp_choice==3:
        result=cc
    elif user_choice==2 and comp_choice==1:
        result=uc
    elif user_choice==3 and comp_choice==1:
        result=cc
    elif user_choice==3 and comp_choice==2:
        result=uc

    print()
    if result==cc:
        print(result," wins")
        print("Computer is the winner")
    elif result==uc:
        print(result," wins")
        print("You are the winner")
    else:
        print("Game drawn")

    print("\nEnter y to play again or enter n to exit the game")
    x=input("Do you want to play again?")
    if x=='y':
        continue
    elif x=='n':
        print("Exit game")
        break
    else:
        print("Invalid entry")
        break





