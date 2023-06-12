my_dict = {
    'name': "Juan",
    "lastname": "Barrios",
    "age": 26
}

print(type(my_dict))
print(my_dict)
print(len(my_dict))
print(my_dict["name"])
print(my_dict["lastname"])

# Si no estoy tan seguro mejor con el get porque devuelve NONE
print(my_dict.get("age"))
print(my_dict.get("Algo"))

#Validacion
print("name" in my_dict)
print("noesta" in my_dict)