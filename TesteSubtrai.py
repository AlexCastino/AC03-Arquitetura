import unittest
from Programa import Calculadora

class TesteSubtrair(unittest.TestCase):
    def testesubtrairok(self):
        calculadora = Calculadora()
        subtrair=calculadora.calcular(10, 1,"-")
        self.assertEqual(subtrair,9)
        
    def testesubtrairoperadorinvalido(self):
        calculadora = Calculadora()
        subtrair=calculadora.calcular(10, 1,"e")
        self.assertEqual(subtrair,9)
        
    def testesubtrairtipoinvalido(self):
        calculadora = Calculadora()
        subtrair=calculadora.calcular("10", 1,"-")
        self.assertEqual(subtrair,9)
        

if __name__ == '__main__':
    unittest.main()
 