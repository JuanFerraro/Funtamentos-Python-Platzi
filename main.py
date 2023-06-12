import random

opciones = ("papel", "tijera", "piedra")
rounds = 0
user_wins = 0
pc_wins = 0
tie = 0

# Reglas:
print('Reglas:\nGana el mejor de 2 en 3 rondas.')

while user_wins < 2 and pc_wins < 2:
    rounds +=1

    # Ingreso por usuario
    while True:
        user_option = input(
            "Elige tu opcion: \n    Piedra\n    Papel \n    Tijera\nOpcion: ")
        user_option = user_option.lower()
        if not (user_option in opciones):
            print("Reescribe de nuevo tu opcion")
        else:
            break


    print('*' * 25)
    # Aleatorio para pc
    computer_option = random.choice(opciones)

    print("*" * 8, f"RONDA {rounds}", "*" * 8)

    if user_option == computer_option:
        print(f"Usuario => {user_option} vs {computer_option} <= PC")
        print("EMPATE")
        tie += 1
    elif (user_option == 'piedra' and computer_option == 'tijera') or (user_option == 'tijera' and computer_option == 'papel') or (user_option == 'papel' and computer_option == 'piedra'):
        print(f"Usuario => {user_option} vs {computer_option} <= PC")
        print("USUARIO GANA")
        user_wins += 1
    else:
        print(f"Usuario => {user_option} vs {computer_option} <= PC")
        print("PC GANA")
        pc_wins += 1
    print('*' * 25)

print('*' * 25)
print(f"MARCADOR FINAL:\nUSUARIO: {user_wins}\nPC: {pc_wins}\nEMPATES: {tie}")
if user_wins > pc_wins:
    print('USUARIO GANADOR')
else:
    print('PC GANA')

