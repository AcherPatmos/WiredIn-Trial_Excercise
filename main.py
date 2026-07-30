class mainMenu:

    def greeting(self):
        name = input("Enter your name: ")
        while True:
            if not name.strip():
                print("Name cannot be empty")
                name = input("Enter your name: ")
                continue
            if name.isdigit():
                print("Name should not be a number")
                name = input("Enter your name: ")
                continue
            break

menu = mainMenu()
menu.greeting()