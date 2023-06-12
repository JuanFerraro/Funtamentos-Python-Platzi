""" for element in range(1,21):
    print(element) """
#Lista
my_list = [23, 45, 12, 7, 89, 9]
for i in my_list:
    print(i)

#Tupla
my_tuple = ('Juan', 'Sebastian', 'Barrios')
for i in my_tuple:
    print(i)

#Diccionario
product = {
    'name': 'Casaca',
    'prince': 10,
    'stock': 20
}

for i in product:
    print(i, '=>', product[i])

for key, value in product.items():
    print(key, '=>', value)
print('*'*20)

people = [
    {
        'name': 'Juan',
        'age': 23
    },
    {
        'name': 'Sebastian',
        'age': 12
    },
    {
        'name': 'Barrios',
        'age': 26
    }
]

for i in people:
    print('name: ', i['name'])
print('*'*20)

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
for i in my_list:
  if i > 0:
    new_list.append(i)

print(new_list)