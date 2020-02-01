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
print(myString[4]) # retorna um caractere na posição
```

01:20:00