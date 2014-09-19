__author__ = 'Stoux'

def look_n_say(n):
    # Decrement n for array compensation
    n -= 1

    # Start with array of one 1
    lookSayArray = [1]

    loop = 0
    # Start looping until you hit the Nth output
    while(loop < n):
        # Create the new array
        newResult = []

        # Keep track
        currentlyFound = -1
        totalFound = 0

        # Loop through the array
        for i in lookSayArray:
            # Check which one is found
            if (currentlyFound != -1 and currentlyFound != i):
                # Add to array
                newResult.append(totalFound)
                newResult.append(currentlyFound)

                # Reset for new value
                totalFound = 0

            currentlyFound = i
            totalFound += 1

        # Add last one
        newResult.append(totalFound)
        newResult.append(currentlyFound)

        # Set the array
        lookSayArray = newResult

        # Increment loop
        loop += 1

    # Return the array
    return lookSayArray

print("Enter a number for the Look'n'Say or type QUIT.")
while(True):
    # Get the input
    var = input("Input: ")

    # Check if Quitting
    if (var.upper() == "QUIT"):
        print("BAI")
        quit()

    # Check if a number
    try:
        value = int(var)
        print("Look'n'Say for " + var + " is: " + ''.join(str(i) for i in look_n_say(value)))
    except ValueError:
        print("'" + var + "' is not a number.")

