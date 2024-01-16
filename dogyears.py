#first i define the function dog_year_converter
#with years this is where the user inputted value is stored

def dog_year_converter(years):
    years = int(human_years)

#if the value inputted is 0 or less 
#it will return with a message prompting the user to input a value larger than 0
    if years < 0:
        return 'Value must be larger than 0'

#if the value inputted is greater than 0, the programme returns years (the user inputted value) and multiplies it by 7
    return years*7

#starts with asking the user to input their dogs age, with a valid intiger and greater than 0
#the final result is the dogs age in dog years from the inputted human years.
human_years = input('Enter your dogs age in human years: ')
print(dog_year_converter(2))

#e.g 7, the result will be 49