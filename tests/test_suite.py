import unittest
from test_ingredients_management import TestRecipeManager
from test_inventory_check import TestInventoryCheck
from test_adding_additional_items import TestAddingAdditionalItems
from test_finalize_list import TestFinalizeList

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRecipeManager))
    test_suite.addTest(unittest.makeSuite(TestInventoryCheck))
    test_suite.addTest(unittest.makeSuite(TestAddingAdditionalItems))
    test_suite.addTest(unittest.makeSuite(TestFinalizeList))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())