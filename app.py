# Step 1: Display a welcome message
print("Welcome to Mad Libs Game!")
print("Answer the questions below to create your own funny story.")
print("-" * 50)

# Step 2: Collect input from the user
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb (action word): ")
food = input("Enter a food item: ")

# Step 3: Create the story template
story = f"""
Once upon a time, there was a person named {name}.
{name} lived in a {adjective1} town called {place}.
One day, a {adjective2} {animal} appeared and started to {verb} everywhere!
Everyone ran and hid, except {name}, who offered the {animal} some {food}.
The {animal} loved it and became friends with the town.
And they all lived happily ever after!
"""

# Step 4: Show the final story
print("\nHere is your Mad Libs story:")
print(story)
