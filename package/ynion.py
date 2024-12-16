from colorama import init , Fore, Style
import os

def ynion_mabeamae():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX + "==== Create Your Dog ====")
    name = input("Enter the dog's name: ")
    breed = input("Enter the dog's breed: ")
    
    while True:
        try:
            age = int(input("Enter the dog's age: "))
            break
        except ValueError:
            print(Fore.RED + "\nInvalid age. Please enter a valid number.")
    
    class Dog:
        def __init__(self, name, breed, age):
            self.name = name
            self.breed = breed
            self.age = age

        def bark(self):
            os.system("cls")
            print(f"\n{self.name} says Woof!")
            input("\nPress Enter to return...")
            os.system("cls")

        def sit(self):
            os.system("cls")
            print(f"\n{self.name} is now sitting.")
            input("\nPress Enter to return...")
            os.system("cls")

        def fetch(self):
            os.system("cls")
            print(f"\n{self.name} is fetching the ball!")
            input("\nPress Enter to return...")
            os.system("cls")

        def play_dead(self):
            os.system("cls")
            print(f"\n{self.name} is playing dead. Such a good dog!")
            input("\nPress Enter to return...")
            os.system("cls")
            
        def roll_over(self):
            os.system("cls")
            print(f"\n{self.name} rolls over! What a good dog!")
            input("\nPress Enter to return...")
            os.system("cls")
            
        def menu(self):
            os.system("cls")
            while True:
                print(Fore.LIGHTBLUE_EX + 
                      "Interact with your dog using the options below:")
                print("\n==== MENU ====")
                print("[1] Bark")
                print("[2] Sit")
                print("[3] Fetch")
                print("[4] Play Dead")
                print("[5] Roll Over")
                print("[6] Back to Main Menu")
                
                choice = input("Enter your choice: ")
                
                os.system("cls")
                match choice:
                    case "1":
                        self.bark()
                    case "2":
                        self.sit()
                    case "3":
                        self.fetch()
                    case "4":
                        self.play_dead()
                    case "5":
                        self.roll_over()
                    case "6":
                        return
                    case _:
                        print(Fore.RED + "Invalid choice. Please try again.")
            input("\nPress Enter to return...")
            os.system("cls")

    dog = Dog(name=name, breed=breed, age=age)
    dog.menu()

ynion_mabeamae()
    

        
