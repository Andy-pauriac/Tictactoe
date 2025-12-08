from helpers import draw_board , check_turn , check_for_win
import os #Permet d'interagir avec le système exploitation (exemple : effacer le contenu a l'écran )
import random #Utiliser pour que l'ordinateur choissent une case au hasard 

########################################
#     PARTIE JOUEUR VS JOUEUR
########################################
def play_pvp():
    spots = {i:str(i) for i in range(1,10)} #crée un dictionnaire qui represente les 9 cases du jeu (vide ))
    playing = True # maintient la boucle de jeu active
    complete = False #False --> True si quelqu'un gagne
    turn = 0 #compteur de tours 
    prev_turn = -1 #permet de détecter si le joueur a entrer une case invalide

    while playing:
        os.system('cls' if os.name=='nt' else 'clear') #permet de garder l'affichage propres en effaçant le contenu sur l'écran
        draw_board(spots) #affiche la grille actuel

        if prev_turn == turn:
            print("Case déjà prise, rejouez.")
        prev_turn = turn 

        print("Joueur " + str((turn %2)+1) + " choisit une case (ou 'q' pour quitter) :")
        choice = input() #demande au joueur (1 ou 2) d'entrer une case choisit

        if choice == 'q':
            playing = False
            break #permet d'arreter le jeu

        if choice.isdigit() and int(choice) in spots: #verifie si l'entrée est un chiffre et que ce chiffre est bien compris dans la liste spots
            if spots[int(choice)] not in ["X","O"]: #vérifie si la case n'est pas déja occupé par un X ou un O 
                turn += 1 #passe au tour suivant 
                spots[int(choice)] = check_turn(turn) #on marque la case avec le signe choisit
            else: 
                prev_turn = turn #si la case est déja prise , on ne passe pas au tour suivant 

        if check_for_win(spots): playing, complete = False, True #vérifie si un des joueurs a aligné 3 même symbole
        if turn >= 9: playing = False # Si le nombre de tour dépasse 9 , on déclenche un match nul

    os.system('cls' if os.name=='nt' else 'clear')
    draw_board(spots)

    if complete:
        if check_turn(turn) == "X": print("Félicitations ! Joueur 1 a gagné !") #si trois X sont alignés , le joueur 1 gagne
        else: print("Félicitations ! Joueur 2 a gagné !") #si trois O sont alignés , le joueur 2 gagne
    else:
        print("Égalité !") # au bout du 9eme tour , si aucun des joueurs n'as aligné 3 symboles , c'est égalité

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
    print("Vous êtes Joueur 1 (X)") #informe que le joueur 1 possède le symbole X 
    print("L'IA est Joueur 2 (O)") #informe que l'ordinateur possède le symbole O
    input("Appuyez sur ENTER pour commencer...") 

    while playing:
        os.system('cls' if os.name=='nt' else 'clear') 
        draw_board(spots) 

        # Tour du joueur humain
        if turn % 2 == 0: #si le tour est pair ( 0 , 2 , 4 ) alors ça signie que c'est le tour du joueur 1
            if prev_turn == turn: 
                print("Case déjà prise, rejouez.")
            prev_turn = turn

            print("Votre tour ! Choisissez une case (ou 'q' pour quitter) :")
            choice = input()

            if choice == 'q': playing = False; break

            if choice.isdigit() and int(choice) in spots: 
                if spots[int(choice)] not in ["X","O"]: #vérifie si la case n'est pas déja occupé par un X ou un O 
                    turn += 1 
                    spots[int(choice)] = "X" # permet de remplacer la case par un X 
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
            spots[ai_choice] = "O" #remplace la case choisit par l'ordinateur par un O 
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
