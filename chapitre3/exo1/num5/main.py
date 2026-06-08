#
#
print("\n", " Bienvenu(e) ".center(36, "*"), "\n")
user_number = int(input("Veuillez entrer un nombre : "))
print("\n")

for i in range(0, 13):
    print(f"{user_number:>3} * {i:>2} = {user_number * i:>4}")

# Table des nombres de 0 à un nombre donner par le user
