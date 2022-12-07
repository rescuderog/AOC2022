'''
Day 3:

One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. 
Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.
Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. 
The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. 
Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment

To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

'''
#this built-in library will help us trivialize a lot of the work required otherwise building the ascii dict
import string

#using dictionary comprehension we can create a dict of letters exactly as required
#we're lucky here that the letters that were asked were the ASCII characters, so
#as said before, this built-in library has a list of ascii characters ready to consume
dictLetters = {letter: i+1 for i, letter in enumerate(string.ascii_letters)}

#the dividing in half part is also fairly trivial with python.
#we just have to slice the string to half its length in each direction
def divideInHalf(theString):
    lowerHalf = theString[:len(theString)//2]
    upperHalf = theString[len(theString)//2:]
    return lowerHalf, upperHalf

#now it's just a matter of looping and comparing between halves

with open('../../inputs/input3.txt') as f:
    lines = f.readlines()
    #this will be the final response tally
    result = 0
    for line in lines:
        line = line.strip()
        line1, line2 = divideInHalf(line)
        alreadyDuplicate = []
        #we iterate over each character and compare it to the other half.
        #we also take in account each duplicate char, so we don't calculate repeats
        for letter in line1:
            if letter in line2 and letter not in alreadyDuplicate:
                alreadyDuplicate.append(letter)
                result = result + dictLetters[letter]

print("The final result is:", result)