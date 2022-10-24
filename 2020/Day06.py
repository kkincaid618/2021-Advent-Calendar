path = './2020/Data/Day06Data.txt'
f = open(path, 'r')

lines = f.read().split('\n\n')
groups = [x.replace('\n','') for x in lines]
people = [x.split('\n') for x in lines]

# Part 1
yes_answers = [list(x) for x in groups if x != '\n']
distinct_answers = [set(x) for x in yes_answers]
num_distinct = [len(x) for x in distinct_answers]
print(f'Part 1 Solution: {sum(num_distinct)}')

# Part 2
num_per_group = [len(x) for x in people]
yes_counter = 0

for i in range(len(groups)):
    yes_responses = set(groups[i])
    len_group = num_per_group[i]

    for r in yes_responses:
        count_responses = len([x for x in groups[i] if x == r])
        if count_responses == len_group:
            yes_counter += 1

print(f'Part 2 Solution: {yes_counter}')


        