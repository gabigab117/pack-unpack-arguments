# Guide Complet du Packing/Unpacking en Python
# De la base aux techniques avancées

print("=== 1. LES BASES : UNPACKING SIMPLE ===")

# Unpacking de base avec des tuples
coords = (10, 20)
x, y = coords  # Unpacking
print(f"x = {x}, y = {y}")

# Avec des listes
fruits = ["pomme", "banane", "orange"]
a, b, c = fruits
print(f"Premier: {a}, Deuxième: {b}, Troisième: {c}")

print("\n=== 2. UNPACKING AVEC * (STAR OPERATOR) ===")

# Récupérer le premier et le reste
nombres = [1, 2, 3, 4, 5]
premier, *reste = nombres
print(f"Premier: {premier}, Reste: {reste}")

# Récupérer le dernier et le début
*debut, dernier = nombres
print(f"Début: {debut}, Dernier: {dernier}")

# Récupérer le milieu
premier, *milieu, dernier = nombres
print(f"Premier: {premier}, Milieu: {milieu}, Dernier: {dernier}")

print("\n=== 3. UNPACKING DANS LES FONCTIONS ===")

def afficher_info(nom, age, ville):
    print(f"{nom}, {age} ans, vit à {ville}")

# Unpacking d'arguments positionnels
personne = ("Patrick", 70, "Ons en Bray")
afficher_info(*personne)  # Équivalent à afficher_info("Patrick", 70, "Ons en Bray")

# Unpacking d'arguments nommés
def creer_profil(nom, age, ville="Non spécifiée", metier="Non spécifié"):
    return f"Profil: {nom}, {age} ans, {ville}, {metier}"

info = {"nom": "Bob", "age": 30, "ville": "Lyon", "metier": "Développeur"}
# on déballe en arguments nommés
profil = creer_profil(**info)  # Unpacking du dictionnaire
print(profil)

print("\n=== 4. PACKING DANS LES FONCTIONS ===")

# *args pour un nombre variable d'arguments positionnels
def somme(*nombres):
    return sum(nombres)

print(f"Somme: {somme(1, 2, 3, 4, 5)}")

# **kwargs pour un nombre variable d'arguments nommés
def config_django(**options):
    return options

config = config_django(debug=True, key="ma_cle", allowed_hosts=["localhost"])
print(f"Config: {config}")
# ou
ma_config = {"debug": True, "key": "ma_cle", "allowed_hosts": ["localhost"]}
config = config_django(**ma_config)
print(f"Config via dict: {config}")

# Combinaison des deux
def combiner(obligatoire, *args, **kwargs):
    print(f"Argument obligatoire: {obligatoire}")
    print(f"Arguments positionnels supplémentaires: {args}")
    print(f"Arguments nommés: {kwargs}")

combiner("test", 1, 2, 3, nom="Patrick", age=70)
combiner_infos = {"nom": "Roger", "age": 30}
combiner("test_bis", 4, 5, 6, **combiner_infos)

print("\n=== 5. UNPACKING DANS LES COMPRÉHENSIONS ===")

# Unpacking dans les list comprehensions
points = [(1, 2), (3, 4), (5, 6)]
distances = [x**2 + y**2 for x, y in points]
print(f"Distances au carré: {distances}")

# Unpacking avec dictionnaires
personnes = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
ages = {nom: age for nom, age in personnes}
ages_bis = dict(personnes)  # Méthode alternative
print(f"Dictionnaire des âges (méthode bis): {ages_bis}")
print(f"Dictionnaire des âges: {ages}")

print("\n=== 6. TECHNIQUES AVANCÉES ===")

# Unpacking imbriqué
donnees = [("Patrick", (70, "Ons en Bray")), ("Roger", (30, "Beauvais"))]
for nom, (age, ville) in donnees:
    print(f"{nom}: {age} ans, {ville}")

# print([f"{nom} a {age} ans et habite à {ville}" for nom, (age, ville) in donnees])

print("\n=== 7. UNPACKING POUR L'ÉCHANGE DE VARIABLES ===")

# Échange de variables sans variable temporaire
a, b = 10, 20
print(f"Avant échange: a={a}, b={b}")
a, b = b, a  # Échange élégant
print(f"Après échange: a={a}, b={b}")

# Rotation de plusieurs variables
x, y, z = 1, 2, 3
print(f"Avant rotation: x={x}, y={y}, z={z}")
x, y, z = z, x, y  # Rotation
print(f"Après rotation: x={x}, y={y}, z={z}")

print("\n=== 8. UNPACKING AVEC DES STRUCTURES COMPLEXES ===")

# Unpacking avec des objets personnalisés
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    # d'abord iter, si n'est pas défini, essaye getitem
    def __iter__(self):
        return iter((self.nom, self.age))

patrick = Personne("Patrick", 25)
nom, age = patrick  # Fonctionne grâce à __iter__
print(f"Personne: nom={nom}, age={age}")

class PersonneBis:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __getitem__(self, index):
        # ce qui permet d'accéder via l'index, sinon pas possible
        return (self.nom, self.age)[index]

roger = PersonneBis("Roger", 30)
nom_bis, age_bis = roger  # Fonctionne grâce à __getitem__
print(f"PersonneBis: nom={nom_bis}, age={age_bis}")

print("\n=== 9. APPLICATIONS PRATIQUES ===")

# Fonction qui retourne plusieurs valeurs
def calculer_stats(nombres):
    return min(nombres), max(nombres), sum(nombres) / len(nombres)

# Unpacking du résultat
valeurs = [10, 20, 30, 40, 50]
minimum, maximum, moyenne = calculer_stats(valeurs)
print(f"Min: {minimum}, Max: {maximum}, Moyenne: {moyenne}")