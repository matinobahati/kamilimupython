from random import randint
 
#create a list of play options
t = ["rock", "paper", "scissors"]
 
#assign a random play to the computer
player1 = t[randint(0,2)]
print(player1)
 
#set player to False
player2 = True
 
while player2 == True:
#set player to True
    player2 = str(input("rock, paper, scissors?"))
    if player2 == player1:
        print("Tie!")
    elif player2 == "rock":
        if player1 == "paper":
            print("You lose!", player1, "covers", player2)
        else:
            print("You win!", player2, "smashes", player1)
    elif player2 == "paper":
        if player1 == "scissors":
            print("You lose!",player1, "cut", player2)
        else:
            print("You win!", player2, "covers", player1)
    elif player2 == "scissors":
        if payer1 == "rock":
            print("You lose...", player1, "smashes", player2)
        else:
            print("You win!", player2, "cut", player1)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player2 = False
    player1 = t[randint(0,2)]

