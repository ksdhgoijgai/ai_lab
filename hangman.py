import random

def print_hangman(attempts):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        """,
        """
           -----
           |   |
           |
           |
           |
           |
        """,
        """
           -----
           |
           |
           |
           |
           |
        """
    ]
    print(stages[attempts])

def hangman():
    words = ["python", "java", "kotlin", "javascript"]
    word = "gitam"
    guessed_letters = set()
    attempts = 6
    displayed_word = ["_"] * len(word)

    print("Welcome to Hangman!")

    while attempts > 0:
        print_hangman(attempts)  # Print the hangman figure
        print("\n" + " ".join(displayed_word))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    displayed_word[index] = guess
            if "_" not in displayed_word:
                print(f"You won! The word was '{word}'.")
                break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

    if attempts == 0:
        print_hangman(attempts)
        print(f"You lost! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
