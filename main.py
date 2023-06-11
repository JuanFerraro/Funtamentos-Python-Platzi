import random

while True:
    user_option = input("Elige tu opcion: \n    Piedra\n    Papel \n    Tijera\nOpcion: ")
    user_option = user_option.lower()
    if not (user_option in ["papel", "tijera", "piedra"]):
        print("Reescribe de nuevo tu opcion")
    else:
        break

computer_option = random.choice(["papel", "tijera", "piedra"])

print("*" * 5, "RESULTADOS", "*" * 5)

if user_option == computer_option:
    print(f"Usuario => {user_option} vs {computer_option} <= PC")
    print("EMPATE")
elif (user_option == 'piedra' and computer_option == 'tijera') or (user_option == 'tijera' and computer_option == 'papel') or (user_option == 'papel' and computer_option == 'piedra'):
    print(f"Usuario => {user_option} vs {computer_option} <= PC")
    print("USUARIO GANA")
else: 
    print(f"Usuario => {user_option} vs {computer_option} <= PC")
    print("PC GANA")