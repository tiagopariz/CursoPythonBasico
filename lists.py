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