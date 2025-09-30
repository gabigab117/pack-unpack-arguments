# Pack/Unpack Arguments en Python 🐍

Ce repository contient un guide complet et des exemples pratiques sur les concepts de **packing** et **unpacking** des arguments en Python, des bases aux techniques avancées.

## 📚 Contenu

### Fichiers principaux

- **`main.py`** : Guide complet avec 9 sections couvrant tous les aspects du packing/unpacking
- **`arguments.py`** : Démonstration des différents types d'arguments dans les fonctions Python

## 🎯 Concepts couverts

### 1. Les bases : Unpacking simple
- Unpacking de tuples et listes
- Assignation multiple de variables

### 2. Unpacking avec l'opérateur * (star operator)
- Récupération du premier élément et du reste
- Récupération du dernier élément et du début  
- Isolation d'éléments du milieu

### 3. Unpacking dans les fonctions
- Unpacking d'arguments positionnels avec `*`
- Unpacking d'arguments nommés avec `**`

### 4. Packing dans les fonctions
- `*args` pour arguments positionnels variables
- `**kwargs` pour arguments nommés variables
- Combinaison des deux techniques

### 5. Unpacking dans les compréhensions
- List comprehensions avec unpacking
- Création de dictionnaires par unpacking

### 6. Techniques avancées
- Unpacking imbriqué
- Structures de données complexes

### 7. Échange de variables
- Échange sans variable temporaire
- Rotation de multiple variables

### 8. Unpacking avec objets personnalisés
- Implémentation de `__iter__`
- Implémentation de `__getitem__`

### 9. Applications pratiques
- Fonctions retournant plusieurs valeurs
- Cas d'usage réels

## 🔧 Types d'arguments Python

Le fichier `arguments.py` démontre la syntaxe complète des paramètres de fonction :

1. **Positionnels obligatoires** : `arg, arg2`
2. **Positionnels avec défaut** : `arg3="défaut"`
3. **Positionnels variables** : `*args`
4. **Keyword-only avec défaut** : `option="Oui"`
5. **Keyword-only obligatoire** : `obligatoire_kw`
6. **Keyword variables** : `**kwargs`

## 🚀 Comment utiliser

```bash
# Exécuter le guide complet
python main.py

# Voir la démonstration des types d'arguments
python arguments.py
```

## 💡 Exemples rapides

### Unpacking de base
```python
coords = (10, 20)
x, y = coords  # x=10, y=20
```

### Avec l'opérateur *
```python
nombres = [1, 2, 3, 4, 5]
premier, *reste = nombres  # premier=1, reste=[2,3,4,5]
```

### Dans les fonctions
```python
def ma_fonction(*args, **kwargs):
    # args = tuple des arguments positionnels
    # kwargs = dictionnaire des arguments nommés
    pass
```

## 🎓 Public cible

Ce repository est parfait pour :
- Les développeurs Python débutants à intermédiaires
- Ceux qui veulent maîtriser les concepts d'arguments en Python
- Les formateurs et enseignants en programmation Python
- Toute personne souhaitant approfondir sa compréhension du packing/unpacking

## 📖 Prérequis

- Python 3.6+ (pour la syntaxe moderne)
- Connaissance de base de Python (variables, fonctions, listes, dictionnaires)

---

*Ce projet est à des fins éducatives pour maîtriser les concepts fondamentaux du packing et unpacking en Python.*
