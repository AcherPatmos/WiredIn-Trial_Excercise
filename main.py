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

class GameLogic:  # class to handle main game logic

    def choosehand(self):  # method to prompt user to start playing the game
        print("Choose your hand")
        print("0. rock")
        print("1. paper")
        print("2. scissors")

    def get_player_hand(self):
        try:
            player_hand = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid option")
        return player_hand

    def get_computer_hand(self):
        computer_hand = random.randint(0, 2)
        return computer_hand

    def viewresult(self, player_hand, computer_hand):
        Hands= {0:"rock", 1:"paper", 2:"scissors"}
        print(f"Your hand is : {Hands[player_hand]} and computer's hand is: {Hands[computer_hand]}")
        if player_hand == computer_hand:
            print(" It is a Draw")






                # if your_hand == 0 and computer_hand == 0:
                #     print("It is a draw")
                # elif your_hand == 0 and computer_hand == 1:
                #     print("You lose")
                # elif your_hand == 0 and computer_hand == 2:
                #     print("You win")
                # elif your_hand == 1 and computer_hand == 0:
                #     print("You win")
                # elif your_hand == 1 and computer_hand == 1:
                #     print("It is a draw")
                # elif your_hand == 1 and computer_hand == 2:
                #     print("You lose")
                # elif your_hand == 2 and computer_hand == 0:
                #     print("You lose")
                # elif your_hand == 2 and computer_hand == 1:
                #     print("You win")
                # elif your_hand == 2 and computer_hand == 2:
                #     print("It is a draw")
                # else:
                #     print("pick a valid option")
        return None


while True:
    game = GameLogic()
    game.choosehand()