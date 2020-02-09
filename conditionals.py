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
