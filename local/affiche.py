import local.ledArduino
import dicoMatrice2D

print("Quelle lettre afficher ?")
lettre = input(">>> ")
matrice = dicoMatrice2D.dico2D[lettre]

for ligne in matrice:
    print(ligne)
local.ledArduino.ledMatrice(matrice)