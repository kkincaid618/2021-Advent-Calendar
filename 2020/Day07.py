import re

path = './2020/Data/Day07Data.txt'
f = open(path, 'r')

lines = f.read().split('\n')
pattern1 = '([a-z]+\s[a-z]+)(?=\sbags*)'
pattern2 = '\d\s([a-z]+\s[a-z]+)'
data = [x.split(' contain ') for x in lines]
rules = [[re.findall(pattern1, r[0]), re.findall(pattern2, r[1])] for r in data]

sets = {}

for i in range(len(rules)):
    parent = ''.join(rules[i][0])
    children = rules[i][1]

    sets[parent] = children

bag = ['shiny gold']
options = []

while bag != []:
    for b in bag:
        option = {key: value for (key, value) in sets.items() if b in value}
        bag = list(option.keys())
        # print(bag)
        options.append(b)

print([o for o in options if o != 'shiny gold'])
print(set([o for o in options if o != 'shiny gold']))
print(len(set([o for o in options if o != 'shiny gold'])))