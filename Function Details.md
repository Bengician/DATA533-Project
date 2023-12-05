# Recipe Selection Module

This Python module, part of sub-package #1, includes a class named `RecipeManager` that provides functionality for managing recipes. The class has several methods to add and display recipes, add ingredients to recipes, and choose a recipe to cook.

## Class: RecipeManager

### Method: `__init__(self)`

- **Description**: Initializes an instance of the `RecipeManager` class.
- **Attributes**:
  - `recipes`: A dictionary to store recipes, where the keys are recipe names, and the values are lists of ingredients.

### Method: `add_recipe(self)`

- **Description**: Adds a new recipe to the recipe list.
- **User Input**:
  - Takes input for the name of the dish to be added.
- **Logic**:
  - Checks if the recipe already exists in the recipe list.
  - If not, adds the recipe with an empty list of ingredients.
  - Prints appropriate messages based on whether the recipe was added or already exists.

### Method: `add_ingredients_to_recipe(self, recipe_name)`

- **Description**: Allows the user to add ingredients to a specific recipe.
- **Parameters**:
  - `recipe_name`: The name of the recipe to which ingredients will be added.
- **User Input**:
  - Takes input for each ingredient until the user enters 'done.'
- **Logic**:
  - Appends each entered ingredient to the specified recipe's ingredient list.
  - Breaks the loop when the user enters 'done.'
  - Prints a message indicating that ingredients have been added.

### Method: `display_ingredients(self, recipe_name)`

- **Description**: Displays the ingredients for a specific recipe.
- **Parameters**:
  - `recipe_name`: The name of the recipe to display ingredients for.
- **Logic**:
  - Checks if the specified recipe exists in the recipe list.
  - If yes, prints the list of ingredients.
  - If no, prints a message indicating that the recipe is not in the list.

### Method: `choose_recipe(self)`

- **Description**: Allows the user to choose a recipe to cook and displays its ingredients.
- **User Input**:
  - Takes input for the name of the dish the user wants to cook.
- **Logic**:
  - Calls the `display_ingredients` method to show the ingredients for the chosen recipe.

## Example Usage:

```python
# Create an instance of the RecipeManager class
manager = RecipeManager()

# Add a new recipe
manager.add_recipe()

# Add ingredients to the recipe
manager.add_ingredients_to_recipe("Spaghetti Bolognese")

# Display ingredients for a recipe
manager.display_ingredients("Spaghetti Bolognese")

# Choose a recipe and display its ingredients
manager.choose_recipe()
```

# Inventory Check Module

This Python module, part of sub-package #1, includes a class named `InventoryChecker` that provides functionality for checking and displaying a shopping list based on the user's existing inventory.

## Class: InventoryChecker

### Method: `__init__(self, recipe_ingredients)`

- **Description**: Initializes an instance of the `InventoryChecker` class.
- **Parameters**:
  - `recipe_ingredients`: A list of ingredients required for a recipe, typically obtained from a `RecipeManager` instance.

### Method: `ask_for_existing_ingredient(self, ingredient)`

- **Description**: Asks the user if they already have a specific ingredient in their inventory.
- **Parameters**:
  - `ingredient`: The name of the ingredient to inquire about.
- **User Input**:
  - Takes input for whether the user already has the specified ingredient.
- **Logic**:
  - If the user responds 'yes,' removes the ingredient from the shopping list.
  - Prints a message indicating the removal.

### Method: `finalize_inventory_check(self)`

- **Description**: Returns the final shopping list after the user has confirmed their existing inventory.
- **Returns**:
  - A list of remaining items in the shopping list.

### Method: `display_shopping_list(self)`

- **Description**: Displays the shopping list based on the remaining items in the inventory.
- **Logic**:
  - If the inventory is not empty, prints a list of items to buy.
  - If the inventory is empty, prints a message indicating that all required ingredients are available.

## Example Usage:

