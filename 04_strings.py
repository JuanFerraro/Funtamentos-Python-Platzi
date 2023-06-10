nombre = "Juan"
print(nombre)

apellido = "Barrios"
print(apellido)

#Unir dos valores (Concatenacion):
nombre_completo = nombre + " " + apellido
print(nombre_completo)

#Usar ingles en variables
quote = "I'm Juan" #Mejor usar comillas dobles
print(quote)

quote2 = "She said 'Hi doggie' "
print(quote2)

#Manipular su formato: (format) estructurar el texto
template = "Hi, my name is " + nombre + " and my last name is " + apellido
print("v1", template)

template = "Hi, my name is {} and my last name is {}".format(nombre, apellido)
print('v2', template)

template = f"Hi, my name is {nombre} and my last name is {apellido}"
print("v3", template)