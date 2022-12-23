
import numpy as np

def line_move(dict_entry, knot_before_dict_entrys):
    import numpy as np
    x_pos = dict_entry['x_pos']; y_pos = dict_entry['y_pos']
    x_pos_know_before = knot_before_dict_entrys['x_pos']; y_pos_know_before = knot_before_dict_entrys['y_pos']

    if x_pos - x_pos_know_before == 0:
        sign_y = np.sign(y_pos_know_before - y_pos)
        new_x_pos = x_pos
        new_y_pos = y_pos + sign_y*1
    elif y_pos - y_pos_know_before == 0:
        sign_x = np.sign(x_pos_know_before - x_pos)
        new_y_pos = y_pos
        new_x_pos = x_pos + sign_x*1

    return new_y_pos, new_x_pos


def diagonal_move(dict_entry, knot_before_dict_entrys):
    import numpy as np
    x_pos = dict_entry['x_pos']; y_pos = dict_entry['y_pos']
    x_pos_know_before = knot_before_dict_entrys['x_pos']; y_pos_know_before = knot_before_dict_entrys['y_pos']

    sign_x = np.sign(x_pos_know_before - x_pos); sign_y = np.sign(y_pos_know_before - y_pos)

    new_x_pos = x_pos + sign_x*1; new_y_pos = y_pos + sign_y*1

    return new_y_pos, new_x_pos

def _move_necessary(H_pos_y, H_pos_x, T_pos_y, T_pos_x, full_rope=False):
    if full_rope:
        if abs(H_pos_y-T_pos_y) + abs(H_pos_x-T_pos_x) > 2:
            move_type = 'dia'
        elif (abs(H_pos_y - T_pos_y)==2
            or (abs(H_pos_x - T_pos_x)==2)):
            move_type = 'line'
        else:
            move_type=''
        return (
            abs(H_pos_y-T_pos_y) + abs(H_pos_x-T_pos_x) == 3
            or (abs(H_pos_y - T_pos_y)==2)
            or (abs(H_pos_x - T_pos_x)==2)
            ), move_type
    return (
            abs(H_pos_y-T_pos_y) + abs(H_pos_x-T_pos_x) == 3
            or (abs(H_pos_y - T_pos_y)==2)
            or (abs(H_pos_x - T_pos_x)==2)
            )

def _new_H_pos(H_pos_y, H_pos_x):
    if dir == 'U':
        H_pos_y -= 1
    elif dir == 'D':
        H_pos_y += 1
    elif dir == 'R':
        H_pos_x += 1
    elif dir == 'L':
        H_pos_x -= 1

    return H_pos_y, H_pos_x
    

def _find_size_of_grid_needed(raw_data):
    
    min_val_x, max_val_x, min_val_y, max_val_y = 0, 0, 0, 0 
    pos_x, pos_y = 0, 0
    for row in raw_data:
        dir, steps = row.split(' ')
        steps = int(steps)

        if dir == 'R':
            pos_x += steps
        elif dir == 'L':
            pos_x -= steps
        elif dir == 'U':
            pos_y -= steps
        elif dir == 'D':
            pos_y += steps

        if pos_x < min_val_x:
            min_val_x = pos_x
        elif pos_x > max_val_x:
            max_val_x = pos_x
        elif pos_y < min_val_y:
            min_val_y = pos_y
        elif pos_y > max_val_y:
            max_val_y = pos_y

    size_x = max_val_x - min_val_x
    size_y = max_val_y - min_val_y
    return size_x, size_y


### Setup data in a numpy array
with open("data/advent_of_code_dec_09.txt", 'r') as f:
    raw_data = f.read().splitlines()

### Puzzle 1 ###

# Grid size needed
size_x, size_y =_find_size_of_grid_needed(raw_data)

# Initiate grid -  Large due to unknown staring pos
grid = np.zeros([size_y*4, size_x*4])
point_grid = np.copy(grid)

