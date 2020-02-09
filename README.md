# Python para principiantes

# Parte 1

## Introdução

Python é uma das linguagens de programação que mais cresceram nos últimos anos. O Python é uma linguagem alto nível de uso geral, incluindo aplicações científicas. É uma linguagem dinamica e de fácil aprendizado.

http://datascienceacademy.com.br/blog/o-incrivel-crescimento-da-linguagem-python/

É um boa linguagem para iniciantes, não exigindo chaves e pontos e vírgulas. É simples e bastante legível. Contém muitas bibliotecas. É gratuíta e tem uma grande comunidade que revisa constantemente.

É possível criar aplicativos de linha de comando, desktop, web, robótica e aplicações científica.

Exemplo que usam Python:

- Quora
- django

## Instalando o Python e Visual Studio Code no Windows

É preciso instalar o interpretador e o ambiente de desenvolvimento.

- https://www.python.org
- https://code.visualstudio.com/

No Visual Studio instale as extensões:

- Python da Microsoft

## Usando o console

Crie um arquivo chamado commands.py

```powershell
# Comando para verão
python --version

# Abrir o interpretador
python

# Cálculo simples
3 + 3

# sair do interpretador
exit()
```

## Meu primeiro programa 

Crie um arquivo chamado helloworld.py

```python
# No interpretador de linha de comando digite 
# "Hello Word!"

# Exibe uma mensagem na tela
print("Hello world!")
```

Execute o comando na pasta 

```powershell
python helloword.py
```

## Variáveis e tipos de dados

Crie uma arquivo chamado variaveis.py

```python
# Tipo Texto
print("Hello world!")
print('Hello world!')
print("""Hello world!""")
print('''Hello world!''')
print(type("Hello world"))

# Concatenar
print("Bye" + "World")

# Números
# Inteiros: 10, 30 ... (int)
print(30)
print(type(30))
print(100)
print(type(100))
# Decimais ou flutuantes: 10.3, 30.5 ... (float)
print(30.5)
print(type(30.5))
print(10.11)
print(type(10.11))

# Lógicos (boolean)
# True e False
print(True)
print(type(True))
print(False)
print(type(False))

# Listas (list)
# Pode alterar
# 10 20 30 55
print([10, 20, 30, 55])
print(type([10, 20, 30, 55]))
print(['Hello', 'Bye', 'Tchau'])
print([10, 'Hello', True, 10.5])

# Tuplas (tuple)
# Não pode alterar
print((10, 20, 30))
print(type((10, 20, 30)))

# Dicionários (dict)
# Lista com nome e valor ("Key":value)
print({
    "nome": "João",
    "sobrenome":"Neves",
    "apelido":"John",
})
print(type({
    "nome": "João",
    "sobrenome":"Neves",
    "apelido":"John",
}))
print({
    "latitude": 12365545,
    "longitude": 6464
})

# Não definido (NoneType)
print(None)
print(type(None))

# Usando variáveis
# case sensitive
# não pode começar com número 
nome = 'Tiago'
print(nome)

usuario = 'tpa'
print(usuario)

idade = 30
print(idade)

altura = 1.76
Altura = 1.56
print(altura)
print(Altura)

cidade, numerocasa = 150, "PoA"
print(cidade, numerocasa)

# Convenções
book_name = 'Fort' # Snake case
bookName = 'O código davinci' # Camel case
BookName = 'Clean code' # Pascal case

# Constantes
# Upper case
PI = 3.1416
```

## Strings

Crie uma arquivo chamado strings.py

```python
# Declare uma variável
myString = 'hello world all!'

print(dir(myString)) # funcões
print(myString.upper()) # Maiúsculça
print(myString.lower()) # Minúscula
print(myString.swapcase()) # Primeira minúscula e demais maíscula
print(myString.capitalize()) # primeira em maiúscula
print(myString.replace('hello', 'bye')) # substitui
print(myString.count('l')) # contar quantas vezes aparece a letra
print(myString.startswith('hello')) # se começa com um texto específico
print(myString.endswith('hello')) # se termina com uma palavra
print(myString.split(' ')) # dividir o texto
print(myString.find('a')) # posição de uma caractere
print(len(myString)) # posicao da ultima letra
print(myString.index('o')) # indice de uma letra
print(myString.isnumeric()) # se o conteudo é númerico
print(myString.isalpha()) # se o conteudo é alfabético

#   h   e   l   l   o       w  o  r  l  d     a  l  l  !
#   0   1   2   3   4   5   6  7  8  9 10 11 12 13 14 15
# -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 

print(myString[4]) # retorna um caractere na posição do índice 4
print(myString[0]) # retorna um caractere na posição do índice 0
print(myString[-2]) # retorna um caractere na posição do índice -2
print(myString[-10]) # retorna um caractere na posição do índice -2

# Concatenações
print('My first app: ' + myString)
print('My first app:', myString)
print(f'My first app: {myString}')
print('My first app: {myString}'.format(myString))
print('My first app: {0}'.format(myString))
```

