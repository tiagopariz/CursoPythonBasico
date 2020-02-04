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