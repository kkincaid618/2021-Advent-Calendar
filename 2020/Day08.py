path = './2020/Data/Day08Data.txt'
f = open(path, 'r')
instr = f.read().split('\n')
instr = [x.split() for x in instr]
acc = 0
loop = []
repeat_flag = False

i = 0
j = 0

while repeat_flag == False:
    instr_type = instr[i][0]
    instr_magn = instr[i][1]
    instr_direction = instr_magn[0]
    instr_amount = instr_magn[1:]

    # print(f'{instr_type}: {instr_direction} {instr_amount}')

    if i not in loop:
        loop.append(i)
    else:
        print(f'Part 1 Solution: The accumulator value is {acc}')
        repeat_flag = True
    
    if instr_type == 'nop':
        i += 1
    elif instr_type == 'jmp':
        if instr_direction == '+':
            i += int(instr_amount)
        else:
            i -= int(instr_amount)
    elif instr_type == 'acc':
        i += 1

        if instr_direction == '+':
            acc += int(instr_amount)
        else:
            acc -= int(instr_amount)

    j += 1