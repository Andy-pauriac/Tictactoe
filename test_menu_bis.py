def main_menu(play_pvp_callback):
    while True:
        print("\n=== TIC-TAC-TOE MENU ===")
        print("1. Play vs Player")
        print("2. Play vs Computer")
        print("3. Rules")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            play_pvp_callback()    # call the game

        elif choice == "2":
            print("AI mode not implemented yet.")
            input("Press ENTER to return...")

        elif choice == "3":
            show_rules()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Try again.")


def show_rules():
    print("\n--- RULES ---")
    print("1. The game is played on a 3x3 grid.")
    print("2. Player 1 is X, Player 2 or AI is O.")
    print("3. First to get 3 in a row wins!")
    print("4. If the grid is full = draw")
    input("\nPress ENTER to return...")
