##### PART 1 #####

# Read Data
with open('./Data/Day01Data.txt', 'r') as f:
     lines = [line.rstrip(',\n') for line in f]

# Initialize counting variable
counter = 0
lines = [int(l) for l in lines]

# Loop through list to determine pattern
for i in range(1, len(lines)):
    this_num = lines[i]
    prev_num = lines[i - 1]
    
    if this_num > prev_num: 
        counter += 1

print(f'Part 1 Solution: There are {counter} measurements that are larger than the previous measurement')

##### PART 2 #####

n = 3 # Sliding window size
counter = 0

for i in range(4, len(lines) + 1):
    this_window = lines[(i - n):i]
    last_window = lines[(i - n - 1):(i - 1)]

    this_sum = sum(this_window)
    last_sum = sum(last_window)

    if this_sum > last_sum:
        counter += 1

print(f'Part 2 Solution: There are {counter} measurement windows that are larger than the previous measurement window')