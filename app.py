import pandas as pd

data = pd.read_csv('.learn/assets/pokemon_data.csv')

print(data.iloc[133,6])