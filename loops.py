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
