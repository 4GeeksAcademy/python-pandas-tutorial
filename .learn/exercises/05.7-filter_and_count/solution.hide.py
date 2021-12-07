import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(len(data_frame.loc[data_frame['Legendary'] == True]))