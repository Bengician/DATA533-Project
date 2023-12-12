import unittest
from unittest.mock import patch
from unittest.mock import call
from finalize_list import FinalizeList

class TestFinalizeList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass: Run once before any tests in this class')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass: Run once after all tests in this class')

    def setUp(self):
        self.shopping_list = ['apples', 'bananas', 'milk']
        self.finalize = FinalizeList(self.shopping_list)
        print('setUp: Run before each test method')

    def tearDown(self):
        print('tearDown: Run after each test method')

    def test_sorted_list(self):
        sorted_list = self.finalize.sorted_list()
        self.assertEqual(sorted_list, sorted(self.shopping_list), "The sorted list should be the same as the manually sorted list")
        self.assertEqual(sorted_list[0], 'apples', "First item should be apples")
        self.assertEqual(sorted_list[-1], 'milk', "Last item should be milk")
        self.assertEqual(len(sorted_list), len(self.shopping_list), "Sorted list should have the same number of items")

    def test_cross_out(self):
        with patch('builtins.print') as mocked_print:
            self.finalize.cross_out('bananas')
            mocked_print.assert_called_once_with("bananas has been crossed out from the list.")
            self.assertNotIn('bananas', self.finalize.shopping_list, "Bananas should be removed from the list")
            self.assertEqual(len(self.finalize.shopping_list), 2, "Shopping list should have one less item after crossing out")

    def test_list_check(self):
        with patch('builtins.print') as mocked_print:
            self.finalize.shopping_list = ['milk']
            self.finalize.list_check()
            expected_calls = [call("The following items are still on the list:"), call("- milk")]
            mocked_print.assert_has_calls(expected_calls)


if __name__ == '__main__':
    unittest.main()



