import unittest

from function_curs08 import sublist_containing_o

class FunctionsTestCase(unittest.TestCase): #trebuie sa mosteneasca de la clasa de baza TestCase din libraria unittest
    def test_sublist_containing_o(self):
        expected_result = ['Python', 'nostru']
        actual_result = sublist_containing_o(["Python", "este", "limbajul", "nostru", "preferat"])
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()