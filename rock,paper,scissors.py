#first I import 'random'
import random 

#next I set both the user_wins & computer_wins to 0 in their own variables so they both start out equal.
user_wins = 0
computer_wins = 0

#here are the options the user can pick from.
options = ["rock", "paper", "scissors"]

#the programme will ask if the user would like to pick one of the 3 options by typying in
#rock, paper or scissors. if they want to quit they can simply type in the letter 'q' at any time and the programme will end.
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

# using the while True loop, the programme will continue asking the user to input an option until they quit.
    if user_input not in options:
        continue

#random will run through the 3 options and randomly generate the result for the computers pick.
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

#where the inputs match and if they are matches the user will have won that round.
#else, they will have lost it and the point for that round will go to the computer instead.
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        
    else: 
        print("You lost!")
        computer_wins += 1

#at the end the programme will tally up all the points and give the user the results.
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")