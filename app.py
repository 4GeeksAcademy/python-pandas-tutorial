import pandas as pd

file = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(file.head())
#print(file.columns)
# print(file['Name'])
# print(file['Name'])
# print(file['Name'][0:5])
#print(file[['Name','Type 1']])
print(file.iloc[2,1])