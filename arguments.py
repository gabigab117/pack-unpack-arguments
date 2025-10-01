def foo_complet(
    arg,                    # 1. Positionnel obligatoire
    arg2,                   # 1. Positionnel obligatoire
    arg3="défaut",          # 2. Positionnel avec défaut
    *args,                  # 3. Positionnels variables
    option="Oui",           # 4. Keyword-only avec défaut
    obligatoire_kw,         # 5. Keyword-only SANS défaut (obligatoire)
    **kwargs                # 6. Keyword variables
):
    print(f"1. Positionnels obligatoires: arg={arg}, arg2={arg2}")
    print(f"2. Positionnel avec défaut: arg3={arg3}")
    print(f"3. *args (positionnels variables): {args}")
    print(f"4. Keyword-only avec défaut: option={option}")
    print(f"5. Keyword-only obligatoire: obligatoire_kw={obligatoire_kw}")
    print(f"6. **kwargs (keyword variables): {kwargs}")

# Utilisation
foo_complet(
    "A",                           # arg
    "B",                           # arg2
    "C",                           # arg3 (ou utilise défaut)
    "D", "E",                      # *args
    option="Non",                  # keyword-only
    obligatoire_kw="REQUIS",       # keyword-only obligatoire
    extra1="X",                    # **kwargs
    extra2="Y"                     # **kwargs
)


# On peut nommer les arguments positionnels mais après plus de positionnels possibles
# Tout garder en positionnel jusque *args
# Ou si on nomme tout avant *args, plus de positionnels possibles


# Exemple 1: utiliser un astérisque seul (*) comme séparateur
def exemple_separateur(a, b, *, verbose=False, mode="standard"):
    """
    Ici le seul '*' force 'verbose' et 'mode' à être keyword-only.
    On ne peut pas les fournir positionnellement.
    """
    print(f"a={a}, b={b}, verbose={verbose}, mode={mode}")

# Appels valides :
exemple_separateur(1, 2, verbose=True, mode="rapide")
# Appel invalide (provoque TypeError) :
# exemple_separateur(1, 2, True, "rapide")  # <-- interdit


# Exemple 2: forcer que tous les paramètres soient keyword-only (aucun positionnel)
def config(*, timeout=30, retries=3):
    """Tous les paramètres doivent être passés par nom."""
    print(f"timeout={timeout}, retries={retries}")

# Appel valide :
config(timeout=10, retries=5)
# Appel invalide :
# config(10, 5)  # <-- TypeError
