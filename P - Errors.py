# Be consistent whether looping over item or index

# Methods that modify that original vs x=x.method

# using 'in' with pandas
x in df['col'].values   # will not work without .values

# pandas dataframe cols must all be same datatype

# if using loc, but deleted index 0 row = PROBLEMS
# dont use .loc until you've made sure you dont have  duplicate indices!!!

# if making changes to a line 'y=x' probably want 'y=x.copy()'

# cant store lists / python objects inside a pandas df

# if you have 2 rows in df with same index, and write to that index, both rows will change.

#slicing a list by booleans
list = ['a', 'b', 'c']
bool = [False, True, False]
result = np.array(list)[ np.array(bool) ]

