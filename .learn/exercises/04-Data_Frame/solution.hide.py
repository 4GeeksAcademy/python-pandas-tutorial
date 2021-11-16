import pandas as pd
# two dimensional array of name,age values.
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]

# create the dataframe and name the columns
df = pd.DataFrame(data,columns=['Brand', 'Make', 'Color'])

# print the dataframe
print(df)