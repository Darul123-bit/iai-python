# Ici nous aurons un système de reservation de billets
# Ajout des bibliothèques de python
import math as m
import sys
from datetime import datetime

# Déclaration de variables

age = 0
estEtudiant = False

# Fonction de vérification de l'âge

def verifAge(nombre):
    if (age <= 0):
        retour = False
    elif (age <= 12):
        retour = False
    else:
        retour = True

    return retour

# Affichage de début du programme

print("****************************************************")
print("Bienvenu(e) sur la platforme de reservation de CANAL\nOLYMPIA.")
print("****************************************************")



# Boucle principal de la fonction
restart = True

while (restart):
    age = int(input("Veuillez entrer votre âge : "))

    # On affecte l'âge à 'conditionAge'
    conditionAge = verifAge(age)
    date = datetime.now().hour

    # On vérifie d'abord l'âge
    if (conditionAge):
        # On vérifie l'heure de reservation
        datE = input("Veuillez entrer l'heure s'il s'agit d'une reservation\nSinon laisser le champ vide : ")

        if (datE == ''):
            pass
            
        elif (datE != ''):
            if (datE < 12):
                if (estEtudiant):
                    print("Vous avez une double réduction donc \nvous aurez à payer 2500 FCFA")
                else:
                    print("Vous avez une réduction de 1000 FCFA")
                    print("Vous aurez donc à payer 4000 FCFA")
            elif (12 < datE < 20):
                if (estEtudiant):
                    print("Vous avez une réduction de 1500 FCFA")
                    print("Vous aurez donc à payer une somme de 3500 FCFA")
                else:
                    print("Vous devez payer 5000 FCFA")


    # Elaboration de la condition de fin
    endCondition = input("Taper 'q' pour quitter et toute autre chose pour reprendre : ")
    if (endCondition == 'q' or endCondition == 'Q'):
        restart = False

    # Fin de la boucle




