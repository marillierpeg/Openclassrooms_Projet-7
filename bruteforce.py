import csv
import itertools
import time
import psutil
import os
import pandas as pd


datas_path = "./datas/data1.csv"


def earnings_calculation(path):
    """calculer le gain par action et modifie csv en ajoutant 1 colonne earning
    prend le chemin d'accès du fichier csv en paramètre"""
    datas = pd.read_csv(path)
    datas["earning"] = (datas.price * datas.profit) / 100
    datas.to_csv(path, index=False)


def create_shares_list(path):
    """retourne une liste de dictionnaires à partir du csv
    prend le chemin d'accès du fichier csv en paramètre"""
    with open(path, "r") as file:
        shares_with_benefit = []
        reader = csv.DictReader(file)
        for row in reader:
            shares_with_benefit.append(row)
    return shares_with_benefit


def calculate_RAM_and_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process(os.getpid())
        base_memory_usage = process.memory_info().rss

        result = function(*args, **kwargs)

        end_time = time.time()
        time_spent = end_time - start_time

        memory_usage = process.memory_info().rss
        total_memory_usage = (memory_usage - base_memory_usage) / (1024*1024)

        print(f"temps de réalisation du programme : {time_spent:.2f} secondes")
        print(f"Mémoire utilisée : {total_memory_usage} Mio")
        return result
    return wrapper


@calculate_RAM_and_time
def combinaisons_list(shares_list):
    """Retourne une liste de toutes les combinaisons possibles
    prend en paramètre la liste des actions"""
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


@calculate_RAM_and_time
def combinaisons_list_alt(shares_list):
    """Retourne une liste de  toutes les combinaisons possibles
    prend en paramètre la liste des actions"""
    n = len(shares_list)
    all_combinations = []
    for i in range(1, n+1):
        for combination in itertools.combinations(shares_list, i):
            all_combinations.append(list(combination))
    print("Nombre de combinaisons possibles avec itertools : ", len(all_combinations))
    return all_combinations


def shares_profits_costs(combinaison):
    """prend en paramètre une combinaison
    retourne coût et gain d'une combinaison"""
    price = 0
    earning = 0
    for share in combinaison:
        price += float(share["price"])
        earning += float(share["earning"])
    return price, earning


def best_combinaison(combination_list):
    """Prend en paramètre la liste de toutes les combinaisons possibles
    Retourne la meilleure combinaison qui respecte les contraintes"""
    # Contraintes :
    # Chaque action ne peut être achetée qu'une seule fois.
    # Nous ne pouvons pas acheter une fraction d'action.
    # Nous pouvons dépenser au maximum 500 euros par client.
    best_match = []
    budget = 500
    best_earning = 0
    best_price = 0
    for combination in combination_list:
        price, earning = shares_profits_costs(combination)
        if price <= budget and earning > best_earning:
            best_match = combination
            best_earning = earning
            best_price = price
    print(best_match)
    return best_match, best_earning, best_price


earnings_calculation(datas_path)
all_combinaisons_list = combinaisons_list(create_shares_list(datas_path))
all_combination_list_alt = combinaisons_list_alt(create_shares_list(datas_path))
best_combinaison(all_combinaisons_list)
best_combinaison(all_combination_list_alt)
