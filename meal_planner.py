#from the contents file we import the pantry section which includes all of the ingredients we currently have.
#and from the recipes section which tells us the exact ingredients we need to make a meal.
from contents import pantry, recipes

#data = dictionary, item = string, amount = int -> = returns the arguments 
def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """add a tuple containing item & amount to the data dict"""
    #set default method
    data[item] = data.setdefault(item, 0) + amount


#display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
#enumerate allows the programme to loop
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    #display a menu of recipies we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

#user selects their choice by inputting the correct alocated number
    choice = input(": ")

    #0 exits the programme                                                                                                
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        #returns to the user confirmation of what they have selected
        print(f"You have selected {selected_item}")
        print("Checking ingredients...")
        
        #prints out the recipe and what the user needs to create the meal
        #if they have the ingredients they need in their pantry, the programme will return the word "ok".
        #if they do not have the ingredients they need in their pantry, 
        #the programme will tell them the item and the quantity they need to buy.
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK") #tab
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)