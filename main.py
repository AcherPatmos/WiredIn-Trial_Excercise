import random #imported the random module
class MainMenu:

    def greeting(self):   #method to greet the user
        name = input("Enter your name: ")
        while True: #while loop for use name validation
            if not name.strip():
                print("Name cannot be empty")
                name = input("Enter your name: ")
                continue
            if name.isdigit():
                print("Name should not be a number")
                name = input("Enter your name: ")
                continue
            break
        print(f"Welcome to the Rock, Paper, Scissors game {name}")

class GameLogic:  #class to handle main game logic

    def choosehand(self):  #method to prompt user to start playing the game
        print("Choose your hand")
        print("0. rock")
        print("1. paper")
        print("2. scissors")
        your_hand = int(input("Enter your choice: "))
        computer_hand = random.randint(0, 2)
        if your_hand== 0 and computer_hand==0 :
            print("It is a draw")
        elif your_hand==0 and computer_hand==1:
            print("You lose")
        elif your_hand==0 and computer_hand==2:
            print("You win")
        elif your_hand==1 and computer_hand==0:
            print("You win")
        elif your_hand==1 and computer_hand==1:
            print("It is a draw")
        elif your_hand==1 and computer_hand==2:
            print("You lose")
        elif your_hand==2 and computer_hand==0:
            print("You lose")
        elif your_hand==2 and computer_hand==1:
            print("You win")
        elif your_hand==2 and computer_hand==2:
            print("It is a draw")
        else:
            print("pick a valid option")

menu = MainMenu()
menu.greeting()
game = GameLogic()
game.choosehand()