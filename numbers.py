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