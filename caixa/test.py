import unittest
from cliente import Imprime
from contas import Conta

class ImprimeTestCase(unittest.TestCase):

    def test_de_conx(self):
        self.assertEqual(1, Imprime().teste(1))


class ContaTestCase(unittest.TestCase):

    def test_de_conx2(self):
        self.assertEqual(2, Conta().deposito(2))

if __name__ == "__main__":
    unittest.main()
