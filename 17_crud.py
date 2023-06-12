# CRUD Create, Read, Update and Delete
# Create
numbers = [1, 2, 3, 4, 5]
numbers_1 = [6, 7, 8, 9, 10]
print(numbers[1])

# Update
numbers[-1] = 10
print(numbers)

# Add end
numbers.append(20)
print(numbers)

# Add anywhere
numbers.insert(3, 'treinta')
print(numbers)

new_list = numbers + numbers_1
print(new_list)

# Preguntar donde esta un elemento
pos = new_list.index("treinta")
new_list[pos] = "cambio"
print(new_list)

# Delete
new_list.remove("cambio")
print(new_list)
# Delete last one
new_list.pop()  # Tambien sirve para eliminar por posicion por parametro
print(new_list)
new_list.pop(0)
print(new_list)

# Al reves
new_list.reverse()
print(new_list)

# Organizar
new_list.sort()
print(new_list)
str_list = ["hola", "como", "estas", "tu", "?"]
str_list.sort()
print(str_list)