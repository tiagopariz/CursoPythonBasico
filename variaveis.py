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