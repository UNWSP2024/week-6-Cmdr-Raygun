# Author: Andrew Bittner
# Date: 10/10/2024

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def exitSequence():
    input('\nPress any key to exit... ')

def randDice(dice_sides, dice_num):
    # Write your logic to generate 2 numbers between 1 and 6 here
    dice_out = 0
    for rolls_count in range(dice_num):
        dice_out += random.randint(1, dice_sides)
    return dice_out

def getDiceAvg(rolls, dice_sides, dice_num):
    dice_avg = 0
    for rolls_count in range(rolls):
        dice_avg += randDice(dice_sides, dice_num)
    dice_avg /= rolls
    return dice_avg

def main():
    rolls = 100
    dice_sides = 6
    dice_num = 2
    dice_avg = getDiceAvg(rolls, dice_sides, dice_num)
    print(f'The average result of {rolls} roll(s) of {dice_num} {dice_sides}-sided die/dice is {dice_avg}', end = '. \n')
    exitSequence()
main()
    # Sum 2 numbers

    # return sum to calling function

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.