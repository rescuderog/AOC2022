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

#using dictionary comprehension we can create a dict of letters exactly as required to get the "priorities"
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

''' Day 3, part 2:

As you finish identifying the misplaced items, the Elves come to you with another issue.
For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. 
For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. 
That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. 
All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.
Additionally, nobody wrote down which item type corresponds to each group's badges. 
The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type.
Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
'''

#well, we now have to check for duplicates in every three lines.

with open('../../inputs/input3.txt') as f:
    lines = f.readlines()
    #this will be the final response tally
    result = 0
    #we'll use  this to check if we went through three lines
    iterator = 0
    #let's create a list of three lists to contain the characters
    alreadyDuplicate = [[], [], []]
    for line in lines:
        line = line.strip()
        for letter in line:
            if letter not in alreadyDuplicate:
                alreadyDuplicate[iterator].append(letter)
        if iterator != 2:
            iterator = iterator + 1
        else:
            for char in alreadyDuplicate[0]:
                if char in alreadyDuplicate[1] and char in alreadyDuplicate[2]:
                    result = result + dictLetters[char]
                    break
            iterator = 0
            alreadyDuplicate = [[], [], []]

print("The result of the second part is:", result)