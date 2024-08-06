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
