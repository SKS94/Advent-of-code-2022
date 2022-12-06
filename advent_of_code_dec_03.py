def shift_ASCII_val(letter_list):
    """
    Shift original ASCII values. a for referene is 97 going to 1
    and A is 65 going to 27
    """
    shift_lower_case = 96; shift_upper_case = 65 - 27; score = 0
    for letter in letter_list:
        # Decide shift based on upper/lower case
        if letter.islower():
            shift = shift_lower_case
        elif letter.isupper():
            shift = shift_upper_case

        # Accumalate score for list
        score += ord(letter) - shift
    return score

import numpy as np

### First puzzle ###
data = np.loadtxt("advent_of_code_dec_03.txt", dtype=str)

acummalative_score = 0
for rucksacks in data:
    num_of_items_in_compartment = int(len(rucksacks)/2)
    compartment_1 = rucksacks[:num_of_items_in_compartment]
    compartment_2 = rucksacks[num_of_items_in_compartment:]

    # List with items that appear in both compartments
    doublet_list = [letter for letter in compartment_1 if letter in compartment_2]
    # Remove duplicates
    doublet_list = list(set(doublet_list))
    # score
    acummalative_score += shift_ASCII_val(doublet_list)

print(f"Sum of the priorities of those item types: {acummalative_score}")

### Second puzzle ###
acummalative_score = 0
for i in range(int(len(data)/3)):
    rucksacks = [data[i*3], data[i*3+1], data[i*3+2]]

    # List with items that appear in two of the rucksacks
    doublet_list = [letter for letter in rucksacks[0] if letter in rucksacks[1]]
    # Remove duplicates
    doublet_list = list(set(doublet_list))

    # Check which letter is in the last rucksack
    item_in_all_three = [letter for letter in doublet_list if letter in rucksacks[2]]

    # Score of item name
    acummalative_score += shift_ASCII_val(item_in_all_three)

print(f"Sum of the priorities of those item types for name tag problem: {acummalative_score}")