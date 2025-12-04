def main_menu(play_pvp_callback):
    while True:
        print("\n=== MENU ===")
        print("1. Jouer contre un autre joueur")
        print("2. Jouer contre l'ordinateur")
        # print("3. Rules")
        print("3. Quitter")

        choice = input("choisis une option (1-3): ")

        if choice == "1":
            play_pvp_callback()    # call the game

        elif choice == "2":
            print("MODE NON INPLANTÉ")
            input("ENTRER pour continuer")

        # elif choice == "3":
        #     show_rules()

        elif choice == "3":
            print("AU REVOIR")
            break

        else:
            print("Entré invalide , veuillez réessayer .")


# def show_rules():
#     print("\n--- RULES ---")
#     print("1. The game is played on a 3x3 grid.")
#     print("2. Player 1 is X, Player 2 or AI is O.")
#     print("3. First to get 3 in a row wins!")
#     print("4. If the grid is full = draw")
#     input("\nPress ENTER to return...")
