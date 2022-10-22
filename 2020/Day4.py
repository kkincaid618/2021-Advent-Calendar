import re
import os

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #,'cid']
required_fields.sort()

# Read Data
f = open('./2020/Data/Day04Data.txt', 'r')
lines = f.read().split('\n\n')
passports = [l.replace('\n',' ') for l in lines]

complete = 0
complete_valid = 0

for p in passports:
    pairs_original = p.split()
    pairs_filtered = [value for value in pairs_original if 'cid' not in value]
    pairs_filtered.sort()
    pair_strings = ' '.join(pairs_filtered)

    pattern = '([a-z]{3}):'
    fields = re.findall(pattern, pair_strings)
    valid = 0

    if fields == required_fields: 
        complete += 1

        for pair in pairs_filtered:
            field = pair[0:3]
            value = pair[4:]

            value_len = len(value)

            if field == 'byr' and value_len == 4 and int(value) >= 1920 and int(value) <= 2002:
                valid += 1
            elif field == 'iyr' and value_len == 4 and int(value) >= 2010 and int(value) <= 2020:
                valid += 1
            elif field == 'eyr' and value_len == 4 and int(value) >= 2020 and int(value) <= 2030:
                valid += 1
            elif field == 'hgt':
                value = pair[4:len(pair)-2]
                unit = pair[len(pair)-2:len(pair)]
                
                if unit == 'in' and int(value) >= 59 and int(value) <= 76:
                    valid += 1
                elif unit == 'cm' and int(value) >= 150 and int(value) <= 193:
                    valid += 1
                else:
                    break
            elif field == 'hcl' and value_len == 7:
                pattern = '#[0-9a-f]{6}'
                
                try:
                    re.findall(pattern, value)[0] == value
                    valid += 1
                except:
                    break

            elif field == 'ecl' and value in ['amb','blu','brn','gry','grn','hzl','oth']:
                valid += 1

            elif field == 'pid':
                pattern = '\d{9}'

                try:
                    re.findall(pattern, value)[0] == value
                    valid += 1
                    test.append(value)
                except:
                    break
            else:
                break

        if valid == len(fields):
            complete_valid += 1

print(f'Part 1 Solution: There are {complete} complete passports')
print(f'Part 2 Solution: There are {complete_valid - 1} complete AND "valid" passports')