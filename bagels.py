import random
import string

MAX_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f"""
I'm thinking of a {MAX_DIGITS} digit number. Try to guess it.
Here are some clues:
When I say:     It means:
    Pico        One digit is correct, but in the wrong position
    Fermi       One digit is correct, and in the right position
    Bagels      No digit is correct
        """)

    secretNum = getNum()
    print(f"I have though up a number. You have {MAX_GUESSES} guesses to get it.")

    guess = 1
    while guess <= MAX_GUESSES:
        print(f"Guess #{guess}")
        userGuess = input("> ")
        while not userGuess.isdecimal() or len(userGuess) != MAX_DIGITS:
            print(f"Guess #{guess}")
            userGuess = input("> ")

        print(getClues(secretNum, userGuess))

        if userGuess == secretNum:
            break


def getNum():
    numbers = list(string.digits)
    random.shuffle(numbers)
    secretNum = "".join(numbers[:MAX_DIGITS])

    return secretNum


def getClues(secretNum, userGuess):
    clues = []

    for i in range(MAX_DIGITS):
        if userGuess == secretNum:
            return "You got it!"

        if userGuess[i] == secretNum[i]:
            clues.append("Fermi")
        elif userGuess[i] in secretNum:
            clues.append("Pico")

        if not clues:
            return "Bagels"

        clues.sort()

        return clues


if __name__ == "__main__":
    main()
