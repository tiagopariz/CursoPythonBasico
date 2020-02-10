# tratando uma exceção simples
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.resultado = 0
    def divisao(self):
        try:
            self.resultado = self.numero1 / self.numero2
            print(self.resultado)
        except:
            print('Erro ao dividir')

calc = Calculadora(10, 0)
print(calc.divisao()) 
calc.numero2 = 2
print(calc.divisao())

# usando mais de um try
class Planilha:
    def __init__(self, valorA, valorB, linhas):
        try:
            posicao = 1
            self.valorA = int(valorA)
            self.valorB = int(valorB)
            while posicao <= linhas:
                try:
                    self.valorA = self.valorA + posicao
                    self.valorB = self.valorB + posicao
                    print('ValorA{}:'.format(posicao), 
                          self.valorA,
                          'ValorB{}:'.format(posicao),
                          self.valorB,
                          'A / B =', self.valorA / self.valorB)
                except:
                    print('Erro ao dividir por zero')
                posicao = posicao + 1
        except:
            print('Erro, Digite apenas números')

planilha = Planilha(10, 2, 5)
planilha = Planilha(3, -1, 5)