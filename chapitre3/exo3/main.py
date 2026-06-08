print(" Bienvenu(e) ".center(44, "*"), "\n")
print(
    "Un tautogramme est un jeu poétique où \npour faire des phase, on ne se sert que de mots\ncommençant par la même lettre.\n"
)
print("*" * 44, "\n")
print(
    "Le prémier programme nous permet de \nvérifier si une chaine de caractère est un \ntautogramme.\n"
)

print("*" * 44, "\n")

chaine_user = input("Entrer votre phrase pour une vérification : ".center(44))
chaine_user = chaine_user.lower()
indice = chaine_user[0]
print(indice)
