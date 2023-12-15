# sub-package#2, module 1

class AddingAdditionalItems:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def list_preview(self):
        print("Your current shopping list:")
        for item in self.shopping_list:
            print(f"- {item}")

    def item_addition_inquiry(self):
        #exception_4
        try:
            item = input("Would you like to add an item to your shopping list? (yes/no) ").strip().lower()
            if item not in ['yes', 'no']:
                raise ValueError("Invalid response. Please answer 'yes' or 'no'.")
            return item == 'yes'
        except ValueError as e:
            print(e)
            return False

    def updated_list(self, new_item):
        #exception_5
        try:
            if not new_item.strip():
                raise ValueError("Item cannot be empty.")
            self.shopping_list.append(new_item.strip())
            self.list_preview()
        except ValueError as e:
            print(e)
