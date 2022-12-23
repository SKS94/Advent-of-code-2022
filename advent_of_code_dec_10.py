
### Setup data in a numpy array
with open("data/advent_of_code_dec_10.txt", 'r') as f:
    raw_data = f.read().splitlines()


### Puzzle 1 ###
x_val = 1; cycle_counter = 1; twenty_cycle_strength = []
for count, row in enumerate(raw_data):
    if (cycle_counter+20)//40 == (cycle_counter+20)/40:
        print(x_val)
        twenty_cycle_strength.append(x_val*cycle_counter)

    if row == 'noop':
        cycle_counter += 1
        continue
    else:
        addx, val = row.split(' ')
        val = int(val)
        cycle_counter += 1
        if (cycle_counter+20)//40 == (cycle_counter+20)/40:
            twenty_cycle_strength.append(x_val*cycle_counter)
        cycle_counter += 1
        x_val += val

print(f"Sum of the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles: {sum(twenty_cycle_strength)}")



### Puzzle 2 ###

# Functions neeeded
def _check_overlap(sprites_pos, cycle_number, pixel_line):
    """"""
    if cycle_number in sprites_pos:
        pixel_line += '#'
    else:
        pixel_line += '.'
    return pixel_line

def _add_cycle(cycle_number):
    if cycle_number + 1 > 39:
        cycle_number = 0
    else:
        cycle_number += 1
    return cycle_number

def _update_sprites_pos(sprites_pos, val):
    sprites_pos = [x+val for x in sprites_pos]
    return sprites_pos

# Calculation
cycle_number = 0; sprites_pos = [0,1,2]
pixel_line = ""
for iter, row in enumerate(raw_data):
    if row == 'noop':
        pixel_line = _check_overlap(sprites_pos, cycle_number, pixel_line)
        cycle_number = _add_cycle(cycle_number)
    else:
        addx, val = row.split(' ')
        val = int(val)
        pixel_line = _check_overlap(sprites_pos, cycle_number, pixel_line)
        cycle_number = _add_cycle(cycle_number)

        pixel_line = _check_overlap(sprites_pos, cycle_number, pixel_line)
        cycle_number = _add_cycle(cycle_number)
        
        sprites_pos = _update_sprites_pos(sprites_pos, val)
        

cycles = int(len(pixel_line)/40)
for i in range(cycles):
    print(pixel_line[i*40:(i+1)*40])

print(f"This answer can be seen by looking at the terminal output, answer: EKRHEPUZ")