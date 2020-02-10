import sys

class CalculaImposto:
    def __init__(self, valorOriginal, percentual, tipo, parcelas = 1):
        try:
            self.valorOriginal = float(valorOriginal)
            self.percentual = float(percentual)
            self.tipo = str(tipo)
            self.parcelas = parcelas
        except TypeError as error:
            print('Dados inválidos: ', error)
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
    def calcular(self):
        try:
            self.imposto = self.valorOriginal * (self.percentual / 100)
            self.valorFinal = self.valorOriginal + self.imposto
            self.valorParcelas = self.valorFinal / self.parcelas
        except:            
            print('Erro ao calcular o imposto e as parcelas')
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
        else:            
            print('Valor original:', self.valorOriginal)
            print('{}: {} ({}%)'.format(self.tipo, self.imposto, self.percentual))
            print('Valor total a pagar:', self.valorFinal)
            print('Valor da Parcela:', self.valorParcelas)
        finally:
            print('Fim')

calc = CalculaImposto(100, 8, 'ICMS')
calc.calcular()
calc = CalculaImposto(1050, 5, 'ISSC', 0)
calc.calcular()