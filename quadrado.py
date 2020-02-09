class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
        self.area = self.tamanho_lado ** 2
        print('Tamanho do lado:', self.tamanho_lado)        
        print('Area:', self.area)
    def alterar(self, novo_tamanho):
        tamanho_lado = novo_tamanho
        area = tamanho_lado ** 2
        print('Tamanho do lado:', tamanho_lado)        
        print('Area:', area)
    
MeuQuadrado = Quadrado(10)
MeuQuadrado.alterar(20)