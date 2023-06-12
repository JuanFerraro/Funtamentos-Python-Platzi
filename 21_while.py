#Version 1: Infinito
""" while True:
    print('Ejecutandose') """

#Version 2:
counter = 0
while counter < 10:
    counter +=1
    print("Ejecucion ", counter)

#Version 3: Forzada
counter = 0
while counter < 20:
    counter +=1
    if counter == 15:
        break
    print(counter)

print("*"*15)

#Version 4:
counter = 0
while counter < 10:
    counter += 1
    print(counter)
    if counter < 5:
        continue    #Ignora lo que hay de ahí para abajo
    print(counter)
    print(counter)

