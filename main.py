import random #imported the random module
class MainMenu:

    def greeting(self):   #method to greet the user
        name = input("Enter your name: ")
        while True: #while loop for user_name validation
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

    def get_player_hand(self): # method to get and return the player's choice/ does error handling as well
        try:
            player_hand = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid option\n")
            return None
        if player_hand < 0 or player_hand > 2:
            print("Invalid option\n")
            return None
        return player_hand

    def get_computer_hand(self): # method to compute and return the computer's hand
        computer_hand = random.randint(0, 2)
        return computer_hand

    def viewresult(self, player_hand, computer_hand): #stores and compares the player's and computer's hand for an outcome
        hands= {0:"rock", 1:"paper", 2:"scissors"}
        print(f"Your hand is : {hands[player_hand]} and computer's hand is: {hands[computer_hand]}")
        if player_hand == computer_hand:
            print(" It is a Draw")
            return "draw"
        elif player_hand == 0 and computer_hand == 1:
                print("You lose")
                return "lose"
        elif player_hand == 0 and computer_hand == 2:
                print("You win")
                return "win"
        elif player_hand == 1 and computer_hand == 0:
                print("You win")
                return "win"
        elif player_hand == 1 and computer_hand == 1:
                print("It is a draw")
                return "draw"
        elif player_hand == 1 and computer_hand == 2:
                print("You lose")
                return "lose"
        elif player_hand == 2 and computer_hand == 0:
                print("You lose")
                return "lose"
        elif player_hand == 2 and computer_hand == 1:
                print("You win")
                return "win"
        elif player_hand == 2 and computer_hand == 2:
                print("It is a draw")
                return "draw"

    def play_game(self): # loops the game whenever there is a draw or an invalid output
        while True:
            self.choosehand()
            player_hand = self.get_player_hand()
            if player_hand is None:
                continue  # invalid input, ask again
            computer_hand = self.get_computer_hand()
            result = self.viewresult(player_hand, computer_hand)
            if result == "draw":
                print("Let's try that again...\n")
                continue  # draw, replay automatically
            else:
                break


def main(): #main method to run the program
    menu = MainMenu()
    menu.greeting()

    game = GameLogic()

    while True:
        game.play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y" and again != "n":
            print("Invalid option")
            continue
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()