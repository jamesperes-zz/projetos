import unittest
from cliente import Imprime

class ImprimeTestCase(unittest.TestCase):

    def test_de_conx(self):
        self.assertEqual(1, Imprime().teste(1))




#if __name__ == "__main__":
#    unittest.main()
