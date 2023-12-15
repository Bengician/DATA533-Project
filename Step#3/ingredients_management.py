# sub-package#1, module 1

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self):
        try:
            recipe_name = input("Enter the name of the dish you can cook: ")
            if not recipe_name:
                raise ValueError("Recipe name cannot be empty.")
            
            if recipe_name in self.recipes:
                raise ValueError(f"Recipe '{recipe_name}' already exists.")
            
            self.recipes[recipe_name] = []
            print(f"Added a new recipe: {recipe_name}")
        except ValueError as ve:
            print(f"Error adding recipe: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def add_ingredients_to_recipe(self, recipe_name):
        try:
            if not recipe_name:
                raise ValueError("Recipe name cannot be empty.")
            
            if recipe_name not in self.recipes:
                self.recipes[recipe_name] = [] 

            print(f"Enter the ingredients for '{recipe_name}' (one ingredient per line)")
            while True:
                ingredient = input("Enter an ingredient (or enter 'done' when finished): ")
                if not ingredient:
                    raise ValueError("Ingredient cannot be empty.")
                
                if ingredient.lower() == 'done':
                    break
                self.recipes[recipe_name].append(ingredient)
                
            print(f"Ingredients for {recipe_name} have been added.")
        except ValueError as ve:
            print(f"Error adding ingredients: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_ingredients(self, recipe_name):
        try:
            if not recipe_name:
                raise ValueError("Recipe name cannot be empty.")
            
            if recipe_name in self.recipes:
                ingredients = self.recipes[recipe_name]
                print(f"To cook '{recipe_name}', you will need the following ingredients:")
                for ingredient in ingredients:
                    print(f"- {ingredient}")
            else:
                print(f"Sorry, '{recipe_name}' is not in your recipe list.")
        except ValueError as ve:
            print(f"Error displaying ingredients: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def choose_recipe(self):
        try:
            recipe_name = input("Enter the name of the dish you want to cook today: ")
            if not recipe_name:
                raise ValueError("Recipe name cannot be empty.")
            
            self.display_ingredients(recipe_name)
        except ValueError as ve:
            print(f"Error choosing recipe: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
