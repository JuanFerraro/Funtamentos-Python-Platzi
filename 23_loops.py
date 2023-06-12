matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    for columna in fila:
       print(columna)

x = 0
y = 0
while x < 20:
    if x < 10:
        print('x' * x)
    else:
        print('x' * (x - y))
        y +=2
    x += 1
     

