# Função

print("Função que imprime na tela")
dir({"Função que retorna ajuda"})
type(["Função que retorna o tipo", 1])
len('Hello')

# Criando a própria função

def hello():
    print('Hello world!')

# Chamando a função

hello()

# Passando parâmetros e sobrecarregando

def hello(name):
    print('Hello', name)

hello('Tiago')
hello('Lucas')

# Definindo uma valor padrão

def congrat(name, nickname='no'):
    print('Hello', name, 'Nick:', nickname)

congrat('Igor', 'ig')
congrat('Valentina')

# Usando cálculos em funções

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 30))
print(add(600, 10))

# Funções lambda

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10, 30))