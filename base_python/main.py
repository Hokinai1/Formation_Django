# les variables en python
nom = "Louis"
age = 12

print(f"Votre nom est {nom} et vous avez {age} ans")

# les listes en python : les structures de données qui permette de stocker plusieurs données à la fois

listes = [
    "Louis", 13, "Present",
    
    "Amah", 18, "Absent",
]

print(f"Contenu de la liste :  {listes}")

# les dictionnaires en python : le dictionnaire permet de stocker des paires (clé , valeur)
dict = {
    "nom" : "Louis",
    "age" : 35,
    "Lieu de naissance" : "Avétonou"
    
    
}

print(f"Contenu de mon dictionnaire : {dict}")

# les structure de controle en python

prenom = input("Votre prénom svp :")
age = int(input("Veillez saisir votre age :"))


if age < 15:
    print(f"{prenom},vous êtes mineur")
elif age < 18:
    print(f"{prenom},vous êtes un adolescent")
elif age == 18:
    print(f"{prenom},vous êtes un jeune")
elif age >= 20 :
    print(f"{prenom},vous êtes un adulte")
else:
    print(f"{prenom},Vous êtes vieux")