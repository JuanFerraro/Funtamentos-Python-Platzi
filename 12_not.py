#NOT negación
print(not True)
print(not False)

print("NOT AND")
print("True and True => ", not (True and True))
print("True and False => ",not (True and False))
print("False and True => ",not (False and True))
print("False and False => ",not (False and False))

print("*" * 25)

stock = int(input("Ingrese la cantidad en stock: "))
role = input ("Digita el rol: ")
print(not (role == 'admin' or role == 'vendedor'))
print(not (stock >= 100 and stock <= 1000))