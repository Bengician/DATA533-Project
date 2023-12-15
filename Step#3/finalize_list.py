# sub-package#2, module 2

class ShoppingListBase:
    def __init__(self, shopping_list):
        try:
            if not isinstance(shopping_list, list):
                raise TypeError("shopping_list must be a list.")
                
            self.shopping_list = shopping_list
        except TypeError as te:
            print(f"Error initializing ShoppingListBase: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_shopping_list(self):
        try:
            print("Your current shopping list:")
            for item in self.shopping_list:
                print(f"- {item}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

class FinalizeList(ShoppingListBase):
    def sorted_list(self):
        try:
            return sorted(self.shopping_list)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def cross_out(self, item):
        try:
            self.shopping_list.remove(item)
            print(f"{item} has been crossed out from the list.")
        except ValueError as ve:
            print(f"Error crossing out item: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_check(self):
        try:
            if not self.shopping_list:
                print("All items have been crossed out. Your shopping list is complete!")
            else:
                print("The following items are still on the list:")
                for item in self.shopping_list:
                    print(f"- {item}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")