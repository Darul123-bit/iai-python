# voici le programme determinant si un nombre est premier ou pas

# Consigne: un nombre est premier ssi il € à N et est supérieur à 1 et qui n'a aucun diviseur positif autre que 1 et lui-même.
import math as m
# notre nombre est 'nbr' on le declare en l'initialisant à '1'

nbr = 1


# L'utilisateur va taper des valeurs et ces valeurs vont être vérifiées sinon il retape à nouveau la valeur


def verifNombre(nombre):
    if isinstance(nbr, int):
        if (nombre > 0):
            print("Le nombre entrer est bien un enier positif.\n")
        else:
            print("Votre nombre est négatif nous ne pouvons donc pas déterminer s'il est premier ou non.\n")
            print("Merci de réessayer !\n")
    elif isinstance(nombre, (float)):
        print("Désolé mais votre nombre est un 'float' il n'est donc pas premier.")
        print("Veuillez réessayer en entrant un nombre entier positif !")
    elif isinstance(nombre, str):
        print("Vous avez entrer un lettre")
        print("Votre saisi est incorrect\nEssayer avec un entier positif !")
    else:
        print("Erreur")    

# AFFICHAGE A L'UTILISATEUR

print("**********************************************")
nbr = int(input("Veuillez enter le nombre à vérifier : "))    

verifNombre(nbr)

if (nbr <= 1):
    print("Le nombre n'est pas premier")
elif (nbr == 3):
    print("Le nombre est premier")
elif (nbr == 2):
    print("Le nombre est premier")
elif (nbr > 3):
    if (nbr % 2 == 0):
        end = int(m.sqrt(nbr) + 1)
        print("Le nombre n'est pas premier")
    for i in range(3, end, 2):
        
else:
    print("Une erreur est survenue\nVeuillez réessayer plutard")