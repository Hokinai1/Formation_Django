# sujet : youtubeur : Monsieur LE SUEUR a 2500 abonnées : 
# s'il gagne 10% d'audience supplementaire par moi,
# combien aura t-il d'abonnées apres 2 ans (24 mois)

abonnes = 2500

mois = 0
while mois <= 24 :
    # +10% = 1 + (10/100): 1.10
    abonnes *=1.10  # abonnes = abonnes *1.10 
    
    print(f"Nombre total d'abonnés : {abonnes}")
    # on passe au mois suivant sinon la boucle sera infinie
    
    mois +=1
    
    


