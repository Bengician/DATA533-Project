# sub-package#1, module 1

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self):
        recipe_name = input("Enter the name of the dish you can cook: ")
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = []
            print(f"Added a new recipe: {recipe_name}")
        else:
            print(f"Recipe '{recipe_name}' already exists.")

    def add_ingredients_to_recipe(self, recipe_name):
        print(f"Enter the ingredients for '{recipe_name}' (one ingredient per line):")
        while True:
            ingredient = input("Enter an ingredient (or enter 'done' when finished): ")
            if ingredient.lower() == 'done':
                break
            self.recipes[recipe_name].append(ingredient)
        print(f"Ingredients for {recipe_name} have been added.")

    def display_ingredients(self, recipe_name):
        if recipe_name in self.recipes:
            ingredients = self.recipes[recipe_name]
            print(f"To cook '{recipe_name}', you will need the following ingredients:")
            for ingredient in ingredients:
                print(f"- {ingredient}")
        else:
            print(f"Sorry, '{recipe_name}' is not in your recipe list.")

    def choose_recipe(self):
        recipe_name = input("Enter the name of the dish you want to cook today: ")
        self.display_ingredients(recipe_name)
