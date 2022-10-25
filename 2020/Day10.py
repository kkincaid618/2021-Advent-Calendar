path = './2020/Data/Day10Data.txt'
f = open(path, 'r')
values = f.read().split('\n')
adapters = [int(v) for v in values]
adapters.append(max(adapters) + 3)
adapters.sort()

differences = [adapters[0] - 0]

for i in range(len(adapters) - 1):
    adapter = adapters[i]
    min_possible = adapter + 1
    max_possible = adapter + 3
    all_possible = [a for a in adapters if a in list(range(min_possible, max_possible + 1))]
    selected_adapter = min(all_possible)
    diff = selected_adapter - adapter
    differences.append(diff)

    # print(f'{adapter} => {selected_adapter} => {differences}')

one_volt_diffs = len([d for d in differences if d == 1])
three_volt_diffs = len([d for d in differences if d == 3])

print(f'Part 1 Solution: {three_volt_diffs * one_volt_diffs}')