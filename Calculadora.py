import unittest
from Programa import *

class Main(unittest.TestCase):
    def teste(self):
        calculadora = Calculadora()
        soma=calculadora.calcular(10, 1,"+")
        self.assertEqual(soma,11)
        
        subtracao=calculadora.calcular(10, 1,"-")
        self.assertEqual(subtracao,9)
        
        divisao=calculadora.calcular(10, 1,"/")
        self.assertEqual(divisao,10)
        
        multiplicar = calculadora.calcular(10,2,"*")
        self.assertEqual(multiplicar,20)

if __name__ == '__main__':
    unittest.main()











