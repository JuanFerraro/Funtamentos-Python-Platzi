# Tupla: () - Lista: []
numbers = (1, 2, 3, 4, 5, 6, 7, 6)
print(type(numbers))
print("Pos -1:", numbers[-1])

# Pa' que usar una tupla?
# Una vez declarada no puedo ingresar más.

# Metodos de tuplas

# Busqueda y posicion:
print(numbers)
print(numbers.index(4))
print(numbers.count(6))

#Convertirlo a lista:
lista = list(numbers)
print(type(lista))

#Convertir lista a tupla:
tupla = tuple(lista)
print(type(tupla))
