from package import ynion
from colorama import init , Fore, Style
import os

EXIT_OPTION = 0
UNSET_OPTION = -1

def menu():
    os.system("cls")
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = main_menu()
        process_choice(choice)
        os.system("cls")
        
    print(Fore.RESET)
        

def main_menu():
    while True:
        print(Fore.LIGHTBLUE_EX + "\n===== Main Menu =====")
        print("[1] Justine Delima")
        print("[2] Ma. Bea Mae Ynion")
        print("[3] Patricia Joy Relente")
        print("[4] Ma. Patricia Anne Quiambao")
        print("[5] Kathleen Citron")
        print("[6] Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 6:
                return choice
        except ValueError:
            print(Fore.RED + "Invalid choice. Please enter a valid number.")
    
def process_choice(choice):  
        os.system("cls")
        match choice:
            case 1:
                pass
            case 2:
                ynion.ynion_mabeamae()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Bye!")
                exit()
            case _:
                print("Invalid choice. Please try again.")

menu()        