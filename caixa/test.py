import unittest
from cliente import Imprime
from contas import Conta


class ImprimeTestCase(unittest.TestCase):

    def test_de_conx(self):
        self.assertEqual(1, Imprime().teste(1))


class ContaTestCase(unittest.TestCase):

    def test_de_conx2(self):
        conta = Conta(1, 1)
        conta.deposito(2)
        self.assertEqual(2, conta.saldo)


if __name__ == "__main__":
    unittest.main()
