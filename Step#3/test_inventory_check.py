import unittest
import inventory_check

class TestInventoryCheck(unittest.TestCase):

    def setUp(self):
        self.ingredient = "oil"
        self.initial_inventory = ["rice", "oil"]
        self.inventory = self.initial_inventory.copy()
        self.response = "yes"

    def tearDown(self):
        self.inventory = self.initial_inventory.copy()

    def test_remove_existing_ingredient(self):
        if self.response.lower() == "yes":
            self.inventory.remove(self.ingredient)

        self.assertNotIn(self.ingredient, self.inventory)
        self.assertEqual(len(self.inventory), 1)
        self.assertTrue(all(item in self.inventory for item in ["rice"]))
        self.assertTrue(self.response.lower() in ["yes", "no"])

def test_display_shopping_list(self):
    result = inventory_check.display_shopping_list(self.inventory)

    if self.inventory:
        expected_output = "You need to buy the following ingredients:\n"
        for item in self.inventory:
            expected_output += f"- {item}\n"
        self.assertEqual(result, expected_output)
    else:
        self.assertEqual(result, "")
    self.assertIsInstance(result, str, "The result should be a string.")
    self.assertGreater(len(result), 0, "The result should have a length greater than 0.")
    self.assertNotIn('!', result, "The result should not contain the '!' character.")

if __name__ == '__main__':
    unittest.main()