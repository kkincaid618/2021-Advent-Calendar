# Read Data
f = open('./2020/Data/Day05Data.txt', 'r')
tickets = f.read().split('\n')
seats = []


for t in tickets:
    row_directions = t[0:7]
    col_directions = t[7:]

    high_slicer = 127
    low_slicer = 0

    for r in row_directions:
        if r == 'F':
            high_slicer = int((high_slicer - low_slicer) / 2) + low_slicer
        else:
            low_slicer = int((high_slicer - low_slicer) / 2) + low_slicer + 1

    row = low_slicer

    high_slicer = 7
    low_slicer = 0

    for c in col_directions:
        if c == 'L':
            high_slicer = int((high_slicer - low_slicer) / 2) + low_slicer
        else:
            low_slicer = int((high_slicer - low_slicer) / 2) + low_slicer

    col = high_slicer
    seat = row * 8 + col
    seats.append(seat)

seats.sort()
num_seats = len(seats)

for s in range(num_seats):
    gap = seats[s] - seats[s - 1]

    if gap == 2:
        my_seat = seats[s] - 1


max_seat = max(seats)

print(f'Part 1 Solution: The highest seat numbers in this batch is {max_seat}!')
print(f'Part 2 Solution: My seat is {my_seat}')