from filecmp import cmp
import random
print("\n")
print("---------WELCOME TO ROCK PAPER SCISSORS----------")
print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer!")
print("\n")

#initialising the user's score and computer' score to 0
computer_score = 0
user_score = 0

#running an infinite loop until the user asks to quit
while True:

    print("Press S to start and Q to quit")
    ch = str(input())

    #if user wants to quit, display the final score and quit
    if ch.lower()=='q':
        print("The computer score is: ", computer_score)
        print("The user's score is: ", user_score)
        break
    
    else:
        computer_choice = ["rock", "paper", "scissors"]
        print("\n")
        print("Enter your move!")
        #user makes a move

        move = str(input())

        cmp_num = random.randint(0,2)
        #getting a random index value to access the computer's choice

        #computer choice and user choice is the same.
        if move.lower()==computer_choice[cmp_num]:
            print("Try again")
        
        #user's move is rock
        elif move.lower() == "rock":
            #computer puts paper hence computer wins and score of computer increases by 1
            if computer_choice[cmp_num] == "paper":
                computer_score+=1
                print("The computer choice is: ", computer_choice[cmp_num])
                print("Computer Wins")
                print("\n")
            #computer puts scissors in which case the user wins 
            else:
                user_score+=1
                print("The computer choice is: ", computer_choice[cmp_num])
                print("You Win")
                print("\n")
        #users move is paper 
        elif move.lower() == "paper":
            #since comp has put scissors it means the comp has won
            if computer_choice[cmp_num] == "scissors":
                computer_score+=1
                print("The computer choice is: ", computer_choice[cmp_num])
                print("Computer Wins")
                print("\n")
            else:
                user_score+=1
                print("The computer choice is: ", computer_choice[cmp_num])
                print("You Win")
                print("\n")
        #users move is scissors 
        else:
            if computer_choice[cmp_num] == "rock":
                computer_score+=1
                print("The computer choice is: ", computer_choice[cmp_num])
                print("Computer Wins")
                print("\n")

            else:
                user_score+=1
                print("The computer choice is: ", computer_choice[cmp_num])
                print("You Win")
                print("\n")
