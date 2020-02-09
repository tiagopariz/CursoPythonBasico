# list
cart = [
    ["book1", 3, 4.99],
    ["book2", 3, 6.99],
    ["book3", 3, 15.99]
]

# Dictionary
product = {
    "name": "Book1",
    "quantity": 3,
    "price": 3
}

print(type(product)) # <class 'dict'>

person = {
    "first_name": "ryan",
    "last_name": "ray"
}

print(type(person)) # <class 'dict'>
print(dir(person)) # help
print(person.keys())
print(person.items())

person.clear()
print(person)
del person;
# print(person)

products = [
    {"name": "Book", "price": 10.99},
    {"name": "Laptop", "price": 100.99}
]

print(products)