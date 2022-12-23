### Functions for puzzle 1 ###
def _iniate_new_folder_entry(folder_dict, folder):
    folder_dict[folder] = {}
    folder_dict[folder]['storage_size_for_files'] = 0
    folder_dict[folder]['full_storage_hierachy'] = 0
    folder_dict[folder]['files'] = []
    folder_dict[folder]['folder_sub'] = []
    if folder == '/':
        folder_dict[folder]['folder_up'] = ''
    else:
        current_folder_one_up = '-'.join(current_folder_list[:-1])
        folder_dict[folder]['folder_up'] = current_folder_one_up
    return folder_dict

def _if_listing_item(folder_dict, current_folder):
    if 'dir' not in line:
        size, filename = line.split()
        folder_dict[current_folder]['files'].append(filename)
        folder_dict[current_folder]['storage_size_for_files'] += int(size)
        folder_dict[current_folder]['full_storage_hierachy'] += int(size)
    else:
        sub_folder_here = current_folder + f'-{line[4:]}'
        folder_dict[current_folder]['folder_sub'].append(sub_folder_here)
    return folder_dict

def _if_cd_in_line(current_folder_list):
    if 'cd /' in line:
        current_folder_list = ['/']
    elif '..' not in line:
        current_folder_list.append(line[5:])
    else:
        current_folder_list.pop(-1)
    return current_folder_list

with open("data/advent_of_code_dec_07.txt", 'r') as f:
    raw_data = f.read().splitlines()


### Puzzle 1 ###
folder_dict = {}; current_folder_list = ['/']
for index, line in enumerate(raw_data):
    current_folder = '-'.join(current_folder_list)
    
    if current_folder not in list(folder_dict.keys()):
        folder_dict = _iniate_new_folder_entry(folder_dict, current_folder)

    if '$' not in line:
        folder_dict =_if_listing_item(folder_dict, current_folder)

    if '$ cd' in line:
        current_folder_list = _if_cd_in_line(current_folder_list)
        
# Find all folders with no sub folders
final_sub_folders = [folder for folder in list(folder_dict.keys()) if len(folder_dict[folder]['folder_sub'])==0]

# While loop to add hierachy folder sizes, starting from the folders with sub folders,
completed_folders = []; iteration_folders = final_sub_folders
while True:
    next_folders = []
    # Add folder size to the folder in one level up
    for sub_folder in iteration_folders:
        higher_folder = folder_dict[sub_folder]['folder_up']
        folder_dict[higher_folder]['full_storage_hierachy'] += folder_dict[sub_folder]['full_storage_hierachy']
        # Folder is now completed, and higher folder is qeued for next iteration
        completed_folders.append(sub_folder); next_folders.append(higher_folder)

    next_folders = list(set(next_folders))
    # Remove higher level element if not all sub folders are accounted for in completed list
    next_folders_temp = next_folders.copy()
    for index, next_folder in enumerate(next_folders_temp):
        check = all(item in completed_folders for item in folder_dict[next_folder]['folder_sub'])
        if check is False:
            next_folders.remove(next_folder)

    # Break at the last folder in the hierachy
    iteration_folders = next_folders.copy()
    if ['/'] == iteration_folders[:]:
        break
    

# Find accumlative size of folder
max_size = 100000; accumalative_size = 0
for folder in list(folder_dict.keys()):
    if folder_dict[folder]['full_storage_hierachy'] <= max_size:
        accumalative_size += folder_dict[folder]['full_storage_hierachy']

print(f"The accumalative size of folders under 100000: {accumalative_size}")

### Puzzle 2 ###
full_size = 70000000; needed_space = 30000000
used_space = folder_dict['/']['full_storage_hierachy']
min_folder = ''; min_storage = full_size
for folder in list(folder_dict.keys()):
    folder_size = folder_dict[folder]['full_storage_hierachy']
    if full_size - used_space + folder_size >= needed_space:
        if min_storage > folder_size:
            min_folder = folder; min_storage = folder_size

print(f"The smallest folder to do the job is of size: {min_storage}")
