import csv
import time
import psutil
import pandas as pd


def earnings_calculation(path):
    """
    Calcule le gain par action et modifie csv en ajoutant 1 colonne earning
    Args :  chemin d'accès du fichier csv en paramètre
    """
    datas = pd.read_csv(path)
    datas["earning"] = (datas.price * datas.profit) / 100
    datas.to_csv(path, index=False)


def shares_to_list(path):
    """
    Crée une liste d'actions à partir du csv donné
    Args : chemin d'accès du fichier csv
    Return :  une liste de dictionnaires à partir du csv
    """
    with open(path, "r") as file:
        shares_list = []
        reader = csv.DictReader(file)
        for row in reader:
            shares_list.append(row)
    return shares_list


def calculate_RAM_and_time(function):
    """
    Args : fonction sur laquelle elle servira de décorateur
    Return : Temps d'exécution et RAM utilisée par une fonction
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process()

        result = function(*args, **kwargs)

        end_time = time.time()
        time_spent = end_time - start_time

        memory_usage = process.memory_info().rss
        total_memory_usage = memory_usage / (1024*1024)
        print("---------------------------------------------------------------")
        print(f"temps d'exécution du programme : {time_spent:.2f} secondes")
        print(f"Mémoire utilisée : {total_memory_usage} MiB")
        print("---------------------------------------------------------------")
        return result
    return wrapper


def shares_profits_costs(combinaison):
    """
    Args :  une combinaison d'actions
    Return : coût et gain d'une combinaison
    """
    price = 0
    earning = 0
    for share in combinaison:
        price += float(share["price"])
        earning += float(share["earning"])
    return price, earning
