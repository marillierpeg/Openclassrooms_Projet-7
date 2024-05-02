import csv
import itertools
import time
import psutil
import os

datas_path = "./datas/data1.csv"
output_file_path = "./datas/sortie.csv"


def earnings_calculation(path):
    """calculer le gain par action et inscrire infos dans 1 nouveau csv"""
    with open(path, "r") as data_file, open(output_file_path, "w", newline="") as output_file:
        reader = csv.reader(data_file)
        writer = csv.writer(output_file)
        header = next(reader)
        header.insert(3, "earnings")
        writer.writerow(header)
        for row in reader:
            price = int(row[1])
            profit = int(row[2])
            gain = price * profit / 100
            row.insert(3, "")
            row[3] = gain
            writer.writerow(row)


def create_shares_list(path):
    """créé une liste à partir du csv de sortie"""
    with open(path, "r") as file:
        shares_with_benefit = []
        reader = csv.DictReader(file)
        for row in reader:
            shares_with_benefit.append(row)
    return shares_with_benefit


def combinaisons_list(shares_updated):
    """Liste toutes les combinaisons possibles"""
    start_time = time.time()
    n = len(shares_updated)
    all_combinations = []
    for i in range(1, 2 ** n):
        # Chaque entier i représente une combinaison unique
        # On parcourt tous les entiers i de 0 à 2^n-1 (n-1 pour ne pas prendre en compte la combinaisons vide)
        combination = []
        for j in range(0, n):
            if (i >> j) & 1:
                # pour chaque entier on vérifie la valeur de chaque bit avec
                # L'opérateur ">>" qui permet le décalage vers la droite et
                # L'opérateur & qui vérifie bit à bit
                combination.append(shares_updated[j])
                # Si le bit est à 1 l'élément est ajouté à la liste combination
        all_combinations.append(combination)
        end_time = time.time()
    print("Nombre de combinaisons possibles : ", len(all_combinations))
    print(f"{(round(end_time - start_time, 4))} secondes")
    print(f"{psutil.virtual_memory().percent}% de RAM utilisés")
    return all_combinations


def combinaisons_list_alt(shares_updated):
    start_time = time.time()
    n = len(shares_updated)
    all_combinations = []
    for i in range(1, n+1):
        for combination in itertools.combinations(shares_updated, i):
            all_combinations.append(list(combination))
    end_time = time.time()
    # p = psutil.Process()
    print("Nombre de combinaisons possibles avec itertools : ", len(all_combinations))
    print(f"{(round(end_time - start_time, 4))} secondes")
    # print(f"{p.memory_info().rss} RAM utilisés")
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB
    print('memory use:', memoryUse)
    return all_combinations


def shares_profits_costs(combinaisons):
    '''retourne coût et gain de chaque combinaison'''
    for combinaison in combinaisons:
        price = combinaison[0]["price"]
        earning = combinaison[0]["earnings"]
    return price, earning


def best_combinaison(combination_list):
    best_match = []
    budget = 500
    best_earning = 0
    best_price = 0
    price, earning = shares_profits_costs(combination_list)
    for combination in combination_list:
        if float(price) <= budget and float(earning) > float(best_earning):
            best_match = combination
            best_earning = earning
            best_price = price
    print(best_match)
    return best_match, best_earning, best_price


earnings_calculation(datas_path)
all_combinaisons_list = combinaisons_list(create_shares_list(output_file_path))
all_combination_list_alt = combinaisons_list_alt(create_shares_list(output_file_path))
best_combinaison(all_combinaisons_list)
best_combinaison(all_combination_list_alt)
