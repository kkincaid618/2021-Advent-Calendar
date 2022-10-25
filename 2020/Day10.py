path = './2020/Data/Day10Data.txt'
f = open(path, 'r')
values = f.read().split('\n')
value_list = [int(v) for v in values]

print(value_list)