while True:
    print("\n--- Calculatrice ---")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Choisissez une opération (1-5) : ")

    if choix == '5':
        print("Au revoir !")
        break

    # Entrée des nombres
    try:
        nombre_1 = float(input("Entrez le premier nombre : "))
        nombre_2 = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        continue

    # Traitement selon le choix
    if choix == '1':
        print("Résultat :", nombre_1 + nombre_2)
    elif choix == '2':
        print("Résultat :", nombre_1 - nombre_2)
    elif choix == '3':
        print("Résultat :", nombre_1 * nombre_2)
    elif choix == '4':
        if nombre_2 != 0:
            print("Résultat :", nombre_1 / nombre_2)
        else:
            print("Erreur : division par zéro.")
    else:
        print("Choix invalide, veuillez réessayer.")