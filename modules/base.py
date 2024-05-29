import csv
import time
import psutil
import pandas as pd


def earnings_calculation(path):
    """
    Calcule le gain par action et crée un csv en ajoutant 1 colonne earning
    Args :  chemin d'accès du fichier csv en paramètre
    """
    data = pd.read_csv(path)
    raw_shares_list = data.to_dict(orient='records')
    # convertit ce DataFrame en une liste de dictionnaires
    # Chaque clé du dictionnaire correspond à un nom de colonne dans le DataFrame.
    # La valeur associée à chq clé est une liste contenant les valeurs de cette colonne pour toutes les lignes.
    filtered_shares_list = []
    for share in raw_shares_list:
        if float(share['price']) > 0 and float(share['profit']) > 0:
            share["price"] = int(round(float(share["price"]) * 100, 0))
            share["earnings"] = int(round(float(share["price"]) * float(share["profit"]) / 100))
            filtered_shares_list.append(share)

    new_path = path[:-4] + "_ouptput.csv"
    df = pd.DataFrame(filtered_shares_list)
    df.to_csv(new_path, index=False, float_format="%.0f")
    return new_path


def shares_to_list(output_path):
    """
    Crée une liste d'actions à partir du csv donné
    Args : chemin d'accès du fichier csv
    Return :  une liste de dictionnaires à partir du csv
    """
    with open(output_path, "r") as file:
        shares_list = []
        reader = csv.DictReader(file)
        for row in reader:
            shares_list.append(dict(row))
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
        print(f"Mémoire utilisée : {total_memory_usage} Mio")
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
        earning += float(share["earnings"])
    return price, earning
