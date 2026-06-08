# Ici nous aurons un système de reservation de billets
import math as m
import sys
from datetime import datetime

def verifAge(age):
    if age < 12:
        print("Vous n'êtes pas élégible")
        print("Le film est déconseillé au moins de 12 ans")
        verdict = False
    else:
        verdict = True
    return verdict

print("Bonjour bienvenu au service de reservation")
ageEntree = int(input("Veuillez enter votre âge : "))
estEtudiant = False
if verifAge(ageEntree):
    print("Vous êtes éligible")
    # ici nous allons vérifier l'heure
    estEtudianT = input("Êtes-vous etudiant(e) ? Si oui taper 'O' : ")
    if estEtudianT == 'o' or estEtudianT == 'O':
        estEtudiant = True
    heureActuelle = datetime.now().hour
    if (0 < heureActuelle < 12):
        if estEtudiant:
            print("Vous avez une réduction de 2500 F CFA")
            print("Vous avez à payer 2500 F CFA")
        else:
            print("Vous avez une réduction de 1000 F CFA")
            print("Vous aurez à payer 3000 F CFA pour votre ticket")

        
    else:
        if estEtudiant:
            print("Vous aurez à payer 3500 F CFA")
        else:
            print("Vous aurez à payer 4000 F CFA pour votre ticket")


