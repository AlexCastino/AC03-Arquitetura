import unittest
from Programa import Calculadora

class TesteSoma(unittest.TestCase):
    def testesomaok(self):
        calculadora = Calculadora()
        soma=calculadora.calcular(10, 1,"+")
        self.assertEqual(soma,11)
        
    def testesomaoperadorinvalido(self):
        calculadora = Calculadora()
        soma=calculadora.calcular(10, 1,"e")
        self.assertEqual(soma,11)
        
    def testesomatipoinvalido(self):
        calculadora = Calculadora()
        soma=calculadora.calcular("10", 1,"+")
        self.assertEqual(soma,11)
        

if __name__ == '__main__':
    unittest.main()
 