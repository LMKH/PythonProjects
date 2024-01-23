#import random is used to generate a random number
import random

#in 'highest', insert the number which is highest in your guessing range.
#e.g. 10, the random module will generate a number between 1 and 10, nothing higher.
#you can decide whatever number you wish.
highest = 10

#answer = is the random generated number chosen by the random module. between 1 and the highest chosen number.
answer = random.randint(1, highest)

#if you want to see the number the programme has chosen, uncomment print(answer). This will reviel the answer. 
#print(answer)

#initialise to any number that dosent = the answer
guess = 0

#will loop until the user gets the correct number.
#will ask the user to input a number
#.format(highest) takes the number you have put in the 'highest' variable. again between 1 and ...
print("Please guess a number between 1 and {}: ".format(highest))

#while the users answer is not the random modules chosen number it will keep asking the user to input a number
while guess != answer:
    guess = int(input())

#0 = exit the programme
    if guess == 0:
        break

    #if the user guesses the correct answer, this message will appear and the programme will stop.
    if guess == answer:
        print("Well done, you got it right! So smart!")
        break

    #if the users guess is lower than the chosen number, it will ask the user to "guess higher"
    else:
        if guess < answer:
            print("Please guess higher")
        #if the users guess is higher than the chosen number, it will ask the user to "guess lower"
        else:
            print("Please guess lower")