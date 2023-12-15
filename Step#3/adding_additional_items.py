# sub-package#2, module 1

class AddingAdditionalItems:
    def __init__(self, shopping_list):
        try:
            if not isinstance(shopping_list, list):
                raise TypeError("shopping_list must be a list.")
                
            self.shopping_list = shopping_list
        except TypeError as te:
            print(f"Error initializing AddingAdditionalItems: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def list_preview(self):
        try:
            print("Your current shopping list:")
            for item in self.shopping_list:
                print(f"- {item}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def item_addition_inquiry(self):
        try:
            item = input("Would you like to add an item to your shopping list? (yes/no) ")
            return item.lower() == 'yes'
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def updated_list(self, new_item):
        try:
            self.shopping_list.append(new_item)
            self.list_preview()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")