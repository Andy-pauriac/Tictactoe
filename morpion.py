import random

# ---------- Logique de base ----------

def gagnant(board, signe):
    lignes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontales
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticales
        (0, 4, 8), (2, 4, 6)              # diagonales
    ]
    for a, b, c in lignes:
        if board[a] == board[b] == board[c] == signe:
            return True
    return False

def plateau_plein(board):
    return all(c != " " for c in board)

def afficher_board(board):
    print()
    for ligne in range(3):
        print(" | ".join(board[3*ligne:3*ligne+3]))
        if ligne < 2:
            print("--+---+--")
    print()

def cases_vides(board):
    return [i for i, v in enumerate(board) if v == " "]

# ---------- IA ----------

def ordinateur(board, signe):
    ia = signe
    joueur = "O" if ia == "X" else "X"

    vides = cases_vides(board)
    if not vides:
        return False

    # 1) Jouer pour gagner
    for i in vides:
        copie = board.copy()
        copie[i] = ia
        if gagnant(copie, ia):
            return i

    # 2) Bloquer l'adversaire
    for i in vides:
        copie = board.copy()
        copie[i] = joueur
        if gagnant(copie, joueur):
            return i

    # 3) Centre, coins, côtés
    priorite = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for i in priorite:
        if i in vides:
            return i

    return random.choice(vides) if vides else False

# ---------- Modes de jeu ----------

def tour_humain(board, signe):
    while True:
        try:
            coup = int(input(f"Joueur {signe}, joue (0-8) : "))
        except ValueError:
            print("Entre un nombre entre 0 et 8.")
            continue
        if coup < 0 or coup > 8:
            print("Coup hors plateau.")
            continue
        if board[coup] != " ":
            print("Case déjà occupée.")
            continue
        board[coup] = signe
        break

def jeu_2_joueurs():
    board = [" "] * 9
    joueur = "X"

    while True:
        afficher_board(board)

        if gagnant(board, "X"):
            print("Le joueur X a gagné !")
            break
        if gagnant(board, "O"):
            print("Le joueur O a gagné !")
            break
        if plateau_plein(board):
            print("Match nul.")
            break

        tour_humain(board, joueur)
        joueur = "O" if joueur == "X" else "X"

def jeu_vs_ordi():
    board = [" "] * 9
    humain = "X"
    ia = "O"
    joueur_courant = humain

    while True:
        afficher_board(board)

        if gagnant(board, humain):
            print("Tu as gagné !")
            break
        if gagnant(board, ia):
            print("L'ordinateur a gagné.")
            break
        if plateau_plein(board):
            print("Match nul.")
            break

        if joueur_courant == humain:
            tour_humain(board, humain)
            joueur_courant = ia
        else:
            coup = ordinateur(board, ia)
            if coup is False:
                print("Aucun coup possible. Match nul.")
                break
            print(f"L'ordinateur joue en case {coup}.")
            board[coup] = ia
            joueur_courant = humain

# ---------- Menu principal ----------

def main():
    while True:
        print("=== TIC TAC TOE ===")
        print("1 - Jouer à 2 joueurs")
        print("2 - Jouer contre l'ordinateur")
        print("0 - Quitter")

        choix = input("Votre choix : ")
        if choix == "1":
            jeu_2_joueurs()
        elif choix == "2":
            jeu_vs_ordi()
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
