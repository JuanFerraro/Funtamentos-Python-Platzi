if True:
    print("this line must be executing")

if False:
    print("this line must not be executing")

pet = input("Which is your favorite pet?: ")

if pet == "dog":
    print("Doggies are cool and loyal")
elif pet == "cat":
    print("Cats are ... Cats")
elif pet == "fish":
    print("Fish are quiet")
else:
    print("Your is pet is unknow for me :O")

stock = int(input("STOCK: "))

if stock >= 100 and stock <= 1000:
    print("Stock is correct")
else:
    print("Stock is not correct")