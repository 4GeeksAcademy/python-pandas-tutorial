import pandas as pd
# two dimensional array of name,age values.
data = [['Alex',10],['Bob',12],['Clarke',13]]

# create the dataframe and name the columns
df = pd.DataFrame(data,columns=['Name','Age'])

# print the dataframe
print(df)