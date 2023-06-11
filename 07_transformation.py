nombre = "Juan"
print(type(nombre))
nombre = 12
print(type(nombre))
name = True
print(type(nombre))

print("Juan" + " Barrios")#Concatena
print(10 + 20) #Suma
#print("Juan" + 12) => Error
print("Juan " + "12")

age = 12
print("Mi edad es " + str(age)) # => Transformación a str
print("Mi edad es ",age)
print(f"Mi edad es {age}")

#Capturar como int
age = int(input("Escribe tu edad: "))
print(type(age))
print(f"Tu edad es 10 años será {age + 10}")

name = 'Juana'
print(name)
age = '10'
print(age)


template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {int(age) + 10} años"
print(template)