## Números

Crie um arquivo chamado Numbers.py

```python
# 10 inteiro
# 14.4 decimal de ponto flutuante

print(type(10)) # tipo int
print(type(14.4)) # tipo float
print(3 + 3) # soma
print(3 - 1) # subtração
print(3 / 5) # divisão
print(5 * 6) # multiplicação
print(5.0 * 5) # multiplicação com decimal
print(2**3) # potenciação 2³
print( 3 / 2) # divisão
print(3 // 2) # divisão inteira
print(3 % 2) # resto da divisão

# precedência
print(20 - 10 * 5 ** 2)
print(5 ** 2) # primeiro a potenciação
print(-10 * 25) # depois a multiplicação
print(20 - 250) # e por último a subtração

# precedência por parenteses
print((20 - 10) * (5 ** 2))
print(20 - 10) # calcula o primeiro parenteses
print(5 ** 2) # calcula o segundo parentese
print(10 * 25) # calcula o resultado dos dois parenteses
```

## Solicitando a entrada do usuário

Crie um arquivo chamado input.py

```python
age = input('Insert your age: ')
print(age) # exibe a entrada
print(type(age)) # tipo string
newAge = int(age) + 5 # converter para inteiro para calcular
print(type(int(age))) # tipo convertido
print(newAge) # imprimir o resultado
```

## Listas

Crie um arquivo chamado lists.py

```python
# listas simples
demoList = [1, 'hello', 1.34, True, [1,2,3]]
print(demoList)

# usando o construtor
numberList = list((1, 2, 3, 4))
print(numberList)
print(type(numberList))


# Intervalos
r = list(range(1, 100))
print(r)

colors = ['red', 'green', 'blue']
print(colors) # exibe os itens
print(type(colors)) # mostra o tipo
print(dir(colors)) # ajuda
print(len(colors)) # conta itens
print(colors[2]) # buscando um item índice
print('green' in colors) # Se um elemento existe
print('orange' in colors)
colors[1] = 'yellow' # editando um item
print(colors)
colors.append('violet') # adicionando um item
colors.extend(('green', 'silver')) # adicionando vários
print(colors)
colors.insert(1, 'white') # adiciona um elemento em uma posição
colors.insert(len(colors), 'black') # adiciona um item no final
print(colors)
colors.pop() # excluir o ultimo item
print(colors)
colors.pop()
colors.pop()
print(colors)
colors.remove('white') # remove por nome
print(colors)
colors.pop(0) # remove por índice
print(colors)
colors.sort() # ordenar asc
print(colors)
colors.sort(reverse=True) # ordernar desc
print(colors)
print(colors.index('yellow')) # exibir o índice de um item
colors.insert(len(colors), 'blue') # adiciona um item no final
colors.insert(len(colors), 'blue') # adiciona um item no final
colors.insert(len(colors), 'violet') # adiciona um item no final
print(colors.count('blue')) # contar por tipo
print(colors.count('violet')) # contar por tipo
print(colors.count('yellow')) # contar por tipo
```

# Parte 2

## Tuplas

Crie um arquivo chamado tuples.py

Mais rápidas e não se pode editar

```python
x = (1, 2, 3) # uma tupla
print(type(x))
print(x)
y = tuple((1, 2, 3)) # tupla por construtor
print(y)
print(dir(y))
x = (1)
print(type(x))
print(x) # não é uma tupla
x = (1,) # é uma tupla
print(type(x))
print(x)
x = (1, 2, 3, 4, 5)
print(x[0]) # buscar por índice
print(x[4])
del x # excluir a tupla
# print(x)
locations = {
    (35.6554646, 39.000): 'Tokyo',
    (35.12545, 39.6565): 'New York'
}
print(locations)
```

## Sets

Crie um arquivo chamado sets.py

```python
colors = {'Red', 'Green', 'Blue'}
print(colors)
print('Green' in colors)
colors.add('Violet')
print(colors)
colors.remove('Red')
print(colors)
colors.clear()
print(colors)
del colors
```

## Dicionários

Adicione um arquivo chamado dictionary.py

