
import pandas as pd

### First puzzle ###
data = pd.read_csv("data/advent_of_code_dec_04.txt", sep=",|-", 
    names=['elf1_from', 'elf1_to', 'elf2_from', 'elf2_to'], engine='python')

# Insert boolean column with True/False of overlap between assignments
data.insert(4, 'full overlap of duties', 
    (
        (data['elf1_from'] <= data['elf2_from']) 
        & 
        (data['elf1_to'] >= data['elf2_to']))
    | 
        ((data['elf1_from'] >= data['elf2_from']) 
        & 
        (data['elf1_to'] <= data['elf2_to']))
    )

number_of_containing_pairs = data["full overlap of duties"].sum()

print(f"The number of pairs that fully contain the otherpoints: {number_of_containing_pairs}")

### Second puzzle ###

# Same assignment with a small tweak in insert boolean logic statement
data.insert(5, 'some overlap of duties', 
    (

        (data['elf1_from'] <= data['elf2_from']) 
        &
        (data['elf1_to'] >= data['elf2_from']))
    |
        ((data['elf1_from'] >= data['elf2_from']) 
        & 
        (data['elf1_from'] <= data['elf2_to']))
    )

number_of_some_overlap = data["some overlap of duties"].sum()

print(f"The number of pairs that fully have some overlap: {number_of_some_overlap}")