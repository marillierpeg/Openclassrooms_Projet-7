from modules.bruteforce import display_bruteforce_solution1, display_bruteforce_solution2
from modules.optimized import display_optimized_solution


def main():
    while True:
        print("Menu :")
        print("1. Solution bruteforce avec les données de 20 actions")
        print("2. Solution bruteforce alternative avec les données de 20 actions")
        print("3. Solution optimisée avec les données de 20 actions")
        print("4. Solution optimisée avec le dataset1")
        print("5. Solution optimisée avec le dataset2")
        print("6. Quitter le programme")

        user_choice = input("Quelle solution souhaitez vous utiliser?")

        if user_choice == "1":
            display_bruteforce_solution1("./datas/data1.csv")
        elif user_choice == "2":
            display_bruteforce_solution2("./datas/data1.csv")
        elif user_choice == "3":
            display_optimized_solution("./datas/data1.csv")
        elif user_choice == "4":
            display_optimized_solution("./datas/dataset1.csv")
        elif user_choice == "5":
            display_optimized_solution("./datas/dataset2.csv")
        elif user_choice == "6":
            break
        else:
            print("Erreur de saisie")


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
