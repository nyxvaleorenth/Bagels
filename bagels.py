import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f"""
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position
    Fermi       One digit is correct and in the right position
    Bagels      No digit is correct

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""")

    while True:     # main game loop
        # stores the secret number
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} to get it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # keep looping untip they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print(f"The answer was {secretNum}")

        # ask the player to play again
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)

    # get the first NUM_DIGITS in the list
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi bagels clues for a guess 
    and secret number pair"""
    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # a correct digit is in the incorrect place
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'   # there are no correct digits at all
    else:
        # sort the clues into alphabetical order so their original order
        # doesn't give information away
        clues.sort()
        # make a single string from the list of string clues
        return ' '.join(clues)


if __name__ == "__main__":
    main()
