def display_menu():
    while True:
        print("\nHello! I'm Ma. Bea Mae Ynion")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comments")
        print("4. Exit")
        
        choice = int(input("Enter your choice:"))

        match choice:
            case 1:
                print("\nDate of Birth : July 29, 2004")
                print("\nAge : 20")
                print("\nEmail : mabeamaeynion@gmail.com")
                print("\nReligion : Roman Catholic")
            case 2:
                print("\nGoals: Improve study habits and time management.")
            case 3:
                print("\nComments")
                #TODO DELIMA
                #TODO RELENTE
                #TODO QUIAMBAO
                #TODO CITRON
            case 4:
                print("\nExiting the menu.")
                return