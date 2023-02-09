import unittest
from main import is_prime, lista_de_prime, Cerc, Patrat
class FunctionTestCase(unittest.TestCase):
    def test_true(self):
        expected_result = True
        actual_result = is_prime(7)
        self.assertEqual(expected_result, actual_result)
    def test_false(self):
        expected_result = False
        actual_result = is_prime(14)
        self.assertEqual(expected_result, actual_result)
    def test_is_prime1(self):
        expected_result = [2, 3, 5, 7]
        actual_result = lista_de_prime(2,9)
        self.assertEqual(expected_result,actual_result)
    def test_is_prime2(self):
        expected_result = [5, 7, 11, 13, 17]
        actual_result = lista_de_prime(4,18)
        self.assertEqual(expected_result,actual_result)


class FiguresTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.cerc = Cerc(5)
        cls.patrat = Patrat(5)

    def test_descrie_cerc(self):
        self.assertEqual(self.cerc.descriere(), 'Eu nu am colturi')


    def test_descrie_patrat(self):
        self.assertEqual(self.patrat.descriere(), 'Cel mai probabil am colturi')

    def test_aria_cerc(self):
        self.assertEqual(self.cerc.arie(), 78.5)

    def test_aria_patrat(self):
        self.assertEqual(self.patrat.arie(), 25)

    def test_setter_getter_cerc(self):
        self.cerc.set_raza = 10
        self.assertEqual(self.cerc.raza, 10)

    def test_setter_getter_patrat(self):
        self.patrat.set_latura = 10
        self.assertEqual(self.patrat.latura, 10)

    def test_deleter_cerc(self):
        del self.cerc.del_raza
        self.assertEqual(self.cerc.raza, None)

    def test_deleter_patrat(self):
        del self.patrat.del_latura
        self.assertEqual(self.patrat.latura, None)

if __name__ == '__main__':
    unittest.main()