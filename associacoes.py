# crio uma classe de cachorro com métodos
class Cachorro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def daAPatinha(self):
        print('{} extendeu a patinha'.format(self.nome))
    def latir(self):
        print('AUAUAUAUAUAUAUAUAUAUAU')

# crio uma classe de pessoa que recebe nome, peso e cão
# o cão é uma associação com a classe cachorro
class PessoaS2Animais:
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
    def treinar(self):
        self.cao.daAPatinha()
        self.cao.latir()

# associa
rex = Cachorro('Rex', 'Marrom')
paulo = PessoaS2Animais('Paulo', 68, rex)

# chamando os atributos das duas classes
print(paulo.nome)
print(paulo.peso)
print(paulo.cao.nome)
print(paulo.cao.cor)

# chamando os metodos
rex.daAPatinha()
rex.latir()
paulo.treinar()
