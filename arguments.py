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
