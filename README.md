# Number Guessing Game

## Description

The Number Guessing Game is a Python script where players try to guess a randomly generated number between 1 and 100. Players have a maximum of 15 attempts to guess the number correctly. The game provides feedback on each guess and allows players to play multiple rounds.

## Features

- **Random Number Generation:** The game generates a random number between 1 and 100.
- **Attempt Limitation:** Players have up to 15 attempts to guess the correct number.
- **Input Validation:** Handles invalid inputs and prompts the player to enter a valid number.
- **Feedback System:** Informs players if their guess is too low or too high.
- **Replay Option:** Players can choose to play again or exit after each game.

## Installation

1. **Prerequisites:**
   - Ensure Python 3.x is installed on your computer.

2. **Download the Script:**
   - Copy the Python code into a file named `number_guessing_game.py`.

## Usage

1. **Run the Game:**
   - Open your terminal or command prompt.
   - Navigate to the directory where `number_guessing_game.py` is saved.
   - Run the script with the following command:
     ```bash
     python number_guessing_game.py
     ```

2. **Gameplay Instructions:**
   - Follow the on-screen prompts to make guesses.
   - The game will notify you if your guess is too low or too high.
   - After using up all attempts or guessing the number correctly, you will have the option to play again or exit.

## Code

Here is the code for the game:

```python
import random

def number_guessing_game():
    max_attempts = 15

    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0

        print("\nWelcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess the number.")

        while attempts < max_attempts:
            try:
                guess = int(input("Make a guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low.")
                elif guess > number_to_guess:
                    print("Too high.")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if guess != number_to_guess:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

number_guessing_game()
