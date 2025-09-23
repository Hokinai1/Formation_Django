# les boucles en 



# Boucle for : pour une valeur de départ (1)......jusqu'a une valeur d'arrivée (5)

# for num_client in range(1, 10):
#     print(f"Vous êtes le client n° {num_client}")
    
    
# Boucle for each : pour chaque valeur d'une liste donnée

# liste des eamil
emails =["hokinaiesso@gmail.com", "coordinateurtg0159@gmail.com", "louis.infoweb@gmail.com", "hokinaimichee@gmail.com"]
# pour xhacune des valeur on affiche le texte : email envoyé à plus le mail
# parcourir une liste en recuperant des valeur
# for email in emails :
#     print(f"Rapport envoyé par mail à l'addresse : {email}")
    
    
   
#    for avec continue et break
# on a une liste de mails les certaisnmaile sint dans la litse noir  avec la boucle on va parourir le liste et qund on arrigne sur un mail qui est dans liste noir on aura un message
# avec continue la boucle va contunuer a pourcourir le reste de la liste
# avec break la boucle va s'arreter
  
allemails = [
    "alice.dupont@example.com",
    "bob.martin@example.com",
    "charlie.leroy@example.com",
    "diane.moreau@example.com",
    "eric.bernard@example.com",
    "fanny.roger@example.com",
    "georges.petit@example.com",
    "helene.roche@example.com",
    "isaac.fontaine@example.com",
    "julie.benoit@example.com"
]

liste_noir  = [
   
    "diane.moreau@example.com",
    "eric.bernard@example.com",
    "fanny.roger@example.com",
    "georges.petit@example.com",
    "helene.roche@example.com",
  
]

for allemail in allemails : 
    
    if allemail in liste_noir:
        print(f"Email {allemail} Alert! Envoi impossible...".format(allemail))
        # continue
        break
    print(f"Email envoyé à : {allemail}")




# boucle while : tant qu'une condition est vrai

salaire = 1000
# tant que le salaire < 2000$ il aura une augmentation de 150$
while salaire < 2000 : 
    
    # ajouter 150$ au salaire
    
    salaire +=150 #salaire = salaire + 150
    
    # afficher le resultat
    
    print(f"Votre salaire actuel est de : {salaire} $")
    
print(f"Fin du programme")
    
    