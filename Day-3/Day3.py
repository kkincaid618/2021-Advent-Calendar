import pandas as pd
import numpy as np

def bin_to_dec(bin_val):
    dec_vals = np.array([])
    bin_length = len(bin_val)

    for i in range(0, bin_length):
        digit = int(bin_val[i])
        pwr = bin_length - 1 - i
        new_val = digit * pow(2,pwr)
        dec_vals = np.append(dec_vals,new_val)
    
    return dec_vals.sum()

def find_digits(df):
    if len(df) > 1:
        value_counts = df.value_counts()

        max_cnt = df.value_counts()[0]
        min_cnt = df.value_counts()[1]

        if max_cnt == min_cnt:
            max_value = 1
            min_value = 0
        else:
            max_value = df.value_counts().index[0]
            min_value = df.value_counts().index[1]
    else:
        max_value = df.iloc[0]
        min_value = df.iloc[0]

    return min_value, max_value

####################################

data = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
    ]

df = pd.read_csv('Day3.csv',dtype=str)
# df = pd.DataFrame(data,columns=['data'])
df = df.data.apply(list).apply(pd.Series).astype(int)

gamma = ''
epsilon = ''

for col in df.columns:
    e, g = find_digits(df.loc[:,col])

    gamma = gamma + str(g)
    epsilon = epsilon + str(e)

gamma = bin_to_dec(gamma)
epsilon = bin_to_dec(epsilon)

power_consumption = int(gamma * epsilon)

print('Part 1 Answer: ',power_consumption)

######################################################

min_values = ''
max_values = ''

df2 = df

for col in df2.columns:
    min, max = find_digits(df2.loc[:,col])
    df2 = df2[df2[col]==max]

    max_values = max_values + str(max)

df2 = df

for col in df2.columns:
    min, max = find_digits(df2.loc[:,col])
    df2 = df2[df2[col]==min]

    min_values = min_values + str(min)

ox_gen = bin_to_dec(max_values)
co2_rating = bin_to_dec(min_values)
life_rating = ox_gen * co2_rating

print('Part 2 Answer: ',int(life_rating))
