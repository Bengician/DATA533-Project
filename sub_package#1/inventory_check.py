# sub-package#1, module 2

class InventoryChecker:
    def __init__(self, recipe_ingredients):
        self.inventory = recipe_ingredients.copy()

    def ask_for_existing_ingredient(self, ingredient):
        response = input(f"Do you already have {ingredient}? (yes/no): ")
        if response.lower() == 'yes':
            self.inventory.remove(ingredient)
            print(f"Removed {ingredient} from the shopping list.")
            
    def finalize_inventory_check(self):
        return self.inventory

    def display_shopping_list(self):
        if self.inventory:
            print("You need to buy the following ingredients:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("You have all the ingredients you need!")

