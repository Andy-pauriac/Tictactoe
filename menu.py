def main_menu(play_pvp_callback):
    while True:
        print("\n=== MENU ===")
        print("1. Jouer contre un autre joueur")
        print("2. Jouer contre l'ordinateur")
        print("3. Quitter")

        choice = input("choisis une option (1-3): ")

        if choice == "1":
            play_pvp_callback()    # call the game

        elif choice == "2":
            print("MODE NON INPLANTÉ")
            input("ENTRER pour continuer")

        elif choice == "3":
            print("AU REVOIR")
            break

        else:
            print("Entré invalide , veuillez réessayer .")


