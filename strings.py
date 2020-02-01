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
