import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    while True:
        print("Welcome to Fermi Pico Bagels game!")
        print(f"Try to guess a {NUM_DIGITS}-digit number!")
        print(f"You have {MAX_GUESSES} guesses to get it!")

        secretNum = getSecretNum()
        print("I have thought a number, try to guess it")
        print(secretNum)

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")

            print(getClues(guess, secretNum))
            numGuesses += 1
        
            if guess == secretNum:
                break

            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print(f"The asnwer was {secretNum}")
        
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith('y'):
            break


    print("Thanks for playing")



def getSecretNum():
    """returns secret num of NUM_DIGITS digits"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum = ''.join(numbers[:NUM_DIGITS])

    return secretNum



def getClues(guess, secretNum):
    """return you got it, fermi, pico, bagels"""
    if guess == secretNum:
        return "You got it!"

    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if not clues:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


if __name__ == "__main__":
    main()
