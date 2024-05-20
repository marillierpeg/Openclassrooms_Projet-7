from modules.base import shares_profits_costs, calculate_RAM_and_time, shares_to_list, earnings_calculation

import itertools


def combinaisons_list(shares_list):
    """
    Args : liste des actions
    Return : liste de toutes les combinaisons possibles
    """
    n = len(shares_list)
    all_combinations = []
    for i in range(1, 2 ** n):
        # Chaque entier i représente une combinaison unique
        # On parcourt tous les entiers i de 0 à 2^n-1 (n-1 pour ne pas prendre en compte la combinaisons vide)
        # La première combinaison prise en compte sera 000...01 (n-1 chiffres 0 suivis d'un chiffre 1)
        combination = []
        for j in range(0, n):
            if (i >> j) & 1:
                # pour chaque entier on vérifie la valeur de chaque bit avec
                # L'opérateur ">>" qui permet le décalage vers la droite et
                # L'opérateur & qui vérifie bit à bit
                combination.append(shares_list[j])
                # Si le bit est à 1 l'élément est ajouté à la liste combination
        all_combinations.append(combination)
    print("Nombre de combinaisons possibles : ", len(all_combinations))
    return all_combinations


def combinaisons_list_alt(shares_list):
    """
    Args : la liste des actions
    Return : liste de toutes les combinaisons possibles
    """
    n = len(shares_list)
    all_combinations = []
    for i in range(1, n+1):
        for combination in itertools.combinations(shares_list, i):
            all_combinations.append(list(combination))
    print("Nombre de combinaisons possibles avec itertools : ", len(all_combinations))
    return all_combinations


@calculate_RAM_and_time
def best_combination(combination_list):
    """
    Args : liste de toutes les combinaisons possibles
    Return : meilleure combinaison qui respecte les contraintes
    """
    # Contraintes :
    # Chaque action ne peut être achetée qu'une seule fois.
    # Nous ne pouvons pas acheter une fraction d'action.
    # Nous pouvons dépenser au maximum 500 euros par client.
    best_combination = []
    budget = 500
    best_earning = 0
    best_price = 0
    best_shares = []
    for combination in combination_list:
        price, earning = shares_profits_costs(combination)
        if price <= budget and earning > best_earning:
            best_combination = combination
            best_earning = earning
            best_price = price
    for combinations in best_combination:
        best_shares.append(combinations["name"])
    print(f"Meilleure combinaison pour un budget de {budget} € :")
    print(best_shares)
    print(f"Coût total de cette combinaison : {best_price} €")
    print(f"Gain total de cette combinaison : {round(best_earning, 2)} €")
    return best_combination, best_earning, best_price


def display_bruteforce_solution1(path):
    print("Lancement du programme")
    new_path = earnings_calculation(path)
    shares_list = shares_to_list(new_path)
    all_combinaisons_list = combinaisons_list(shares_list)
    best_combination(all_combinaisons_list)


def display_bruteforce_solution2(path):
    print("Lancement du programme")
    new_path = earnings_calculation(path)
    shares_list = shares_to_list(new_path)
    all_combinaisons_list = combinaisons_list_alt(shares_list)
    best_combination(all_combinaisons_list)
