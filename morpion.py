from helpers import draw_board , check_turn , check_for_win
import os
from menu import main_menu

def play_pvp():

    spots = {1 : "1" , 2 : "2", 3 : "3", 4 : "4", 5 : "5",
         6 : "6", 7 : "7", 8 : "8", 9 : "9"}

    playing = True
    complete = False
    turn = 0
    prev_turn = -1

    while playing:
    
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)
        if prev_turn == turn:
            print("Case déjà prise, rejouez.")
        prev_turn = turn
        print("Joueur " + str((turn %2) + 1) + " choisit une case (ou 'q' pour quitter): ")
        choice = input()
        if choice == 'q':
            playing = False
        elif str.isdigit(choice) and int(choice) in spots:
            if not spots [int(choice)] in ['X' , 'O']:
                turn += 1
                spots[int(choice)] = check_turn(turn)
            
        if check_for_win(spots): playing, complete = False, True
        if turn >9 : playing = False
    
    
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if complete:
        if check_turn(turn) =='X': 
           print("Félicitations! Joueur 1 a gagné ! " )
        else : print("Félicitations! Joueur 2 a gagné ! " )
  
  
    else : 
    
        print("Egalité !")
        
        

    print("\nRetour au Menu principal")
    input("Press ENTER to return...")
    
    
if __name__ == "__main__":
    main_menu(play_pvp)


