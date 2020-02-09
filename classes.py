# Classe básica
class My_Object(object):
    # Construtor
    def  __init__(self):
        # Atributos
        self.nome = 'Tiago'
        self.idade = '36'
        print('Construtor chamado com sucesso')
    # Métodos
    def imprime(self):
        print('Olá meu nome é {} e eu tenho {}'.format(self.nome, self.idade))

# Instanciando
Tiago = My_Object()

# Exibindo os atributos
print(Tiago.nome, Tiago.idade)

# Chamando o método
Tiago.imprime()

# Passando parâmetros no construtor
class My_Object2:
    def __init__(self, n, i):
        self.nome = n
        self.idade = i
        print("Meu nome é {} e eu tenho {}".format(self.nome, self.idade))

Ronald = My_Object2('Ronald', 38)

# Passando parâmetros nos métodos
class My_Object3:
    # Método que recebe dois parâmetros
    def imprime(self, nome, idade):
        print('Meu nome é {} e eu tenho {}'.format(nome, idade))
    # Recebe e efetua um cálculo
    def quanto_falta_pra_30(self, idade):
        falta = 30 - idade
        print('Faltam {} anos para 30'.format(falta))
    # Recebe e retorna um valor
    def que_ano_faco_30(self, anoatual, idade):
        facoem = anoatual + (30 - idade)
        return facoem
    # Recebe argumentos sem um limite
    def amigos(self, *args):
        return args

Eric = My_Object3()
Eric.imprime('Eric', 15)
Eric.quanto_falta_pra_30(15)
print('Faço 30 em', Eric.que_ano_faco_30(2020, 15))
print('Meus amigos:', Eric.amigos('Antonio', 'Margaret', 'Paulo'))