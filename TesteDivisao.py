import unittest
from Programa import Calculadora

class TesteDividir(unittest.TestCase):
    def testedividirok(self):
        calculadora = Calculadora()
        dividir=calculadora.calcular(10, 1,"/")
        self.assertEqual(dividir,10)
        
    def testedividiroperadorinvalido(self):
        calculadora = Calculadora()
        dividir=calculadora.calcular(10, 1,"e")
        self.assertEqual(dividir,10)
        
    def testedividirtipoinvalido(self):
        calculadora = Calculadora()
        dividir=calculadora.calcular("10", 1,"/")
        self.assertEqual(dividir,10)
        

if __name__ == '__main__':
    unittest.main()
 