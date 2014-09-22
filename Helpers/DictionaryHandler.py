__author__ = 'Stoux'
''' Script that handles handling of the Dictionary file (External/2014-09-22_Dictionary.txt) '''

from random import randint

class DictionaryHandler:

    # The words
    words = {}

    def __init__(self):
        # Check if it has already been initialized or not
        if (len(self.words) > 0):
            return

        # Not initialized yet; initialize it
        # => Open the dictionary file
        f = open("../External/2014-09-22_Dictionary.txt")

        # => Parse the lines
        for lineUntrimmed in f:
            line = lineUntrimmed.replace("\n", "")

            # Get the length of the word
            size = len(line)

            # Create the array if it doesn't exist yet
            if (size not in self.words.keys()):
                self.words[size] = []


            # Get the array that belongs to that
            array = self.words[size]

            # Add the word
            array.append(line)

    # Get a list of all the different sizes
    def get_word_lengths(self):
        return list(self.words.keys())

    # Get a number of words from the list, with a specified size
    def get_words(self, lengthOfWord, nrOfWords, uppercase=False):
        # Get the array of that length
        array = self.words[lengthOfWord]
        arraySize = len(array)

        chosenWords = {}

        # Get a random words from the array
        x = 0
        while (x < nrOfWords):
            # Get a random number
            randomNr = randint(0, arraySize)

            # Check if the word is already chosen
            if (randomNr in chosenWords.keys()):
                continue;

            # Add the word
            chosenWord = array[randomNr]
            if uppercase:
                chosenWord = chosenWord.upper()
            chosenWords[randomNr] = chosenWord
            x += 1

        # Return the result
        return list(chosenWords.values())