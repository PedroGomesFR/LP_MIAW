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

"""
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
