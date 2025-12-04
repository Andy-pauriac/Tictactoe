from helpers import draw_board , check_turn , check_for_win
import os
import random
import sys

########################################
#     PARTIE JOUEUR VS JOUEUR
########################################
def play_pvp():
    spots = {i:str(i) for i in range(1,10)}
    playing = True
    complete = False
    turn = 0
    prev_turn = -1

    while playing:
        os.system('cls' if os.name=='nt' else 'clear')
        draw_board(spots)

        if prev_turn == turn:
            print("Case déjà prise, rejouez.")
        prev_turn = turn

        print("Joueur " + str((turn %2)+1) + " choisit une case (ou 'q' pour quitter) :")
        choice = input()

        if choice == 'q':
            playing = False
            break

        if choice.isdigit() and int(choice) in spots:
            if spots[int(choice)] not in ["X","O"]:
                turn += 1
                spots[int(choice)] = check_turn(turn)
            else:
                prev_turn = turn

        if check_for_win(spots): playing, complete = False, True
        if turn >= 9: playing = False

    os.system('cls' if os.name=='nt' else 'clear')
    draw_board(spots)

    if complete:
        if check_turn(turn) == "X": print("Félicitations ! Joueur 1 a gagné !")
        else: print("Félicitations ! Joueur 2 a gagné !")
    else:
        print("Égalité !")

    input("\nPress ENTER pour revenir au menu...")

########################################
# JOUEUR CONTRE ORDINATEUR
########################################
def ordinateur():
    spots = {i:str(i) for i in range(1,10)}
    playing = True
    complete = False
    turn = 0
    prev_turn = -1

    os.system('cls' if os.name=='nt' else 'clear')
    print("Vous êtes Joueur 1 (X)")
    print("L'IA est Joueur 2 (O)")
    input("Appuyez sur ENTER pour commencer...")

    while playing:
        os.system('cls' if os.name=='nt' else 'clear')
        draw_board(spots)

        # Tour du joueur humain
        if turn % 2 == 0:
            if prev_turn == turn:
                print("Case déjà prise, rejouez.")
            prev_turn = turn

            print("Votre tour ! Choisissez une case (ou 'q' pour quitter) :")
            choice = input()

            if choice == 'q': playing = False; break

            if choice.isdigit() and int(choice) in spots:
                if spots[int(choice)] not in ["X","O"]:
                    turn += 1
                    spots[int(choice)] = "X"
                else:
                    prev_turn = turn
            else:
                prev_turn = turn

        # Tour IA
        else:
            empty = [k for k,v in spots.items() if v not in ["X","O"]]
            if not empty:
                playing = False
                break

            ai_choice = random.choice(empty)
            print(f"L'IA choisit la case {ai_choice}...")
            spots[ai_choice] = "O"
            turn += 1

        # Vérification victoire
        if check_for_win(spots):
            playing = False
            complete = True

        if turn >= 9:
            playing = False

    os.system('cls' if os.name=='nt' else 'clear')
    draw_board(spots)

    if complete:
        if check_turn(turn) == "X": print("le joueur à gagner !")
        else: print("Le joueur à perdu!")
    else:
        print("Match nul !")

    input("\nPress ENTER pour revenir au menu...")

########################################
# MENU DE JEU
########################################
def main_menu():
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print("\n===== MENU TIC-TAC-TOE =====")
        print("1. Joueur vs Joueur")
        print("2. Joueur vs IA")
        print("3. Quitter")

        choice = input("Choisissez une option (1-3) : ")

        if choice == "1": play_pvp()
        elif choice == "2": ordinateur()
        elif choice == "3": print("A bientôt !"); break
        else: print("Choix invalide."); input("ENTER...")

########################################
# lancement jeux
########################################
if __name__ == "__main__":
    main_menu()
