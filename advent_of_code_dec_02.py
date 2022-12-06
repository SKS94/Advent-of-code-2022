import numpy as np

### First puzzle ###
data = np.loadtxt("data/advent_of_code_dec_02.txt", dtype=str)

# Number representation of the possible moves
number_rep = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}

# Number rep of key that beats element
cyclic_win_dict = {1:3, 3:2, 2:1}

# Points for outcome and initilizaition of my accumalated points
win_points = 6; draw_points = 3; points_for_me = 0

for game in data:
    my_move = number_rep[game[-1]]
    elf_move = number_rep[game[0]]

    # points gained for move same as number rep of my move
    move_points = my_move
    outcome_points = 0

    # If statement check for win based on cyclic win pattern 1-->3-->2-->1
    if cyclic_win_dict[my_move] == elf_move:
        outcome_points = win_points
    elif my_move == elf_move:
        outcome_points = draw_points
    points_for_me += outcome_points + move_points

print(f"The number of points I accumalate in the game: {points_for_me}")


### Second puzzle ###

# Number rep of key that wins and looses to element
cyclic_win_dict = {3:1, 2:3, 1:2}
cyclic_loose_dict = {1:3, 3:2, 2:1}

# Points gained for each needed outcome
needed_outcome_points = {'X': 0, 'Y': 3, 'Z': 6}

points_for_me = 0
for game in data:
    elf_move = number_rep[game[0]]
    needed_outcome = game[-1]

    # Move points
    move_points = elf_move
    if needed_outcome == 'X':
        move_points = cyclic_loose_dict[elf_move]
    elif needed_outcome == 'Z':
        move_points = cyclic_win_dict[elf_move]

    # Outcome points
    outcome_points = needed_outcome_points[game[-1]]

    # Accumalated points
    points_for_me += outcome_points + move_points

print(f"The number of points I accumalate in the game: {points_for_me}")