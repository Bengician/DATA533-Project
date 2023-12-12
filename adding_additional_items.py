# sub-package#2, module 1

class AddingAdditionalItems:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def list_preview(self):
        print("Your current shopping list:")
        for item in self.shopping_list:
            print(f"- {item}")

    def item_addition_inquiry(self):
        item = input("Would you like to add an item to your shopping list? (yes/no) ")
        return item.lower() == 'yes'

    def updated_list(self, new_item):
        self.shopping_list.append(new_item)
        self.list_preview()