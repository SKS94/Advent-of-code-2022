import pandas as pd
import numpy as np

with open("data/advent_of_code_dec_05.txt", 'r') as f:
    raw_data = f.readlines()

# Split index of data set into the two different asepcts
data_change_index = raw_data.index('\n')

# Setting up the container data
width_container_array = int((len(raw_data[0])+1)/4)    
indices_for_input = [index*4+1 for index in range(width_container_array)]

full_container_list = [[] for i in range(width_container_array)]
for counter, line in enumerate(raw_data):
    if counter >= data_change_index - 1:
        break

    # Container array of horizontal axes
    container_line = [line[index] for index in indices_for_input]
    
    for i, vertical_list in enumerate(full_container_list):
        if container_line[i] != ' ':
            full_container_list[i].append(container_line[i])

# Setting up the movement data into a dataframe
movement_list = []
for line in raw_data[data_change_index+1:]:
    # Split instead of calling indices, if amount is more than single digit
    move_string = line[:-1].split(' ')
    
    move_list = [move_string[1], move_string[3], move_string[5]]
    movement_list.append(move_list)
move_df = pd.DataFrame(movement_list, columns=['amount', 'from', 'to'])
move_df=move_df.astype(int)






# # ### First Puzzle ###
full_container_list_og = full_container_list.copy()
for index, row in move_df.iterrows():
    # Crates to move
    moving_crates_list = full_container_list[row['from']-1][:row['amount']]
    # Reverse list for later append
    moving_crates_list.reverse()

    # append into
    full_container_list[row['to']-1] = moving_crates_list + full_container_list[row['to']-1]
    # remove from old array
    full_container_list[row['from']-1] = full_container_list[row['from']-1][row['amount']:]

final_top_crate_str = ''
for final_vert_line in full_container_list:
    final_top_crate_str += final_vert_line[0]

print(f"Puzzle 1: Final configuration of all the top crates on each vertical row: {final_top_crate_str}")


### Second Puzzle ###

full_container_list = full_container_list_og
for index, row in move_df.iterrows():
    # Crates to move
    moving_crates_list = full_container_list[row['from']-1][:row['amount']]

    # append into
    full_container_list[row['to']-1] = moving_crates_list + full_container_list[row['to']-1]
    # remove from old array
    full_container_list[row['from']-1] = full_container_list[row['from']-1][row['amount']:]
    

final_top_crate_str = ''
for final_vert_line in full_container_list:
    final_top_crate_str += final_vert_line[0]

print(f"Puzzle 2: Final configuration of all the top crates on each vertical row: {final_top_crate_str}")