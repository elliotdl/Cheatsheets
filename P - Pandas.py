
# DATAFRAMES
import pandas as pd
df =pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['a','b','c'], columns=['x','y','z'])
df['col'].dtype
x.head()
df.iloc[1,2]          # slice
df.loc['row','col']   # slice

# rows
df.shape[0]    # nrow
df.index                # check names
df.reset_index          # index to column, integers as index
df.loc[:,'a']           # slice rows (by name)
df[ df['x']==1 ]                            # filter rows
df[ (df['x']==1) & (df['y'!='foo']) ]       # double filter rows
df['y'].str.contains('asdf')                # filter by string
df.sort_values['x','y']                     # sort rows by cols

# columns
df.columns                  # check names
df.shape[1]                     # ncol
df = df.rename(columns = {'index':'Doc'})
df.loc[:,'x']               # single slice (by name)
df.x
df = df.loc[:, ['x','z']]   # re-arrange / slice columns (by name)
df = df.loc[:, 'y':'z']     # slice columns (by range)
del df['y']                 # delete columns
df['col'].unique()          # unique vals
df['col'].value_counts()    # tally vals

# loop
for index, row in df.iterrows():
    df.loc[len(df) + 1] = [1 , 2 , 3 , 4]  # append row

# strings
df = df.replace(['a','b'],['c','d'])                # find & replace (exact)
df['col'] = df['col'].str.replace(r'\bfoo\b','asd')  # partial or regex
df.fillna(0)                                        # replace na and nan with 0

# concatenating DFs
df = df.merge(lookup_df, on='col', how='left')  # excel lookup
pd.concat([df1,df2])            # vstack
pd.concat([df1,df2], axis=1)    # hstack

df.groupby('x').count()
df.groupby('x').agg({'y':sum, 'z': np.mean})    # apply diff summary functions to columns after grouping
df.groupby('x').transform(lambda x: x/mean(x))   # apply every element that requires calculatin over whole grp
for name, group in df.groupby('col'):       # loop over groups


# transform (returns same index df as original)
my_func = lambda x: x.mean()/x.std()
df.groupby('x').transform(my_func)

# apply
df.apply(my_func)               # summary func, applied to each col
df.apply(my_func, axis=1)       # summary func, applied to each row
df.applymap(my_func)            # func applied to every element
df[df.apply(lambda x: sum(x)>1)]  # filter with apply


# series to list
df['col'].tolist()  # series to list
df['col'].toframe() # series to dataframe



# applying custom window fn to pandas
def my_func(x,y):
    return (x+y)

df['new col'] = np.vectorize(my_func)(df['x'],df['y'])