# sub-package#1, module 1

class RecipeNotFoundException(Exception):
    def __init__(self, message="Recipe not found"):
        self.message = message
        super().__init__(self.message)

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self):
        #exception_1
        try:
            recipe_name = input("Enter the name of the dish you can cook: ").strip()
            if not recipe_name:
                raise ValueError("Recipe name cannot be empty.")
            if recipe_name not in self.recipes:
                self.recipes[recipe_name] = []
                print(f"Added a new recipe: {recipe_name}")
            else:
                print(f"Recipe '{recipe_name}' already exists.")
        except ValueError as e:
            print(e)

    def add_ingredients_to_recipe(self, recipe_name):
        #exception_2 (user-defined exception)
        try:
            if recipe_name not in self.recipes:
                raise RecipeNotFoundException(f"'{recipe_name}' does not exist in your recipe list.")
            print(f"Enter the ingredients for '{recipe_name}' (one ingredient per line)")
            while True:
                ingredient = input("Enter an ingredient (or enter 'done' when finished): ")
                if ingredient.lower() == 'done':
                    break
                if not ingredient.strip():
                    raise ValueError("Ingredient cannot be empty.")
                self.recipes[recipe_name].append(ingredient.strip())
            print(f"Ingredients for {recipe_name} have been added.")
        except RecipeNotFoundException as e:
            print(e)
        except ValueError as e:
            print(e)

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


