import unittest
import ingredients_management

class TestRecipeManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common_ingredient = "Common Ingredient"
        cls.common_recipe_name = "Common Recipe"
        print(f"Setting up common data for all tests")

    @classmethod
    def tearDownClass(cls):
        print(f"Tearing down common data for all tests")

    def setUp(self):
        self.recipes = {}
        self.recipe_name = "Test Recipe"
        print(f"Adding a new recipe: {self.recipe_name}")
        self.recipes[self.recipe_name] = []

    def tearDown(self):
        print(f"Removing the test recipe: {self.recipe_name}")
        del self.recipes[self.recipe_name]

    def test_add_recipe(self):
        self.assertIn(self.recipe_name, self.recipes)
        self.assertEqual(len(self.recipes[self.recipe_name]), 0)
        new_recipe_name = "New Recipe"
        self.assertNotIn(new_recipe_name, self.recipes)
        self.recipes[new_recipe_name] = ["Ingredient 1", "Ingredient 2"]

    def test_add_ingredient(self):
        initial_ingredient_count = len(self.recipes[self.recipe_name])

        ingredient1 = "Test Ingredient 1"
        self.recipes[self.recipe_name].append(ingredient1)

        self.assertIn(ingredient1, self.recipes[self.recipe_name])
        self.assertEqual(len(self.recipes[self.recipe_name]), initial_ingredient_count + 1)

        ingredient2 = "Test Ingredient 2"
        self.recipes[self.recipe_name].append(ingredient2)

        self.assertIn(ingredient2, self.recipes[self.recipe_name])
        self.assertEqual(len(self.recipes[self.recipe_name]), initial_ingredient_count + 2)

if __name__ == '__main__':
    unittest.main()