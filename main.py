from package.ynion import Dog

def main_menu():
    dog = Dog(name="Jana", breed="Aspin", age=3)
    while True:
        print("\n===== Main Menu =====")
        print("[1] Justine Delima")
        print("[2] Ma. Bea Mae Ynion")
        print("[3] Patricia Joy Relente")
        print("[4] Ma. Patricia Anne Quiambao")
        print("[5] Kathleen Citron")
        print("[6] Exit")
        
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                pass
            case 2:
                dog.menu()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case _:
                print("Invalid choice. Please try again.")

main_menu()        