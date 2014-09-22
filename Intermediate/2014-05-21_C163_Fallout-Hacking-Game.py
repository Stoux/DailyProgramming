__author__ = 'Stoux'
''' http://www.reddit.com/r/dailyprogrammer/comments/263dp1/5212014_challenge_163_intermediate_fallouts/ '''

from random import randint

# Import the helpers
import os, sys
lib_path = os.path.abspath('../Helpers')
sys.path.append(lib_path)
# => Import the DictionaryHandler
from DictionaryHandler import DictionaryHandler ''' Errors can be ignored '''

# Checking function | Check if a string is a number, and in a range
def is_number(s, range):
    try:
        i = int(s)
        return (i in range)
    except ValueError:
        return False

# Create a DictionaryHandler
dc = DictionaryHandler()
# => Get the word lengths
wordLengths = dc.get_word_lengths()
print(wordLengths)

# Instructions
print("\n\nWelcome to Fallout's Hacking Game!")
print("The goal of this game is to guess the word. You'll get a list of words and one of those is the word you are looking for.")

# Settings
nrOfWords = 5
wordLen = 5
changeSettings = True

while(True):
    # Start a new game
    print("\n[== Starting a new Game ==]")

    # Check if settings should be changed
    if (changeSettings):
        # Determine howmany words it should display
        wordsQuestion = "Howmany options should I display (4-20)? "
        while(True):
            nrOfWordsString = input(wordsQuestion)
            # Check if the input is valid
            res = is_number(nrOfWordsString, range(4, 21))
            if (res):
                # Get the number as int
                nrOfWords = int(nrOfWordsString)
                break

            # Input is not valid
            wordsQuestion = "That's not a valid number. Enter a number between 4 & 20: "

        # Determine the length
        lenQuestion = "How long should the words be (" + str(wordLengths[0]) + "-" + str(wordLengths[len(wordLengths) - 1]) + ")? "
        while(True):
            wordLenString = input(lenQuestion)
            # Check if valid
            if (is_number(wordLenString, range(wordLengths[0], wordLengths[len(wordLengths) - 1] + 1))):
                # Get as int
                wordLen = int(wordLenString)
                break;

            # Invalid answer
            lenQuestion = "That's not a valid number! Enter a number between " + str(wordLengths[0]) + " & " + str(wordLengths[len(wordLengths) - 1]) + ": "

    # Calculate available tries
    availTries = int(((nrOfWords + wordLen) / 2) / 4)
    # => Check if not out of bounds
    if (availTries < 1):
        availTries = 1
    if (availTries > 6):
        availTries = 6

    # Output settings
    print("\nSettings: " + str(wordLen) + " chars | " + str(nrOfWords) + " options | " + str(availTries) + " tries available! Options:")

    # Get a list of options
    options = dc.get_words(wordLen, nrOfWords, uppercase=True)
    # => Display options
    for word in options:
        print(word)
    # => Empty line
    print("")

    # Select an option
    selectedOption = options[randint(0, len(options) - 1)]
    selectedOptionChars = list(selectedOption)

    # Keep track
    guessArray = {}
    for x in range(0, wordLen):
        guessArray[x] = "_"
    correct = False

    # While tries are available
    while (availTries > 0):
        # Prompt for a guess
        print("Currently guessed: " + " ".join(guessArray.values()))
        guess = input("Guess (" + str(availTries) + " tries left): ")

        # Check length
        if (len(guess) != wordLen):
            print("Your input is not the same length as the word currently being guessed! (" + str(wordLen) + " chars long)")
            continue

        # Check if it matches
        if (guess.upper() == selectedOption):
            correct = True
            break

        # Get correct letters from the input
        guessChars = list(guess.upper())
        # => Loop through chars
        i = 0
        for char in guessChars:
            if (char == selectedOptionChars[i]):
                guessArray[i] = char
            i += 1

        # Decrement
        availTries -= 1

    # Check if they failed or not
    if correct:
        print("Well done! You've hacked the system!")
    else:
        print("You failed to hack the system. You are dead.")

    # What's next
    nextGame = input("What now? Another game (N), New game with other settings (S), Quit (Q).").upper()
    if (nextGame == "N"):
        changeSettings = False
    elif (nextGame == "S"):
        changeSettings = True
    else:
        print("OK BAI.")
        quit()

