from os import X_OK
import pandas as pd
import numpy as np

df = pd.read_csv('day2.csv')

#Split data into separate columns and name them
df = df['pw'].str.extract('^(\d+)-(\d+)\s(\w):\s(\w+)$')
df.columns = ['min','max','letter','pw']

# Convert from string to int
df['min'] = df['min'].astype('int64')
df['max'] = df['max'].astype('int64')

# Create empty array to store values
num_letters_found = np.array([])
pos_one_arr = np.array([])
pos_two_arr = np.array([])

# Loop through each row to determine how many letters are in each password & populate array
for i in df.index:
    pw_val = df.iloc[i]['pw']
    letter = df.iloc[i]['letter']
    pos_one = df.iloc[i]['min'] - 1
    pos_two = df.iloc[i]['max'] - 1

    cnt = pw_val.count(letter)
    pos_one_val = pw_val[pos_one]
    pos_two_val = pw_val[pos_two]

    num_letters_found = np.append(num_letters_found, cnt)
    pos_one_arr = np.append(pos_one_arr, pos_one_val)
    pos_two_arr = np.append(pos_two_arr, pos_two_val)

# Add array back to data frame
df['num_found'] = num_letters_found
df['test1'] = (df['num_found'] >= df['min']) & (df['num_found'] <= df['max'])

df['pos_one'] = pos_one_arr
df['pos_two'] = pos_two_arr
df['test2'] = ((df['pos_one'] == df['letter']) & (df['pos_two'] != df['letter'])) | ((df['pos_two'] == df['letter']) & (df['pos_one'] != df['letter']))

# How many are valid?
valid = len(df[df['test1']]==True)
invalid = len(df.index) - valid
print('Part 1: There are {x} valid passwords and {y} invalid passwords'.format(x=valid, y=invalid))

valid2 = len(df[df['test2']==True])
invalid2 = len(df.index) - valid2
print('Part 2: There are {x} valid passwords and {y} invalid passwords'.format(x=valid2, y=invalid2))