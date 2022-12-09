def set_search_unique_charecters(num_of_charecters):
    for i in range(len(raw_data) - num_of_charecters):
        search_array = raw_data[i:i+num_of_charecters]
        
        # if set is len four the items are unique
        if len(set(search_array)) == num_of_charecters:
            index_for_first_seq_change = i+num_of_charecters
            break

    return index_for_first_seq_change

with open("data/advent_of_code_dec_06.txt", 'r') as f:
    raw_data = f.readline()

### Puzzle 1 ###
index_packet_marker_change = set_search_unique_charecters(num_of_charecters=4)
print(f"Puzzle 1: Number of characters processed before first start of packet marker: {index_packet_marker_change}")

### Puzzle 2 ###

index_message_marker_change = set_search_unique_charecters(num_of_charecters=14)
print(f"Puzzle 1: Number of characters processed before first start of message marker: {index_message_marker_change}")