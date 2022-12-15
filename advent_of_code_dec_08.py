
import numpy as np

### Setup data in a numpy array
with open("data/advent_of_code_dec_08.txt", 'r') as f:
    raw_data = f.read().splitlines() 

raw_data_width = len(raw_data[0]); raw_data_length = len(raw_data)

tree_matrix_og = np.zeros([raw_data_length, raw_data_width], dtype=int)
for count, row in enumerate(raw_data):
    row_split = list(row)
    tree_matrix_og[count, :] = row_split


### Puzzle 1 ###
# Looping thorugh matrix with count for invisble trees
tree_matrix = np.copy(tree_matrix_og)
not_visible_counter = 0
for x_dir in range(1, raw_data_width-1):
    for y_dir in range(1, raw_data_length-1):
        # tree val
        entry_value = tree_matrix[x_dir, y_dir]
        # temp matrix with index tree subtracked in size
        temp_tree = tree_matrix - entry_value
        if (
            True in (temp_tree[x_dir, :y_dir] >= 0)
            and True in (temp_tree[x_dir, y_dir+1:] >= 0)
            and True in (temp_tree[:x_dir, y_dir] >= 0)
            and True in (temp_tree[x_dir+1:, y_dir] >= 0)
        ):
            not_visible_counter += 1
print(f"Number of visible trees in total: {raw_data_width*raw_data_length - not_visible_counter}")


### Puzzle 2 ###
# Scenic score

# Function for puzzle
tree_matrix = np.copy(tree_matrix_og)
def score_direction(input_list, origin_tree, reverse=False):
    """
    Function to compute the count of trees in a direction
    before one is equal size o larger to orginal tree
    """
    # list reverse for loop if necessary
    if reverse:
        input_list = np.flip(input_list)
    
    # Loop through trees in lines
    for count, entry in enumerate(input_list):
        if origin_tree <= entry:
            break
    return count+1


# Solutions to puzzle
best_scenic_score = 0
for x_dir in range(1, raw_data_width-1):
    for y_dir in range(1, raw_data_length-1):
        # tree val
        entry_value = tree_matrix[x_dir, y_dir]
        # temp matrix with index tree subtracked in size
        x1_scenic = score_direction(tree_matrix[:x_dir, y_dir], origin_tree=entry_value, reverse=True)
        x2_scenic = score_direction(tree_matrix[x_dir+1:, y_dir], origin_tree=entry_value)
        y1_scenic = score_direction(tree_matrix[x_dir, :y_dir], origin_tree=entry_value,reverse=True)
        y2_scenic = score_direction(tree_matrix[x_dir, y_dir+1:], origin_tree=entry_value)
        
        # Score for entry
        scenic_score = x1_scenic * x2_scenic * y1_scenic * y2_scenic
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

print(f"Best scenic score: {best_scenic_score}")
