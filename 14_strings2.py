text = "Aprendiendo a programar en Python"

print("JS" in text)
print("Python" in text)

size = len("love")
print(size)

#Metodos:
print(text)
print(text.upper()) #Todo en mayuscula
print(text.lower()) #Todo en minuscula
print(text.count("a")) #Contar cuantos caracteres hay de x
print(text.swapcase()) #May -> min y min -> may
print(text.startswith("Aprendiendo")) #Inicia con algo en especifico
print(text.endswith("on")) #Inicia con algo en especifico
print(text.replace("Python", "C++"))

text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize()) #Pone la primer eltra enmayuscula
print(text_2.title()) #primer letra de cada palabra en mayusucla
print(text_2.isdigit())
print("222".isdigit())