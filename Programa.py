import abc
from unittest import result
class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = OperacaoFabrica.criar(self,operador)
        print("")
        print("Executando a conta ",valor1,operador,valor2)
        print("__________________________")
        print("")
        
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1,valor2)
            print("Resultado ",resultado)
            print("")
            return resultado
        
class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == "+") or (operador == "soma"):
            return Soma()
        elif (operador == "-") or (operador == "subtracao"):
            return Subtracao()
        elif (operador == "/") or (operador == "divisao"):
            return Divisao()
        elif (operador == "*") or (operador == "multiplicacao"):
            return Multiplicacao()
        else:
            print("")
            print("")
            print("Erro Operador invalido")
        
class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,valor1,valor2):
        pass
    
###############################Inicio Soma######################################    
################################################################################
class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado
################################################################################
 
###############################Inicio Subtracao#################################
################################################################################       
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado
################################################################################

###########################Inicio Multiplicacao#################################
################################################################################   
class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado
################################################################################

###############################Inicio Divisao###################################
################################################################################    
class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado
################################################################################
    
    

