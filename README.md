# Python para principiantes
Curso Python para Principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo (Canal Fazt) 

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

## Crie um arquivo chamado commands.py

```python
# Comando para verão
python --version

#Abrir o interpretador
python

#Cálculo simples
3 + 3

#sair do interpretador
exit()
```

## Crie um arquivo chamado helloworld.py

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

## Trabalhando com strings

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

## Trabalhando com números

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

## Solicitando antrada do usuários

Crie um arquivo chamado input.py

```python
age = input('Insert your age: ')
print(age) # exibe a entrada
print(type(age)) # tipo string
newAge = int(age) + 5 # converter para inteiro para calcular
print(type(int(age))) # tipo convertido
print(newAge) # imprimir o resultado
```

## trabalhando com listas

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

01:59:00