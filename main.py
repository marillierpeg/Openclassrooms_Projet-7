import bruteforce
import optimized
# import optimized


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
            bruteforce.display_bruteforce_solution1()
        elif user_choice == "2":
            bruteforce.display_bruteforce_solution2()
        elif user_choice == "3":
            optimized.display_optimized_solution()
        elif user_choice == "4":
            pass
        elif user_choice == "5":
            pass
        elif user_choice == "6":
            break
        else:
            print("Erreur de saisie")


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
