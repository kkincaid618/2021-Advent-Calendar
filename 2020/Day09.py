def check_one_number(preamble_values, number_to_check):
    for i in range(len(preamble_values)):
        this_value = preamble_values[i]
        delt_value = number_to_check - this_value

        if delt_value in preamble_values:
            return True

        if i == len(preamble_values) - 1:
            return False

def check_all_numbers(value_list, n_preamble_size):
    is_valid = True
    i = n_preamble_size

    while is_valid == True:
        preamble_values = value_list[(i - n_preamble_size):i]
        num_to_eval = value_list[i] 
        is_valid = check_one_number(preamble_values, num_to_eval)

        i += 1

    return num_to_eval

def find_set(value_list, buggy_value):
    slice_size = len(value_list) - 1
    
    while slice_size >=2:
        max_start_i = len(value_list) - slice_size
        pos_start_i = [i for i, j in enumerate(value_list) if i <= max_start_i]
        
        for i in range(len(pos_start_i)):
            sliced = value_list[i:(i + slice_size)]
            
            if sum(sliced) == buggy_value:
                max_value = max(sliced)
                min_value = min(sliced)

                return max_value + min_value
        
        slice_size -= 1

    return 0

path = './2020/Data/Day09Data.txt'
f = open(path, 'r')
values = f.read().split('\n')
value_list = [int(v) for v in values]

preamble = 25

buggy_value = check_all_numbers(value_list, preamble)
print(f'Part 1 Solution: {buggy_value} is the first invalid number')

encryption_weakness = find_set(value_list, buggy_value)
print(f'Part 2 Solution: {encryption_weakness} is the encryption_weakness')
