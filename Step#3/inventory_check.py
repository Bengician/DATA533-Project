# sub-package#1, module 2

class InventoryChecker:
    def __init__(self, recipe_ingredients):
        try:
            if not isinstance(recipe_ingredients, list):
                raise TypeError("recipe_ingredients must be a list.")
                
            self.inventory = recipe_ingredients.copy()
        except TypeError as te:
            print(f"Error initializing InventoryChecker: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def ask_for_existing_ingredient(self, ingredient):
        try:
            if not isinstance(ingredient, str):
                raise TypeError("Ingredient must be a string.")
            
            response = input(f"Do you already have {ingredient}? (yes/no): ")
            
            if response.lower() == 'yes':
                if ingredient in self.inventory:
                    self.inventory.remove(ingredient)
                    print(f"Removed {ingredient} from the shopping list.")
                else:
                    print(f"You don't have {ingredient} in your shopping list.")
        except TypeError as te:
            print(f"Error checking existing ingredient: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def finalize_inventory_check(self):
        try:
            return self.inventory
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_shopping_list(self):
        try:
            if self.inventory:
                print("You need to buy the following ingredients:")
                for item in self.inventory:
                    print(f"- {item}")
            else:
                print("You have all the ingredients you need!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")