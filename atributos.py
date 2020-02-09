class Atributo:
    def __init__(self):
        self.x = 0
        self.y = 0

MeuAtributo = Atributo()

# Exibindo os valores dos atributos
print(MeuAtributo.x)
print(MeuAtributo.y)

# Alterando os valore
MeuAtributo.x = 5
MeuAtributo.y = 7
print(MeuAtributo.x)
print(MeuAtributo.y)

# Adicionando um novo atributo
MeuAtributo.z = 8
print(MeuAtributo.z)