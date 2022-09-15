import pandas as pd
import numpy as np

### Part 1
df = pd.read_csv('input_data.csv')
df['change'] = df['depths'].diff() # Calculate depth change
df['direction'] = np.where(
                            df['change'] < 0, 
                            'decrease', 
                            np.where(
                                df['change'] > 0, 
                                'increase', 
                                'no change')) # Categorize change
inc = len(df.loc[df['direction']=='increase']) # Count number of increases
print('Part 1 Answer: There are {x} increases in depth measurement'.format(x=inc))

#############################

### Part 2
df['sliding_window'] = df['depths'].rolling(3,min_periods=3).sum() # Calculate rolling depth
df['sliding_change'] = df['sliding_window'].diff() # Calculate depth change
df['sliding_direction'] = np.where(
                                    df['sliding_change'] < 0, 
                                    'decrease', 
                                    np.where(
                                        df['sliding_change'] > 0, 
                                        'increase', 
                                        'no change')) # Categorize change
sliding_inc = len(df.loc[df['sliding_direction']=='increase']) # Count number of increases
print('Part 2 Answer: There are {x} increases in depth measurement'.format(x=sliding_inc))

