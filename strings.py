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