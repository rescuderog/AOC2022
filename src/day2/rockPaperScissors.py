'''
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

'''

#this one is a little tougher but it still can be systematized: first, we'll build two dictionaries
#and we'll assign the values that were mentioned in the description of the exercise
dictAgainst = {"A": 1, "B": 2, "C": 3}
dictMe = {'X': 1, 'Y': 2, 'Z': 3}
totalValue = 0

def solveRPS(a, b):
    valueA = dictAgainst[a]
    valueB = dictMe[b]
    outcome = 0
    #first outcome is the easiest: a draw, we just add 3 as per the rules and the value of the shape
    if valueB == valueA:
        outcome = 3 + valueB
    #the exception to the rule in both loss and win scenarios
    elif valueA == 3 and valueB == 1:
        outcome = 6 + valueB
    elif valueA == 1 and valueB == 3:
        outcome = 0 + valueB
    #this is the win scenario, except for the Rock-Scissors combo, which is an exception to the rule (1 wins against 3)
    #in all other cases, the higher value wins against the lower one
    elif valueB > valueA:
        outcome = 6 + valueB
    #loss scenario
    elif valueA > valueB:
        outcome = 0 + valueB
    return outcome


with open('../../inputs/input2.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        a, b = line.split(' ')
        result = solveRPS(a, b)
        totalValue += result

print("The resulting score of the simulation is:", totalValue)

''' Part 2: 

The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated.
Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

'''
#so, now we have to invert what we did, let's write a new function to account for that.
#first, though, we may be better off utilizing a dict of the winning outcomes to compare faster

dictWinningOutcomes = {"A": 2, "B": 3, "C": 1}

def solveRPS2(a, b):
    valueA = dictAgainst[a]
    valueB = dictMe[b]
    outcome = 0

    #loss condition. We saw last time that, excepting the Rock-Scissors combo, we can safely just
    #deduct 1 from the shape the opponent does and we're losing every time
    if valueB == 1:
        if valueA != 1:
            myShape = valueA - 1
        else:
            myShape = 3
        outcome = myShape + 0
    #win condition. Same here, we add 1 to the shape of the opponent and we're winning.
    elif valueB == 3:
        if valueA != 3:
            myShape = valueA + 1
        else:
            myShape = 1
        outcome = myShape + 6
    #draw condition. We just need to replicate the opponent's shape.
    elif valueB == 2:
        myShape = valueA
        outcome = 3 + myShape

    return outcome

totalValue = 0

with open('../../inputs/input2.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        a, b = line.split(' ')
        result = solveRPS2(a, b)
        totalValue += result

print("The resulting score of the 2nd simulation is:", totalValue)