```python
# Assume recipe_ingredients is obtained from a RecipeManager instance
recipe_ingredients = ["Pasta", "Tomato Sauce", "Cheese", "Garlic"]

# Create an instance of the InventoryChecker class
checker = InventoryChecker(recipe_ingredients)

# Ask the user about existing ingredients
checker.ask_for_existing_ingredient("Pasta")
checker.ask_for_existing_ingredient("Cheese")

# Display the final shopping list
final_shopping_list = checker.finalize_inventory_check()
print("Final Shopping List:")
checker.display_shopping_list()
```

# Adding Additional Items Module

This Python module, part of sub-package #2, includes a class named `AddingAdditionalItems` that provides functionality for previewing, inquiring about, and updating a shopping list by adding additional items.

## Class: AddingAdditionalItems

### Method: `__init__(self, shopping_list)`

- **Description**: Initializes an instance of the `AddingAdditionalItems` class.
- **Parameters**:
  - `shopping_list`: The initial shopping list to be managed.

### Method: `list_preview(self)`

- **Description**: Prints a preview of the current shopping list.
- **Output**:
  - Displays each item in the shopping list.

### Method: `item_addition_inquiry(self)`

- **Description**: Asks the user if they would like to add an item to the shopping list.
- **User Input**:
  - Takes input for whether the user wants to add an item.
- **Returns**:
  - Boolean indicating the user's choice.

### Method: `updated_list(self, new_item)`

- **Description**: Updates the shopping list by adding a new item.
- **Parameters**:
  - `new_item`: The item to be added to the shopping list.
- **Logic**:
  - Appends the new item to the shopping list.
  - Calls the `list_preview` method to display the updated shopping list.

## Example Usage:

```python
# Assume shopping_list is obtained from an InventoryChecker instance
shopping_list = ["Pasta", "Tomato Sauce", "Cheese", "Garlic"]

# Create an instance of the AddingAdditionalItems class
additional_items_manager = AddingAdditionalItems(shopping_list)

# Preview the current shopping list
additional_items_manager.list_preview()

# Inquire about adding a new item
add_item_decision = additional_items_manager.item_addition_inquiry()

if add_item_decision:
    new_item = input("Enter the item you want to add to the shopping list: ")
    # Update the shopping list
    additional_items_manager.updated_list(new_item)
```

# Finalize List Module

This Python module, part of sub-package #2, consists of two classes: `ShoppingListBase` and `FinalizeList`. These classes provide functionality for displaying, sorting, and finalizing a shopping list.

## Class: ShoppingListBase

### Method: `__init__(self, shopping_list)`

- **Description**: Initializes an instance of the `ShoppingListBase` class.
- **Parameters**:
  - `shopping_list`: The initial shopping list to be managed.

### Method: `display_shopping_list(self)`

- **Description**: Prints the current shopping list.
- **Output**:
  - Displays each item in the shopping list.

## Class: FinalizeList (Inherits from ShoppingListBase)

### Method: `sorted_list(self)`

- **Description**: Returns a sorted version of the shopping list.
- **Returns**:
  - A sorted list of items in the shopping list.

### Method: `cross_out(self, item)`

- **Description**: Crosses out a specified item from the shopping list.
- **Parameters**:
  - `item`: The item to be crossed out.
- **Logic**:
  - Removes the specified item from the shopping list.
  - Prints a message indicating whether the item was successfully crossed out.

### Method: `list_check(self)`

- **Description**: Checks if all items have been crossed out from the shopping list.
- **Logic**:
  - Prints a message indicating whether the shopping list is complete or lists remaining items.

## Example Usage:

```python
# Assume shopping_list is obtained from an AddingAdditionalItems instance
shopping_list = ["Pasta", "Tomato Sauce", "Cheese", "Garlic"]

# Create an instance of the ShoppingListBase class
shopping_list_base = ShoppingListBase(shopping_list)

# Display the current shopping list
shopping_list_base.display_shopping_list()

# Create an instance of the FinalizeList class
finalized_list_manager = FinalizeList(shopping_list)

# Sort the shopping list
sorted_list = finalized_list_manager.sorted_list()

# Cross out an item
finalized_list_manager.cross_out("Cheese")

# Check the status of the shopping list
finalized_list_manager.list_check()
```