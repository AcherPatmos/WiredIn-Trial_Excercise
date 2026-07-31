# Rock, Paper, Scissors Game Program

## Overview
A command-line Rock, Paper, Scissors game built as a trial exercise for Wiedin Academy. 
The project uses two classes to separate the menu/greeting flow from the core game logic.

## Features

Player name validation on entry (rejects empty input or numbers-only input)

Classic Rock / Paper / Scissors gameplay against a random computer opponent

Invalid input handling (non-numeric or out-of-range choices are rejected and re-prompted)

Draws are automatically replayed until there's a clear winner

"Play again?" prompt after each completed round

## Project Structure

Python Trial Excerise_Wiedin Academy

├── Project Screenshots   # screenshots documenting the project/testing

└── main.py                # entry point — contains all game logic

## Classes

### class MainMenu: Handles the welcome flow.

- Method greeting(): prompts for and validates the player's name, then displays a welcome message.

### class GameLogic: Handles the actual game.

- Method choosehand(): displays the hand options (rock/paper/scissors)

- Method get_player_hand(): reads and validates the player's numeric choice

- Method get_computer_hand(): generates the computer's random choice

- Method viewresult(player_hand, computer_hand): compares hands and prints/returns the outcome ("win", "lose", or "draw")

- Method play_game(): runs one full round, automatically replaying on invalid input or a draw

## How to Play

1. Clone or download this repository.
2. Navigate to the project directory in your terminal.
3. Run main.py
4. Enter your name when prompted
5. Choose your hand:
  0 — Rock
  1 — Paper
  2 — Scissors
6. See the result (win, lose, or draw; draws replay automatically)
7. Choose whether to play again (y/n; anything else is rejected and re-prompted)
   
## Requirements

Python 3.x

No external dependencies (uses only the built-in random module)

## Notes / Possible Next Steps
Add score tracking across rounds (wins/losses/draws tally)

Add input for "best of N" rounds instead of playing indefinitely

# Author
Patmos Acher Mpakaniye
