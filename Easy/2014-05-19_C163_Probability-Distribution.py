__author__ = 'Stoux'
from random import randint

# Number of rolls that will be thrown
nrOfRolls = [1,2,3,4,5,6,7,8,9,10, 100, 1000, 10000, 100000, 1000000]

# Dict with results. [nrOfRolls => Dict[Dice side => Throws]]
results = {}

# Loop through rolls
for rolls in nrOfRolls:
    # Create a dictionary for this
    rollResults = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    # Number of rolls done
    rollTimes = 0
    while (rollTimes < rolls):
        # 'Roll a the dice'
        roll = randint(1, 6)

        # Get current result
        currentRolls = rollResults[roll]
        # Increment that by one
        rollResults[roll] = currentRolls + 1

        # Increment rollTimes
        rollTimes += 1

    # Add the results to the main results dict
    results[rolls] = rollResults

# Print the results
# => Header
print("# of Rolls | 1s      | 2s      | 3s      | 4s      | 5s      | 6s      ")
print("===========|=========|=========|=========|=========|=========|=========")

# => Function to calculate row %
def calc(totalRolls, resultRolls):
    # Calculate percentage
    onePer = totalRolls / 100
    resultPer = resultRolls / onePer

    # Return formatted string
    return str("{0:.2f}%".format(resultPer)).ljust(7, " ")

# => Rows
for rolls in nrOfRolls:
    # Get the results
    resultArray = results[rolls]

    # Formatted array
    formatted = []

    # Loop through results
    for side in range(1, 7):
        formatted.append(calc(rolls, resultArray[side]))

    # Print as one string
    print(str(rolls).ljust(10, " ") + " | " + " | ".join(formatted))