```python
# list
cart = [
    ["book1", 3, 4.99],
    ["book2", 3, 6.99],
    ["book3", 3, 15.99]
]

# Dictionary
product = {
    "name": "Book1",
    "quantity": 3,
    "price": 3
}

print(type(product)) # <class 'dict'>

person = {
    "first_name": "ryan",
    "last_name": "ray"
}

print(type(person)) # <class 'dict'>
print(dir(person)) # help
print(person.keys())
print(person.items())

person.clear()
print(person)
del person;
# print(person)

products = [
    {"name": "Book", "price": 10.99},
    {"name": "Laptop", "price": 100.99}
]

print(products)
```

## Conditional

Crie um arquivo chamado conditionals.py

```python
# 3 > 2 = True
# 2 > 3 = False
# 2 < 3 = True
# 3 == 3 = True
# 3 == 4 = False
# name == 'Tiago'

x = 20
print('x =', x)
if x < 30: 
    print("x is less than 30")

x = 40
print('x =', x)
if x > 30: 
    print("x is greater than 30")

x = 30
print('x =', x)
if x == 30:
    print("x is 30")

# senão
x = 15
print('x =', x)
if x < 20:
    print('x is less then 20')
else:
    print('x is greater then 20')

# textos

color = 'Blue'

if color == 'Red':
    print('The color is Red')
else:
    print('Any color')

# senão se
color = 'Blue'

if color == 'Red':
    print('The color is Red')
elif color == 'Blue':
    print('The color is Blue')
else:
    print('Any color')

# Vários se

name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "Carter":
        print("You are", name, lastname)
    else:
        print('You are not John')
else:
    print('You are not Jhon')

# and, or e not

x = 3
if x > 2 and x <= 10:
    print("x is greater than two and less than or equal to ten")

if x > 2 or x <= 20:
    print("x is greater than two or less than or equal to twenty")

if (not(x == 10)):
    print("x is not equal to ten")
```

## Laços

Crie um arquivo chamado loops.py

```python
# lista

foods = ['Apples', 'Brad', 'Cheese', 'Milk', 'Bananas', 'Grapes']

print(foods)
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[2])
print(foods[4])

# usando for

for food in foods:
    print(food)

# usando for e if

for food in foods:
    if food == 'Cheese':
        print("You have to buy this:", food)
    print(food)

# Parando o laço

for food in foods:
    if food == 'Apples':
        break
    print(food)

# Continuando o laço

for food in foods:
    if food == 'Bread':
        continue
    print(food)

# Usando um intervalo

for number in range(1,8):
    print(number)

for letter in 'Hello':
    print(letter)

# Usando o while

count = 4

while count <= 10:
    print(count)
    count = count + 1
```

## Funções

Crie um arquivo chamado functions.py

```python
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
```

## Modulos

Crie um arquivo chamado modules.py

```python
# Módulos: own modules, thirdy party modules e python modules
# Python Module Index: https://docs.python.org/3/py-modindex.html
# PyPI: https://pypi.org/

# Usando o módulo do Python datetime 
# Basic date and time types: https://docs.python.org/3/library/datetime.html
import datetime

print(datetime.date.today())

# Importar apenas uma função

from datetime import timedelta

print(datetime.timedelta(minutes=70))
print(datetime.timedelta(minutes=100))
```

Crie um arquivo chamado matematica.py

```python
def add(n1, n2):
    print(n1 + n2)

def subtract(n1, n2):
    print(n1 - n2)
```

Crie um arquivo chamado calculos.py

```python
import matematica

matematica.add(1, 2)
matematica.subtract(1, 2)

from matematica import add

add(1, 2)

from matematica import add, subtract

subtract(1, 2)
add(1, 2)
```

## Instalando um módulo de terceiros

Vá em https://pypi.org/project/colorama/ e veja o comando para executar.

Verifique a versão do pip

```powershell
pip --version
```

Execute o comando para instalar o módulo

```powershell
pip install colorama
```

Crie o arquivo cores.py

```python
# importe o módulo colorama
import colorama
# ou importe apenas o que irá usar
from colorama import Fore, Style, init

init(convert=True)
print("Hello World!")
print(Fore.RED + "Hello world!")
```

# Parte 3

## Classes

Crie um arquivo chamado classes.py

```python
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
```

Crie uma classe chamada quadrado.py que calcule o quadrado

```python
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
```

## Atributos

Crie um arquivo chamado atributos.py

```python
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
```

## Associações e funções

Crie um novo arquivo chamado associacoes.py

```python
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
```


# Referências

Curso Python para Principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo (Canal Fazt)

Aulas Python - 059 - POO I: Sintaxe Básica, Construtor e Métodos - https://www.youtube.com/watch?v=lsPZTMJ9I6Q

Aulas Python - 060 - POO II: Atributos, Associações e Funções - https://www.youtube.com/watch?v=5FCA0SDvxcI