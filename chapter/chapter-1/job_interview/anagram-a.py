# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# For example, the word 'anagram' can be rearranged into 'nag a ram'.
# Write a function that generates an anagram of a given string.
# The function should take a string as an argument and return a string with the characters shuffled.
# For example, given the string 'anagram', the function could return 'nag a ram'.
# You can assume that the input string will contain only letters and spaces.
# The anagram does not have to be a valid English word.
# 
# We have discussed this example in our second session on #critcode on October 1th.
#
import random

# example of an anagram function with detailed code explanation
def anagramA(text): # O(n)
    a = list(text) # Convert the string to a list of characters
    for i in range(len(a)): # Iterate through the list
        letter = a[i] # Store the current character
        j = random.randint(0, len(a) - 1) # Select a random index
        a[i] = a[j] # Swap the current character with the random one
        a[j] = letter # Assign the current character to the random index
    return ''.join(a) # Return the shuffled string

# @TODO: rethink (and feel free to rework!) the functions and reflect upon the code and the discussion we had in our course