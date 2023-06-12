person = {
    'name': 'Juan',
    'lastname': 'Barrios',
    'age': 26,
    'langs': ['python', 'java']
}

print(person)

# Update
person['name'] = 'Sebastian'
person['age'] -= 1
person['langs'].append('javascript')
print(person)

# Delete
del person['lastname']  # eliminar atributo
person.pop('age')  # Si o si espera argumento en diccionarios
print(person)

#Metodos importantes
print('items')
print(person.items()) #Devuelve en pares de tupla

print('keys')
print(person.keys()) #Devuelve las 'llaves o claves'

print('values')
print(person.values()) #Devuelve los 'valores'