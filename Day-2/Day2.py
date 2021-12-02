import pandas as pd
import numpy as np

df = pd.read_csv('Day2.csv')

##### Part 1
df = df['directions'].str.extract('(\w+)\s(\d+)')
df.columns = ['direction','amount']
df['amount'] = df['amount'].astype('int64')

df['plane'] = np.where(df['direction']=='forward','horizontal','vertical')
df['multiplier'] = np.where(df['direction']=='up',-1,1)
df['net_change'] = df['multiplier'] * df['amount']

product1 = df.loc[:,['plane','net_change']].groupby(['plane']).sum().product().item()

print('Part 1: The product of the current position is {x}'.format(x=product1))

##### Part 2
df['aim'] = np.where(df['plane']=='vertical',df['net_change'],0)
df['position'] = np.where(df['plane']=='horizontal',df['net_change'],0)

df['curr_aim'] = df['aim'].cumsum()
df['curr_position'] = df['position'].cumsum()

df['depth'] = np.where(df['plane']=='horizontal',df['net_change']*df['curr_aim'],0)
df['curr_depth'] = df['depth'].cumsum()

max_row = max(df.index)

last_position = df[df.index==max_row]
last_position = last_position.loc[:,['curr_depth','curr_position']]

product2 = last_position['curr_depth'].item()*last_position['curr_position'].item()

print('Part 2: The product of the real current position is {x}'.format(x=product2))