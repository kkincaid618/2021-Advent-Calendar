from os import X_OK
import pandas as pd

df = pd.read_csv('day1.csv')
target = 2020

#Loop through each value in the data and determine if the number it needs to add with to get to 2020 is present in the data
for i in df.index:
    val = df.iloc[i,0]
    diff = target - val
    search = df.loc[df['amounts']==diff]['amounts']
    
    if len(search.index) > 0:
        product = val * search.item()
        print('Part 1: The numbers {a} and {b} add up to 2,020, so the answer is {a} * {b} = {c}'.format(a=val,b=search.item(),c=product))
        break

for i in df.index:
    val = df.iloc[i,0]
    for j in range(1,len(df.index)):
        val2 = df.iloc[j,0]
        
        diff = target - val - val2
        if diff > 0:
            search = df.loc[df['amounts']==diff]['amounts']

            if len(search.index) > 0:
                product = val * val2 * search.item()
                print('Part 2: The numbers {a} and {b} and {c} add up to 2,020, so the answer is {a} * {b} * {c} = {d}'.format(a=val,b=val2,c=search.item(),d=product))
                break
    else:
        continue
    break
