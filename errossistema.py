import sys

class Calculadora:
    def dividir(self, numero1, numero2):
        try:
            print(numero1 / numero2)
        except:
            print('Error {}'.format(sys.exc_info()[0]))
            print('Error {}'.format(sys.exc_info()[1]))
            print('Error {}'.format(sys.exc_info()[2]))

calc = Calculadora()
calc.dividir(10, 0)