#travel modes
travel_mode = {"1": "car", "2": "plane"}

#here we have a list of household items
items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

#here are the restricted items. None of these are allowed on a plane (option 2) 
#so they will not be present in the "need to pack" list. 
#However in car travel (option 1) items such as scissors and shampoo are okay to take
restricted_items = {
    "catapult",
    "fuel",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

#asks the user which form of travel they are taking.
print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")

#makes the user input a valid option or the programme won't run
mode = "-"
while mode not in travel_mode:
    mode = input("> ")

# travelling by plane, remove restricted items
if mode == "2":
    # for restricted_items in restricted_items:
    #     items.discard(restricted_items)
    #     #'.remove' would give an error here.
    #     items -= restricted_items
    items.difference_update(restricted_items)

# prints the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)
