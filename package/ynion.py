class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def sit(self):
        print(f"{self.name} is sitting.")

    def fetch(self):
        print(f"{self.name} is fetching a ball.")

    def play_dead(self):
        print(f"{self.name} is playing dead. Such a good dog!")

    def menu():
        while True:
            print("=== Dog Menu ===")
            print("[1] Bark")
            print("[2] Sit")
            print("[3] Fetch")
            print("[4] Play Dead")
            print("[5] Back")
            choice = input("Choose an action: ")

            match choice:
                case 1:
                    self.bark()
                case 2:
                    self.sit()
                case 3:
                    self.fetch()
                case 4:
                    self.play_dead()
                case 5:
                    return
                case _:
                    print("Invalid choice. Please choose a valid option.")