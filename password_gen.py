#first I import the random method. 
#This is what gives the programme the ability to pick the following numbers, letters and symbols at completely random order.
import random

#this is where all the lower case letters are stored and picked from
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"

#this is where all the upper case letters are stored and picked from
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#here is where the numbers are stored and picked from
every_number = "1234567890"

#where all the symbols are stored and picked from. It is more and more important to create random, difficult-to-guess passwords.
#using symbols in a password can make it far tougher for anyone to guess.
every_symbol = "!£$%^&*()_-+=[];:'@#<>.,?/"

#here I combine all the variables & characters
combined = lower_case_letters + upper_case_letters + every_number + every_symbol

#here the user inputs what length they want their password to be
password_len = int(input("Please enter exactly how long you want your password to be: "))

#using .join and random.sample in conjunction with all the combined numbers, letters and symbols + the users chosen length
#a completly new random password will be generated. the user then can simply copy and paste what has been given to them.
new_password = "".join(random.sample(combined, password_len))
print("Here is your new randomly generated password:", new_password)

#I placed quit here just so the programme does not continue looping/running
quit