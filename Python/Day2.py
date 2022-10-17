##### PART 1 #####

# Read Data
with open('./Data/Day02Data.txt', 'r') as f:
     lines = [line.rstrip(',\n') for line in f]

instructions = [l.split(' ') for l in lines]

x = 0 # horizontal position
y = 0 # depth
a = 0 # aim

x2 = 0 # 2nd method
y2 = 0 # 2nd method

for d in instructions:
    direction = d[0]
    magnitude = int(d[1])

    if direction == 'up':
        y -= magnitude

        a -= magnitude
    elif direction == 'down':
        y += magnitude
        
        a += magnitude
    elif direction == 'forward':
        x += magnitude

        x2 += magnitude
        y2 += a * magnitude

print(f'Part 1 Solution: Horizontal Position * Depth = {x} * {y} = {x*y}')
print(f'Part 2 Solution: Horizontal Position * Depth = {x2} * {y2} = {x2*y2}')