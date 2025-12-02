def menu():
    print("[1] choix 1")
    print("[2] choix 2")
    print("[0] Quitter")
    
    
menu()
option = int(input("Entrer un choix:  "))

while option != 0:
    if option == 1:
        #si option 1 choisis
        print("choix 1")
    elif option == 2:
        #si option 2 choisis
        print("choix 2")
    else : 
        print("option invalide ")
        
    menu()
    option = int(input("Entrer un choix:  "))

print("Merci ")

