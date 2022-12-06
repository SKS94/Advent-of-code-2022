import numpy as np

### First puzzle ###
max_calorie_elf, temp_calorie_count = 0, 0
f = open("data/advent_of_code_dec_01.txt")
for line in f:
    if line != "\n":
        temp_calorie_count += int(line)
    else:
        max_calorie_elf = temp_calorie_count if max_calorie_elf < temp_calorie_count else max_calorie_elf
        temp_calorie_count = 0        
f.close()
print(f"The maximum calories carried by one elf is: {max_calorie_elf}")


### Second puzzle ###
max_calorie_elf, temp_calorie_count = [0, 0, 0], 0
f = open("data/advent_of_code_dec_01.txt")
for line in f:
    if line != "\n":
        temp_calorie_count += int(line)
    else:
        # As long as the list is sorted only last list item has to checked.
        max_calorie_elf[-1] = temp_calorie_count if max_calorie_elf[-1] < temp_calorie_count else max_calorie_elf[-1]
        max_calorie_elf.sort(reverse=True)
        temp_calorie_count = 0        
f.close()

print(f"The maximum calories carried by the top three elves are: {max_calorie_elf}")
print(f"Sum of the above: {sum(max_calorie_elf)}")