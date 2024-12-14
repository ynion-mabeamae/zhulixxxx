class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"\n{self.name} says Woof!")

    def sit(self):
        print(f"\n{self.name} is now sitting.")

    def fetch(self):
        print(f"\n{self.name} is fetching the ball!")

    def play_dead(self):
        print(f"\n{self.name} is playing dead. Such a good dog!")
        
    def menu(self):
        while True:
            print("\n==== DOG MENU ====")
            print("[1] Bark")
            print("[2] Sit")
            print("[3] Fetch")
            print("[4] Play Dead")
            print("[5] Back")
            
            choice = input("Enter your choice: ")
            
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
                    return
                case _:
                    print("Invalid choice. Please try again.")
                    
   