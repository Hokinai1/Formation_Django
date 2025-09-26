
# les conditions   simple 

age = 15
sexe = "F"

if sexe == "M" :
    print(f"Bonjour Monsieur")
else : 
    print(f"Bonjour Madame")
    
    
 
#  un programme qui verifie si on a l'argent dans le protemonnaie avant l'achet d'un produit

solde = 1500
prix = 2500

if prix <= solde :
    print(f"Achat possible !")
    solde = solde - prix
else : 
    print(f"Désolé achat impossible !")
print(f"Votre solde actuel {solde} FCFA")


# verification de deux conditions

# si le solde est indefrieur au prix et le prix de l'ordinateur est supérieur à 50 000

caisse = int(input("Veilllez saisir le solde disponible :"))
materiel = int(input("Veillez saisir le prix du matériel à acheter : "))

if materiel <= caisse and materiel > 20000 :
    print(f"Opération d'achat possible !")
    caisse = caisse - materiel
else : 
    print(f"Opération impossible !")
print(f"Solde disponible : {caisse} FCFA")


# LES conditions ternaires en python



texte = ("Achat possible", "Achat impossible")[materiel <= 1000]
print("CONDITIONS TERNAIRE")
print(texte)