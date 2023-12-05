"""
NOTES:
    In order to run the package in the terminal, please make sure the four modules: 
    ingredients_management.py, inverntory_check.py, adding_additional_items.py, 
    finalize_list.py and test_usage.py are in the same file. 
"""

from adding_additional_items import AddingAdditionalItems
from finalize_list import FinalizeList
from ingredients_management import RecipeManager
from inventory_check import InventoryChecker


## Step 1: Manage Recipes and Ingredients
## This step involves managing recipes, including adding(changing) a new recipe and its ingredients.

print("==== Step 1: Recipe and Ingredients Management ====")

# Creating an instance of RecipeManager
recipe_manager = RecipeManager()

# Prompting the user to input a new recipe name
# Ex: enter "fried rice"
recipe_manager.add_recipe() 

# Asking for the recipe name to add ingredients
# Ex: enter "fried rice"
recipe_name = input("Which recipe do you want to add ingredients to? : ")

# Adding/chaning ingredients to the specified recipe
# Ex: Let's make a simple fried rice, so enter "rice, egg, oil" one by one, then enter "done".
recipe_manager.add_ingredients_to_recipe(recipe_name)

# Choosing and displaying ingredients for the chosen recipe
# Ex: enter "fried rice", it will show you all the ingredients you need
recipe_manager.choose_recipe()



## Step 2: Check Inventory
## In this step, the script checks the user's inventory against the required ingredients for the selected recipe.

print("\n==== Step 2: Inventory Check ====")

# Retrieving ingredients of the selected recipe
selected_recipe_ingredients = set(recipe_manager.recipes[recipe_name])

# Creating an InventoryChecker instance
inventory_checker = InventoryChecker(selected_recipe_ingredients)
    
# Asking the user to confirm the presence of each ingredient in their inventory
# Ex: I only have oil at home, so enter "no" for "egg" and "rice", enter "yes" for "oil".
for ingredient in selected_recipe_ingredients:
    inventory_checker.ask_for_existing_ingredient(ingredient)
    
# Generating a shopping list based on missing ingredients
shopping_list = inventory_checker.finalize_inventory_check()



## Step 3: Manage Shopping List
## This step allows the user to add any additional items to the shopping list.

print("\n==== Step 3: Adding Additional Items ====")

# Creating an instance to manage additional items
additional_items = AddingAdditionalItems(list(shopping_list))

# Ex: I may want some wine pair with the fried rice lol. so I will enter "yes" first, then enter "wine",
#     and it will show you the "to buy list" which is "egg, rice, wine". You can keep add something you need.
while True:
    # Looping to allow the user to continuously add items until they choose not to
    if additional_items.item_addition_inquiry():
        new_item = input("Enter the new item: ")
        additional_items.updated_list(new_item)
    else:
        # Breaking the loop when the user is done adding items
        break



## Step 4: Finalize Shopping List
## The final step involves finalizing the shopping list by crossing out items already bought.

print("\n==== Step 4: Finalize Shopping List (Time to go to the supermarket!) ====")

# Creating an instance to finalize the shopping list
final_list = FinalizeList(additional_items.shopping_list)

# Ex: I got everything in the supermarket, when it asks me what I have got, I enter "egg, rice, wine" then "no" one by one,
#     then it will tell you "All items have been crossed out. Your shopping list is complete!".
while True:
    # Allowing the user to cross out items they have already bought during the shopping
    item_to_remove = input("Enter the item you have already bought (or 'no' to finish): ")
    if item_to_remove == 'no':
        # Exiting the loop when the user indicates they are finished
        break
    # Crossing out the specified item
    final_list.cross_out(item_to_remove)

# Displaying the final list of items still needed    
final_list.list_check()


