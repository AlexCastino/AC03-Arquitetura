import unittest
from Programa import Calculadora

class TesteMultiplicar(unittest.TestCase):
    def testemultiplicarok(self):
        calculadora = Calculadora()
        multiplicar=calculadora.calcular(10, 1,"*")
        self.assertEqual(multiplicar,10)
        
    def testemultiplicaroperadorinvalido(self):
        calculadora = Calculadora()
        multiplicar=calculadora.calcular(10, 1,"e")
        self.assertEqual(multiplicar,10)
        
    def testemultiplicartipoinvalido(self):
        calculadora = Calculadora()
        multiplicar=calculadora.calcular("10", 1,"*")
        self.assertEqual(multiplicar,10)
        

if __name__ == '__main__':
    unittest.main()
 