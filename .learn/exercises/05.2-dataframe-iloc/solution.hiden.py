import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

print(data_frame.iloc[133,6])