import unittest
from unittest.mock import patch
from adding_additional_items import AddingAdditionalItems

class TestAddingAdditionalItems(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shopping_list = ['apples', 'bananas', 'milk']
        cls.adding = AddingAdditionalItems(cls.shopping_list)
        print('setUpClass: Run once before any tests in this class')

    @classmethod
    def tearDownClass(cls):
        cls.adding = None
        print('tearDownClass: Run once after all tests in this class')

    def setUp(self):
        self.new_item = 'bread'
        print('setUp: Run before each test method')

    def tearDown(self):
        print('tearDown: Run after each test method')

    def test_list_preview(self):
        with patch('builtins.print') as mocked_print:
            self.adding.list_preview()
            mocked_print.assert_called()
            self.assertEqual(mocked_print.call_count, len(self.shopping_list) + 1)

    def test_updated_list(self):
        initial_list_size = len(self.adding.shopping_list)
        self.adding.updated_list(self.new_item)

        self.assertIn(self.new_item, self.adding.shopping_list, "New item should be added to the list")
        self.assertEqual(self.adding.shopping_list[-1], self.new_item, "New item should be last in the list")
        self.assertEqual(len(self.adding.shopping_list), initial_list_size + 1, "List should increase by one item")
        self.assertNotIn('orange', self.adding.shopping_list, "Item not added should not be in the list")

if __name__ == '__main__':
    unittest.main()
