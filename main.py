# Mon jeu Tic Tac Toe - version débutant Python
# Plateau = liste de 9 cases (0 à 8)

def afficher_plateau(board):
    print("\n--- PLATEAU ---")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def verifier_gagnant(board, signe):
    # Toutes les façons de gagner
    victoires = [
        [0,1,2], [3,4,5], [6,7,8],  # lignes
        [0,3,6], [1,4,7], [2,5,8],  # colonnes  
        [0,4,8], [2,4,6]            # diagonales
    ]
    
    for combo in victoires:
        if board[combo[0]] == signe and board[combo[1]] == signe and board[combo[2]] == signe:
            return True
    return False

def plateau_plein(board):
    for case in board:
        if case == " ":
            return False
    return True

def cases_libres(board):
    libres = []
    for i in range(9):
        if board[i] == " ":
            libres.append(i)
    return libres

# ========== FONCTION ORDINATEUR (comme demandé) ==========
def ordinateur(board, signe):
    # signe de l'ordi et du joueur
    ordi_signe = signe
    joueur_signe = "O" if signe == "X" else "X"
    
    libres = cases_libres(board)
    
    # 1. Est-ce que je peux gagner ?
    for case in libres:
        board_test = board.copy()
        board_test[case] = ordi_signe
        if verifier_gagnant(board_test, ordi_signe):
            return case
    
    # 2. Est-ce que le joueur peut gagner ? Je bloque !
    for case in libres:
        board_test = board.copy()
        board_test[case] = joueur_signe
        if verifier_gagnant(board_test, joueur_signe):
            return case
    
    # 3. Je joue au centre si possible
    if 4 in libres:
        return 4
    
    # 4. Sinon coins
    coins = [0,2,6,8]
    for coin in coins:
        if coin in libres:
            return coin
    
    # 5. N'importe où
    return libres[0]

# ========== JEU 2 JOUEURS ==========
def jeu_2_joueurs():
    board = [" "] * 9
    joueur = "X"
    
    while True:
        afficher_plateau(board)
        
        if verifier_gagnant(board, "X"):
            print("X a gagné !")
            break
        if verifier_gagnant(board, "O"):
            print("O a gagné !")
            break
        if plateau_plein(board):
            print("Egalité !")
            break
        
        # Tour du joueur
        while True:
            try:
                coup = int(input(f"Joueur {joueur}, choisis case (0-8): "))
                if coup < 0 or coup > 8:
                    print("Entre 0 à 8 !")
                    continue
                if board[coup] != " ":
                    print("Case prise !")
                    continue
                board[coup] = joueur
                break
            except:
                print("Entre un nombre !")
        
        joueur = "O" if joueur == "X" else "X"

# ========== JEU VS ORDINATEUR ==========
def jeu_vs_ordi():
    board = [" "] * 9
    humain = "X"
    ordi = "O"
    
    while True:
        afficher_plateau(board)
        
        if verifier_gagnant(board, humain):
            print("Bravo ! Tu as gagné !")
            break
        if verifier_gagnant(board, ordi):
            print("L'ordi a gagné :(")
            break
        if plateau_plein(board):
            print("Egalité !")
            break
        
        # Tour humain
        while True:
            try:
                coup = int(input("Ton coup (0-8): "))
                if coup < 0 or coup > 8 or board[coup] != " ":
                    print("Coup impossible !")
                    continue
                board[coup] = humain
                break
            except:
                print("Entre un nombre valide !")
        
        # Tour ordi
        coup_ordi = ordinateur(board, ordi)
        if coup_ordi == False:
            print("Erreur !")
            # break
        board[coup_ordi] = ordi
        print(f"L'ordi joue case {coup_ordi}")

# ========== MENU ==========
print("===TIC TAC TOE - project =====")
print("1 - 2 joueurs")
print("2 - Vs ordi")
choix = input("Choisis: ")

if choix == "1":
    jeu_2_joueurs()
elif choix == "2":
    jeu_vs_ordi()
else:
    print("Au revoir !")
