print("Programa que dice si un numero es par o impar")

while True:
    try:
        number = int(input("Ingrese un número entero: "))
        break
    except ValueError:
        print("Error. Debe ingresar un número entero.")

if number % 2 == 0:
    print(f"El número {number} es par")
else:
    print(f"El número {number} no es par")