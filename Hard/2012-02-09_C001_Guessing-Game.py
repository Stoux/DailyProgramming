__author__ = 'Stoux'

from random import randint

tries = 1

# Ceil & Floor
ceil = 100
floor = 1

# Start with a wild guess
wildGuess = randint(0, 100) + 1
print("A wild guess! Is your number: " + str(wildGuess) + "?")

guessing = True
# Get input from the user
while (guessing):
    var = input("(Y)es, (H)igher, (L)ower: ")
    varU = var.upper()

    # Correct answer
    if (varU == "Y"):
        guessing = False
        continue

    # The number is higher
    elif (varU == "H"):
        floor = wildGuess

    # The number is lower
    elif (varU == "L"):
        ceil = wildGuess

    # Invalid input
    else:
        print("You can only answer Y, H or L!")
        continue

    # Next wild guess
    wildGuess = randint(floor + 1, ceil - 1) # Random implementation or Halving: wildGuess = int((floor + ceil) / 2)
    print("Is your number: " + str(wildGuess) + "?")

    # Increment tries
    tries += 1

print("Huzzah! Only took me " + str(tries) + " tries!")

# 24
