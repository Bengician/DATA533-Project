# sub-package#2, module 2

class ShoppingListBase:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def display_shopping_list(self):
        print("Your current shopping list:")
        for item in self.shopping_list:
            print(f"- {item}")

class FinalizeList(ShoppingListBase):
    def sorted_list(self):
        return sorted(self.shopping_list)

    def cross_out(self, item):
        #exception_6
        try:
            self.shopping_list.remove(item)
            print(f"{item} has been crossed out from the list.")
        except ValueError:
            print(f"{item} was not in the shopping list.")

    def list_check(self):
        if not self.shopping_list:
            print("All items have been crossed out. Your shopping list is complete!")
        else:
            print("The following items are still on the list:")
            for item in self.shopping_list:
                print(f"- {item}")