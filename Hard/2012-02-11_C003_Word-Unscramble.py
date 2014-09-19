__author__ = 'Stoux'
''' http://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/ '''

# Words to be unscrambled
scrambled = ["mkeart", "sleewa", "edcudls", "iragoge", "usrlsle", "nalraoci", "nsdeuto", "amrhat", "inknsy", "iferkna"]
# Sort the array on length of string
scrambled.sort(key = lambda s: len(s))

alphaScrambled = {}
# => Reorder to Alphabetical
for reorderWord in scrambled:
    alpha = ''.join(sorted(reorderWord))
    alphaScrambled[alpha] = reorderWord

# Final wordlist
solvedTuple = {}

# Load the data from the Wordlist
f = open('../External/2012-02-11_C003_Word-Unscramble_Wordlist.txt')
for line in f:
    # Read the word, reorder to alphabetical
    unscrambled = line.replace("\n", "")
    alpha = ''.join(sorted(unscrambled))

    # Check if it is a scrambled word
    if alpha in alphaScrambled:
        solvedTuple[alphaScrambled[alpha]] = unscrambled

# Output result
for scrambledWord in scrambled:
    print('{0: <8} => {1: <8}'.format(scrambledWord, solvedTuple[scrambledWord]))