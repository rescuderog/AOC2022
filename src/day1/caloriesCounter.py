'''
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. 
Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
'''

#so, we need to read the input from a file, and sum the numbers given
#we could just do that, and keep a tally on who's got the biggest sum and given they're
#just asking for the amount of calories, we don't even have to individualize it.

#we initialize biggestSum at 0 so we can compare it with the other sums
biggestSum = 0
currentTally = 0

with open('../../inputs/input1.txt') as f:
    lines = f.readlines()
    for line in lines:
        #as per https://bobbyhadz.com/blog/python-check-if-line-is-empty, we can use the strip method to remove the trailing
        #and leading whitespaces and thus check if the line is empty.
        if line.strip():
            #we are casting to int directly because we know for sure it's an int. We could do some error checking here.
            currentTally = currentTally + int(line)
        else:
            #we reset the tally to 0 and compare to the biggestSum
            if currentTally > biggestSum:
                biggestSum = currentTally
            currentTally = 0

print("The elves with the most calories carried has:", biggestSum)

'''
Second challenge of day 1:

(...) the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. 
That way, even if one of those Elves runs out of snacks, they still have two backups.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

'''

#this is very similar, we'll just need to do a little more manipulation of the data in order to know the top 3

biggestSum = [0, 0, 0]
currentTally = 0

with open('../../inputs/input1.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line.strip():
            currentTally = currentTally + int(line)
        else:
            #I know, this doesn't scales well, either programatically or in Big O, this is just a quick and dirty solution.
            if currentTally > biggestSum[0]:
                biggestSum[1] = biggestSum[0]
                biggestSum[0] = currentTally
            elif currentTally > biggestSum[1]:
                biggestSum[2] = biggestSum[1]
                biggestSum[1] = currentTally
            elif currentTally > biggestSum[2]:
                biggestSum[2] = currentTally
            currentTally = 0

sumOfThree = biggestSum[0] + biggestSum[1] + biggestSum[2]
print("The three elves with the most calories carried have:", sumOfThree)            
