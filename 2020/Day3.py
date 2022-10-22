import pandas as pd
import numpy as np

df = pd.read_csv('day3.csv')
df = df['data'].str.split('',expand=True)
df.drop([0,32],axis=1,inplace=True)

def find_trees(x_slope,y_slope,df):
    # Determine number of times to repeat the data
    num_rows = len(df.index)
    num_cols = len(df.columns)
    min_col = x_slope * num_rows

    # Loop to repeat the data
    copy_value = df

    while len(df.columns) < min_col:
        df = df.merge(copy_value,left_index=True,right_index=True)
    
    count = 0
    row = 0
    col = 0

    while row < len(df.index):
        val = df.iloc[row,col]
        if val == '#':
            count += 1

        row += y_slope
        col += x_slope

    print("I ran into {n} trees with a path of {x_slope} right and {y_slope} down".format(n=count,x_slope=x_slope,y_slope=y_slope))
    return count

##########

slopes_list = [[1,1],[3,1],[5,1],[7,1],[1,2]]
trees_list = np.array([])
for item in slopes_list:
    x_slope = item[0]
    y_slope = item[1]
    
    count = find_trees(x_slope,y_slope,df)
    trees_list = np.append(trees_list,count)

product = 1

for item in trees_list:
    product = product * item

print(trees_list)
print(product)