"""""
import math

# Quantités pour 4 personnes
farine_pour_4 = 200  # en grammes
sucre_pour_4 = 150   # en grammes
lait_pour_4 = 100    # en millilitres
beurre_pour_4 = 100  # en grammes
oeufs_pour_4 = 2     # en nombre d'œufs

# Demander à l'utilisateur pour combien de personnes il souhaite préparer le gâteau
nb_personnes = int(input("Pour combien de personnes voulez-vous préparer le gâteau ? "))

# Calcul des nouvelles quantités
proportion = nb_personnes / 4

farine = farine_pour_4 * proportion
sucre = sucre_pour_4 * proportion
lait = lait_pour_4 * proportion
beurre = beurre_pour_4 * proportion
oeufs = math.ceil(oeufs_pour_4 * proportion)  # Arrondir au supérieur pour les œufs

# Affichage des quantités adaptées
print(f"Pour {nb_personnes} personnes, il vous faut :")
print(f"{farine:.2f} g de farine")
print(f"{sucre:.2f} g de sucre")
print(f"{lait:.2f} ml de lait")
print(f"{beurre:.2f} g de beurre")
print(f"{oeufs} œufs (arrondi au supérieur)")



# Demander l'âge de l'utilisateur
age = int(input("Entrez votre âge : "))

# Vérifier la catégorie d'âge
if age < 12:
    print("Catégorie : Enfant")
elif 12 <= age <= 17:
    print("Catégorie : Adolescent")
elif 18 <= age <= 64:
    print("Catégorie : Adulte")
else:
    print("Catégorie : Senior")


revenue = int(input("Entrez votre revenue annuelle: "))

if revenue <= 10000 : 
    print("vous payer 0%")
elif 10001 <= revenue <= 25000 : 
    print("vous payer 10%")
elif 25001 <= revenue <= 50000 :
    print("vous payer 20%")
elif revenue > 50000 :
    print("vous payer 30%")
    
    
    
def est_bissextile(annee):
    # Une année est bissextile si elle est divisible par 4 mais pas par 100,
    # sauf si elle est aussi divisible par 400.
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def jours_dans_mois(mois, annee):
    # Retourner le nombre de jours dans un mois donné
    if mois == 2:
        if est_bissextile(annee):
            return 29  # Février bissextile
        else:
            return 28  # Février normal
    elif mois in [4, 6, 9, 11]:
        return 30  # Avril, Juin, Septembre, Novembre ont 30 jours
    else:
        return 31  # Tous les autres mois ont 31 jours

def date_valide(jour, mois, annee):
    # Vérifier si le mois est valide
    if mois < 1 or mois > 12:
        return False
    # Vérifier si le jour est valide pour le mois et l'année donnés
    jours_max = jours_dans_mois(mois, annee)
    if jour < 1 or jour > jours_max:
        return False
    return True

# Demander à l'utilisateur d'entrer une date
jour = int(input("Entrez le jour (1-31) : "))
mois = int(input("Entrez le mois (1-12) : "))
annee = int(input("Entrez l'année : "))

# Vérifier si la date est valide
if date_valide(jour, mois, annee):
    print(f"La date {jour}/{mois}/{annee} est valide.")
else:
    print(f"La date {jour}/{mois}/{annee} n'est pas valide.")

"""

i = 0
while i <= 10:
    print(i)
    i += 1 