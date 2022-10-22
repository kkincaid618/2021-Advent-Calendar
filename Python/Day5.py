##### PART 1 #####

# Read Data
with open('./Data/Day05Data.txt', 'r') as f:
     lines = [line.rstrip(',\n') for line in f]

instructions = [l.split(' -> ') for l in lines]
# x1 = instructions[0][0][0]

x1 = [[[int(i[0][0]), int(i[0][2])], [int(i[1][0]), int(i[1][2])]] for i in instructions]

x = [int(i[0]) for i in instructions]
print(x)
print(x1)
all_x = [j for j in instructions]
# max_x = max(x1)
# max_y = max(y1)

# print(all_x)