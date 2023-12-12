import unittest
from test_ingredients import TestRecipeManager
from test_inventory_check import TestInventoryCheck

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRecipeManager))
    test_suite.addTest(unittest.makeSuite(TestInventoryCheck))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())