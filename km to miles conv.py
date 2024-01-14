#asks the user to input the number of kilometers they wish to convert into miles.
kilometres = int(input("Enter the number of kilometres you want to convert: "))

#once they have correctly inputted a number, the number will be rounded and divided by 1.609
miles = round(kilometres / 1.609, 2)

#finally it will print out the message below, with the conversion from Kilometres to Miles.
print(kilometres, "kilometres converts to", miles, "miles.")