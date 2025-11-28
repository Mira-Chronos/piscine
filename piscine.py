#   
#   
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = []
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        personne = input("Qui nage ? ")
        nage = input("quelle nage ? ")
        longueur = input("combien de longueur ? ")
        date = input("Quel jour ? YY_MM_DD")
        liste.append((personne,nage,longueur,date))
   
    if commande == 'liste':
        for personne, nage, longueur, date in liste:
            print(f"Prénom {personne}, nage {nage}, longueur {longueur},Date {date}")

    if commande == 'nage':
        n=input("Quelle nage ?")
        for personne, nage, longueur, date in liste:
            if nage == n:
                print(f"Prénom:{personne},longueur {longueur},Date {date}")

    if commande == 'nageur':
        na = input("Qui?")
        for personne, nage, longueur, date in liste:
            if personne == na:
                print(f"Nage: {nage}, longueur: {longueur}, Date: {date}")

    if commande == 'date':
        da=input("Quelle date?")
        for elt in list:
            if elt[3] == da:
                print(f"Prénom {elt[0]},nage {elt[1]},")