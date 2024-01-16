#weight = where the user will put in the number of the weight they which to convert
weight = int(input("Weight: "))

#after inputting their number, the programme will ask whether the weight they are inputting is Kilograms or Pounds.
#this is for the original input.
unit = input("(K)g or (L)bs: ")

#if the user inputted "K" or "k" (doesn't matter as I used .upper() here) the weight will be devided by 0.45
#the message would concatinate both the message "weight in Lbs" with the converted int to string result.
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))

#else, is where the user has inputted "L" or "l" for pounds, the inputted weight will be multiplied by 0.45
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))