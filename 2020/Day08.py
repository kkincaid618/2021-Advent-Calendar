def run_loop(instr):
    acc = 0
    loop = []

    is_inf_loop = False
    i = 0

    while is_inf_loop == False and i <= len(instr) - 1:
        instr_type = instr[i][0]
        instr_magn = instr[i][1]
        instr_direction = instr_magn[0]
        instr_amount = instr_magn[1:]

        # print(f'{instr_type}: {instr_direction} {instr_amount}')

        if i not in loop:
            loop.append(i)
        else:
            is_inf_loop = True
            return is_inf_loop, acc
        
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

        if i >= len(instr):
            return is_inf_loop, acc

def perturb_loop(instr):

    new_loop = instr.copy()

    for i in range(len(new_loop)):
        instr_type = new_loop[i][0]
        instr_magn = new_loop[i][1]
        instr_direction = instr_magn[0]
        instr_amount = instr_magn[1:]

        if instr_type == 'nop':
            new_loop[i] = ['jmp', instr_magn]
            is_inf_loop, last_acc = run_loop(new_loop)
        elif instr_type == 'jmp':
            new_loop[i] = ['nop', instr_magn]
            is_inf_loop, last_acc = run_loop(new_loop)
        else:
            is_inf_loop = True
            new_loop = new_loop

        new_loop = instr.copy()

        if is_inf_loop == False:
            # print(i, ' ',new_loop, ' ', is_inf_loop, ' ', last_acc)
            return last_acc

path = './2020/Data/Day08Data.txt'
f = open(path, 'r')
instr = f.read().split('\n')
instr = [x.split() for x in instr]

x = perturb_loop(instr)
print(x)
            