# Initiate H and T in middle
H_pos_x, H_pos_y = size_x*2, size_y*2
T_pos_x, T_pos_y, = H_pos_x, H_pos_y

# Add first placement for T in point grid
point_grid[T_pos_y, T_pos_x] = 1
for row in raw_data:
    dir, steps = row.split(' ')
    steps = int(steps)
    for i in range(steps):
        # New position for head
        H_pos_y, H_pos_x = _new_H_pos(H_pos_y, H_pos_x)

        # If Manhatten distance from tail is more than 1 in a direction
        # set tail pos as head pos from last iteration
        if (abs(H_pos_y-T_pos_y) + abs(H_pos_x-T_pos_x) == 3
                or (abs(H_pos_y - T_pos_y)==2)
                or (abs(H_pos_x - T_pos_x)==2)
            ):
            T_pos_y, T_pos_x = old_H_pos_y, old_H_pos_x
            # Updating point grid with new pos for tail
            point_grid[T_pos_y, T_pos_x] = 1
        # Save old H positions for future tail pos
        old_H_pos_y, old_H_pos_x = H_pos_y, H_pos_x
        
print(f"All the places the tail has visited a minimum of once in the grid: {np.count_nonzero(point_grid)}")


### Puzzle 2 ###

with open("data/advent_of_code_dec_09.txt", 'r') as f:
    raw_data = f.read().splitlines()

# Grid size needed
size_x, size_y =_find_size_of_grid_needed(raw_data)

# Initiate grid -  Large due to unknown staring pos
grid = np.zeros([size_y*4, size_x*4])
point_grid = np.copy(grid)

# Initiate H and T in middle
H_pos_x, H_pos_y = size_x*2, size_y*2

# 10 knots in a dict
knot_dict = {
    x: {'x_pos': H_pos_x,
        'y_pos': H_pos_y,
        'old_x_pos': H_pos_x,
        'old_y_pos': H_pos_y} 
        for x in range(10)
    }


# Add first placement for T in point grid
point_grid[knot_dict[9]['y_pos'], knot_dict[9]['x_pos']] = 1
for row in raw_data:
    dir, steps = row.split(' ')
    steps = int(steps)
    
    for i in range(steps):
        for j in range(10):
            knot_pos_x = knot_dict[j]['x_pos']; knot_pos_y = knot_dict[j]['y_pos']
            
            if j == 0:
                H_pos_y, H_pos_x = _new_H_pos(knot_pos_y, knot_pos_x)
                knot_dict[j]['x_pos'] = H_pos_x
                knot_dict[j]['y_pos'] = H_pos_y
                knot_dict[j]['old_x_pos'] = knot_pos_x
                knot_dict[j]['old_y_pos'] = knot_pos_y
            else:
                check, move_type = _move_necessary(
                    knot_dict[j-1]['y_pos'],
                    knot_dict[j-1]['x_pos'],
                    knot_pos_y,
                    knot_pos_x, full_rope=True)
                
                if check:
                    if move_type == 'line':
                        knot_dict[j]['old_x_pos'] = knot_pos_x
                        knot_dict[j]['old_y_pos'] = knot_pos_y
                        new_pos_y, new_pos_x = line_move(knot_dict[j], knot_dict[j-1])
                        knot_dict[j]['x_pos'] = new_pos_x
                        knot_dict[j]['y_pos'] = new_pos_y
                    elif move_type == 'dia':
                        knot_dict[j]['old_x_pos'] = knot_pos_x
                        knot_dict[j]['old_y_pos'] = knot_pos_y
                        new_pos_y, new_pos_x = diagonal_move(knot_dict[j], knot_dict[j-1])
                        knot_dict[j]['x_pos'] = new_pos_x
                        knot_dict[j]['y_pos'] = new_pos_y
                    
                    if j == 9:
                        # Updating point grid with new pos for tail
                        point_grid[knot_dict[j]['y_pos'], knot_dict[j]['x_pos']] = 1
            
    
print(f"All the places the tail has visited a minimum of once in the grid: {np.count_nonzero(point_grid)}")

