import sys

class Calculadora:
    def __init__(self):
        super().__init__()
    def dividir(self, n1, n2):
        try:
            print(n1 / n2)
        except ZeroDivisionError as error:
            print('Divisão por zero não permitida:', error)
        except TypeError as error:
            print('Apenas números inteiros são permitidos:', error)
        except:
            print('Error {}'.format(sys.exc_info()[0]))
            print('Error {}'.format(sys.exc_info()[1]))

calc = Calculadora()
calc.dividir(10, 0)
calc.dividir('', 0)