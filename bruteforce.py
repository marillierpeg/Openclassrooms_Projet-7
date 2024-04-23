import csv
import itertools
import time
import math


datas_path = "./datas/data1.csv"
output_file_path = "./datas/sortie.csv"


def earnings_calculation(path):
    """calculer le gain par action et inscrire infos dans 1 nouveau csv"""
    with open(path, "r") as data_file, open(output_file_path, "w", newline="") as output_file:
        reader = csv.reader(data_file)
        writer = csv.writer(output_file)
        header = next(reader)
        header.insert(3, "Earnings")
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
    n = len(shares_updated)
    each_combinations = []
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
        each_combinations.append(combination)

    print("Nombre de combinaisons possibles : ", len(each_combinations))
    return each_combinations


def combinaisons_list_alt(shares_updated):
    start_time = time.perf_counter()
    n = len(shares_updated)
    each_combinations = []
    for i in range(1, n+1):
        for combination in itertools.combinations(shares_updated, i):
            each_combinations.append(list(combination))
    end_time = time.perf_counter()
    print(f"{round(((end_time + start_time) / 1000000), 2)} secondes")
    print("Nombre de combinaisons possibles avec itertools : ", len(each_combinations))


earnings_calculation(datas_path)
combinaisons_list(create_shares_list(output_file_path))
combinaisons_list_alt(create_shares_list(output_file_path))