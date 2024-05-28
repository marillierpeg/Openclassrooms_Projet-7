from modules.base import shares_to_list, calculate_RAM_and_time, earnings_calculation


@calculate_RAM_and_time
def best_combination(shares_list, budget):
    """
    Utilisation de la programmation dynamique pour déterminer la meilleure combinaison
    Args : liste d'actions, budget max
    Return : meilleure combinaison d'actions avec le budget donné
    """

    number_of_shares = len(shares_list)
    # Initialiser une liste à 2 dimensions pour stocker les résultats intermédiaires
    results = [[0 for _ in range(budget + 1)] for _ in range(number_of_shares + 1)]
    # Initialiser une liste à 2 dimensions pour stocker les actions sélectionnées pour chaque budget
    chosen_shares = [[[] for _ in range(budget + 1)] for _ in range(number_of_shares + 1)]

    for i in range(0, number_of_shares):
        # Pour chaque action
        share = shares_list[i]
        # Obtenir le prix et le profit de l'action
        share_price = int(share.get("price"))
        share_earning = int(share.get("earnings"))

        # Pour chaque valeur du budget
        for j in range(1, budget):
            # On vérifie que le prix de l'action courante est inférieur au budget courant
            if share_price <= j:
                # Si oui, on vérifie si son profit est plus intéressant
                if share_earning + results[i][j - share_price] > results[i][j]:
                    # Si c'est le cas on met à jour le budget en y soustrayant le prix de l'action
                    results[i + 1][j] = share_earning + results[i][j - share_price]
                    # On ajoute l'action à la liste d'actions sélectionnées
                    chosen_shares[i + 1][j] = chosen_shares[i][j - share_price] + [share.get("name")]
                else:
                    # Si l'action courante n'est pas assez rentable, on met à jour les valeurs
                    results[i + 1][j] = results[i][j]
                    chosen_shares[i + 1][j] = chosen_shares[i][j]
            else:
                # Si l'action courante n'entre pas dans le budget, on met à jour les valeurs
                results[i + 1][j] = results[i][j]
                chosen_shares[i + 1][j] = chosen_shares[i][j]

    # On obtient la combinaison la plus rentable qui tient compte du budget imposé
    best_combination = chosen_shares[number_of_shares][budget - 1]
    return best_combination


def earning_cost(shares_list, budget):
    best_shares_combination = best_combination(shares_list, budget)
    earning = 0
    cost = 0
    for best_share in best_shares_combination:
        for share in shares_list:
            if share["name"] == best_share:
                earning += float(share["earnings"])
                cost += float(share["price"])
                break
    earning = earning / 100
    cost = cost / 100

    return best_shares_combination, cost, earning


def display_optimized_solution(path):
    print("Lancement du programme")
    new_path = earnings_calculation(path)
    shares_list = shares_to_list(new_path)
    best_shares_combination, cost, earning = earning_cost(shares_list, 500*100)
    print(f"La meilleure combinaison d'achat est la suivante : {best_shares_combination}")
    print(f"Cette combinaison a un coût total de  {cost}€ et rapportera {earning}€")
    print("---------------------------------------------------------------")
